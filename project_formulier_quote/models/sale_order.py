# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrderInherit(models.Model):
    """ Sale Order Temp"""

    _name = "sale.order.temp"
    _inherit = "sale.order"
    _description = "Sale Order Temp"

    order_line = fields.One2many('sale.order.line.temp', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
    transaction_ids = fields.Many2many('payment.transaction', 'sale_order_transaction_temp_rel', 'sale_order_id', 'transaction_id',
                                       string='Transactions', copy=False, readonly=True)
    tag_ids = fields.Many2many('crm.tag', 'sale_order_tag_temp_rel', 'order_id', 'tag_id', string='Tags')

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist.id)
        result = super(SaleOrderInherit, self).create(vals)
        return result


class SaleOrderLineInherit(models.Model):
    """ Sale Order Line Temp"""

    _name = "sale.order.line.temp"
    _inherit = "sale.order.line"
    _description = "Sale Order Line Temp"

    order_id = fields.Many2one('sale.order.temp', string='Sale Order Temp')
    invoice_lines = fields.Many2many('account.move.line', 'sale_order_line_invoice_temp_rel', 'order_line_id', 'invoice_line_id', string='Invoice Lines', copy=False)


class QuoteTemplate(models.Model):
    _inherit = "sale.order.template"

    xaa_aa_task_product_id = fields.Many2one('product.product', string='Task product')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    xaa_aa_cost_price_total = fields.Float(string='Total cost price')
    xaa_aa_commission = fields.Float(string='Total commission')
