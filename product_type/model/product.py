# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    xaa_aa_producttype = fields.Selection([
        ('vloer','Vloer'),('muur','Muur'),
        ('dak','Dak'),('pv','PV')], string="Product Type")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    xaa_aa_producttype = fields.Selection([
        ('vloer','Vloer'),('muur','Muur'),
        ('dak','Dak'),('pv','PV')], string="Product Type")

    @api.onchange('product_id')
    def product_producttype(self):
        for rec in self:
            if rec.product_id.xaa_aa_producttype:
                rec.xaa_aa_producttype = rec.product_id.xaa_aa_producttype

class SaleReport(models.Model):
    _inherit = "sale.report"

    xaa_aa_producttype = fields.Selection([
        ('vloer','Vloer'),('muur','Muur'),
        ('dak','Dak'),('pv','PV')], string="Product Type")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['xaa_aa_producttype'] = ",l.xaa_aa_producttype"
        groupby += """
            , l.xaa_aa_producttype
        """
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
