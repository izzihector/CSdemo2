# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleLineConfig(models.Model):
    _inherit = "sale.line.config"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_three', 'intake PV')])


class SaleLineWizard(models.TransientModel):
    _inherit = "sale.line.config.wizard"

    def add_lines(self):
        super(SaleLineWizard, self).add_lines()
        if self.xaa_aa_formulier_type == 'formulier_three':
            Product = self.env['product.product'].sudo()
            SaleOrderLine = self.env['sale.order.line'].sudo()
            if self.xaa_aa_qty_hours:
                hours,hours_cost,hours_sales,overhead_total,overhead_sale_total=1,0,0,0,0
                sale_conf = self.env['sale.line.config'].search([
                    ('xaa_aa_qty_hours', '=', self.xaa_aa_qty_hours),
                    ('xaa_aa_formulier_type', '=', 'formulier_three')],limit=1)
                if sale_conf:
                    hours = sale_conf.xaa_aa_qty_hours
                    hours_cost = sale_conf.xaa_aa_team_cost
                    hours_sales = sale_conf.xaa_aa_team_sale
                    overhead_total = sale_conf.xaa_aa_overhead_total
                    overhead_sale_total = sale_conf.xaa_aa_sales_overhead_total

                vat_id = Product.search([
                    ('xaa_aa_product_type', '=', 'BTW teruggave')], limit=1)
                material_id = Product.search([
                    ('xaa_aa_product_type', '=', 'Overige Materialen')], limit=1)
                stekkers_id = Product.search([
                    ('xaa_aa_product_type', '=', 'Stekkers')], limit=1)
                installation_product = Product.search([
                    ('name', 'ilike', 'Montage kosten zonnepanelen')], limit=1)
                task_product = Product.search([
                    ('name','ilike','Projectbegeleiding PV')], limit=1)
                overhead_product = self.env.ref('formulier_quote_set_lines.overhead_product', False)
                if vat_id:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': vat_id.id,
                        'product_uom_qty': 1,
                        'discount': 100,
                        })
                if stekkers_id:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': stekkers_id.id,
                        'product_uom_qty': 1,
                        })
                if installation_product:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': installation_product.id,
                        'product_uom_qty': 1,
                        'price_unit': hours_sales or installation_product.lst_price,
                        'purchase_price': hours_cost or installation_product.standard_price,
                    })
                if material_id:
                    SaleOrderLine.create({
                        'order_id': self.xaa_aa_sale_id.id,
                        'product_id': material_id.id,
                        'product_uom_qty': 1,
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
