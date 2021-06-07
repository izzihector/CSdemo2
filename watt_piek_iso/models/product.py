# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    xaa_aa_watt_piek = fields.Float(string="Watt Peak")
    xaa_aa_iso = fields.Float(string="ISO")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _order_watt_piek_and_iso(self):
        """ Calculates Sub total for watt peak and iso"""
        for order in self:
            total_watt_piek = 0.0
            total_order_iso = 0.0
            for line in order.order_line:
                total_watt_piek += line.xaa_aa_total_watt_piek
                total_order_iso += line.xaa_aa_total_iso
            order.xaa_aa_order_watt_piek = total_watt_piek
            order.xaa_aa_order_iso = total_order_iso

    xaa_aa_order_watt_piek = fields.Monetary(compute='_order_watt_piek_and_iso', string="Order Watt Peak")
    xaa_aa_order_iso = fields.Monetary(compute='_order_watt_piek_and_iso', string="Order ISO")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_id','xaa_aa_watt_piek', 'xaa_aa_iso', 'product_uom_qty')
    def _sub_total_watt_piek_and_iso(self):
        """ Calculates Sub total for watt peak and iso"""
        for line in self:
            if line.product_id and line.product_id.xaa_aa_watt_piek > 0.0 or line.product_id.xaa_aa_iso > 0.0:
                line.xaa_aa_total_watt_piek = line.product_uom_qty * line.xaa_aa_watt_piek
                line.xaa_aa_total_iso = line.product_uom_qty * line.xaa_aa_iso
            else:
                line.xaa_aa_total_iso = 0.0
                line.xaa_aa_total_watt_piek = 0.0

    xaa_aa_watt_piek = fields.Float(related="product_id.product_tmpl_id.xaa_aa_watt_piek",string="Watt Peak")
    xaa_aa_iso = fields.Float(related="product_id.product_tmpl_id.xaa_aa_iso",string="ISO")
    xaa_aa_total_watt_piek = fields.Float(compute='_sub_total_watt_piek_and_iso', string="Total Watt Peak",store=True)
    xaa_aa_total_iso = fields.Float(compute='_sub_total_watt_piek_and_iso', string="Total ISO",store=True)