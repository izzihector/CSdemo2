# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    xaa_aa_watt_piek = fields.Float(string='Watt Peak', digits=(16, 0), compute="_compute_watt_pick")
    xaa_aa_rendement = fields.Float(string='Efficiency', default=88, digits=(16, 0))
    xaa_aa_jaaropbrengsten = fields.Float(
        string='Annual yields', compute="calculate_all")
    xaa_aa_jaaropbrengst_prijs_van = fields.Monetary(
        string='Annual yield price of', default=0.22)
    xaa_aa_totale_verwachte_jaaropbrengst_van_de = fields.Float(
        string='Total expected annual yield of the', compute="calculate_all", digits=(16, 0))
    xaa_aa_verwachte_terugverdientijd = fields.Float(
        string='Expected payback time', compute="calculate_all", digits=(16, 1))
    xaa_aa_related_amount_untaxed = fields.Monetary(related='amount_untaxed', string='Untaxed Amount')

    @api.depends('order_line')
    def _compute_watt_pick(self):
        for rec in self:
            total = 0.0
            for line in rec.order_line:
                if line.product_uom_qty > 0.0:
                    total += line.product_uom_qty * line.xaa_aa_watt_piek
            rec.xaa_aa_watt_piek = total


    @api.depends('xaa_aa_watt_piek', 'xaa_aa_rendement')
    def calculate_all(self):
        for rec in self:
            if rec.xaa_aa_watt_piek and rec.xaa_aa_rendement:
                rec.xaa_aa_jaaropbrengsten = rec.xaa_aa_rendement / 100 * rec.xaa_aa_watt_piek
                rec.xaa_aa_totale_verwachte_jaaropbrengst_van_de = rec.xaa_aa_jaaropbrengst_prijs_van * \
                    rec.xaa_aa_jaaropbrengsten
                if rec.xaa_aa_totale_verwachte_jaaropbrengst_van_de != 0:
                    rec.xaa_aa_verwachte_terugverdientijd = rec.xaa_aa_related_amount_untaxed / \
                        rec.xaa_aa_totale_verwachte_jaaropbrengst_van_de
            else:
                rec.xaa_aa_jaaropbrengsten = 0
                rec.xaa_aa_totale_verwachte_jaaropbrengst_van_de = 0
                rec.xaa_aa_verwachte_terugverdientijd = 0

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if res.sale_order_template_id:
            res.fill_calculations_value()
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if vals.get('sale_order_template_id'):
            self.fill_calculations_value()
        return res

    def fill_calculations_value(self):
        footer = ""
        description = ""
        cal_dict = {}
        if self.website_description:
            description = self.website_description.encode('utf-8')
        if self.xaa_aa_website_desc_footer:
            footer = self.xaa_aa_website_desc_footer.encode('utf-8')
        if description or footer:
            currency = self.currency_id.symbol
            cal_dict ={
                '<td id="id_1" style="width:20%"></td>': '<td id="id_1" style="width:20%">'+
                 str("%.2f" % self.xaa_aa_watt_piek or 0.0) +'</td>',
                '<td id="id_2" style="width:20%"></td>': '<td id="id_2" style="width:20%">'+
                 currency +' ' +str(self.xaa_aa_jaaropbrengst_prijs_van) +'</td>',
                '<td id="id_3" style="width:20%"></td>': '<td id="id_3" style="width:20%">'+
                 str("%.f" % self.xaa_aa_jaaropbrengsten) +'</td>',
                '<td id="id_4" style="width:20%"></td>': '<td id="id_4" style="width:20%">'+
                 str(self.xaa_aa_rendement) +'%</td>',
                '<td id="id_5" style="width:20%"></td>': '<td id="id_5" style="width:20%">'+
                 str("%.2f" % self.xaa_aa_verwachte_terugverdientijd) +'</td>',
                '<td id="id_6" style="width:20%"></td>': '<td id="id_6" style="width:20%">'+
                 str("{:,.2f}".format(self.xaa_aa_totale_verwachte_jaaropbrengst_van_de).replace('.',',').replace(',','.', 1))+
                '</td>',
                '<td id="id_7" style="width:20%"></td>': '<td id="id_7" style="width:20%">'+
                 currency +' '+str("{:,.2f}".format(self.xaa_aa_related_amount_untaxed).replace('.',',').replace(',','.', 1))+
                '</td>',
            }
        if description:
            for key, val in cal_dict.items():
                description = description.replace(
                    key.encode('utf-8'), val.encode('utf-8'))
            self.website_description = description
        if footer:
            for key, val in cal_dict.items():
                footer = footer.replace(
                    key.encode('utf-8'), val.encode('utf-8'))
            self.xaa_aa_website_desc_footer = footer