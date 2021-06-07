# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleLineConfig(models.Model):
    _inherit = "sale.line.config"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_two', 'intake ISO')])


class SaleLineWizard(models.TransientModel):
    _inherit = "sale.line.config.wizard"

    def add_lines(self):
        super(SaleLineWizard, self).add_lines()
        if self.xaa_aa_formulier_type == 'formulier_two':
            Product = self.env['product.product'].sudo()
            SaleOrderLine = self.env['sale.order.line'].sudo()
            if self.xaa_aa_qty_hours:
                hours,hours_cost,hours_sales,overhead_total,overhead_sale_total=1,0,0,0,0
                sale_conf = self.env['sale.line.config'].search([
                    ('xaa_aa_qty_hours', '=', self.xaa_aa_qty_hours),
                    ('xaa_aa_formulier_type', '=', 'formulier_two')],limit=1)
                if sale_conf:
                    hours = sale_conf.xaa_aa_qty_hours
                    hours_cost = sale_conf.xaa_aa_team_cost
                    hours_sales = sale_conf.xaa_aa_team_sale
                    overhead_total = sale_conf.xaa_aa_overhead_total
                    overhead_sale_total = sale_conf.xaa_aa_sales_overhead_total

                service_product = Product.search([
                    ('name', 'ilike', 'Aanbrengen spouwmuurisolatie')],limit=1)
                certificate_product = Product.search([
                    ('xaa_aa_product_type', '=', 'SKG IKOB Certification payment')],limit=1)
                task_product = Product.search([
                    ('name','ilike','Projectbegeleiding Isolatie')], limit=1)
                overhead_product = self.env.ref('formulier_quote_set_lines.overhead_product', False)
                if service_product:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': service_product.id,
                        'product_uom_qty': 1,
                        'price_unit': hours_sales or service_product.lst_price,
                        'purchase_price': hours_cost or service_product.standard_price,
                    })
                if certificate_product:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': certificate_product.id,
                        'product_uom_qty': self.xaa_aa_product_qty or 1,
                    })
                if overhead_product:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': overhead_product.id,
                        'product_uom_qty': 1,
                        'purchase_price': overhead_total or overhead_product.standard_price,
                        'price_unit': overhead_sale_total or overhead_product.lst_price,
                        })
                if task_product:
                    SaleOrderLine.create({
                            'order_id': self.xaa_aa_sale_id.id,
                            'product_id': task_product.id,
                            'product_uom_qty': hours,
                        })


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def add_formulier_lines(self):
        if (self.xaa_aa_formulier_type == 'formulier_two'):
            panel_line = False
            for line in self.order_line:
                if line.product_id.categ_id.name in ['Cavity','Spouw']:
                    panel_line = line
            if panel_line:
                hours=False
                sale_conf = self.env['sale.line.config'].search([
                    ('xaa_aa_formulier_type','=','formulier_two'),
                    ('xaa_aa_qty','=',panel_line.product_uom_qty)],limit=1)
                if sale_conf:
                    hours = sale_conf.xaa_aa_qty_hours
                ctx = {
                    'default_xaa_aa_sale_id': self.ids[0],
                    'default_xaa_aa_qty_hours': hours,
                    'default_xaa_aa_formulier_type': 'formulier_two',
                    'default_xaa_aa_product_qty': panel_line.product_uom_qty,
                }
                view_id = self.env.ref('formulier_quote_set_lines.view_sale_line_form', False)
                if view_id:
                    return {
                        'type': 'ir.actions.act_window',
                        'view_mode': 'form',
                        'res_model': 'sale.line.config.wizard',
                        'views': [(view_id.id, 'form')],
                        'view_id': view_id.id,
                        'target': 'new',
                        'context': ctx,
                    }
        else:
            return super(SaleOrder, self).add_formulier_lines()
