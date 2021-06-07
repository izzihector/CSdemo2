# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, api, fields, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    xaa_aa_invisible = fields.Boolean(string='Not Visible')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    xaa_aa_invisible = fields.Boolean(string='Not Visible')

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if self.product_id:
            self.xaa_aa_invisible = self.product_id.xaa_aa_invisible
        return res

    @api.model
    def create(self, vals):
        res = super(SaleOrderLine,self).create(vals)
        if res.product_id and not res.xaa_aa_invisible:
            res.xaa_aa_invisible = res.product_id.xaa_aa_invisible
        return res