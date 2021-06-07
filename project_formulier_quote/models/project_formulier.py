# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProjectFormulier(models.Model):
    _inherit = "question.formulier"

    xaa_aa_need_discount = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do You need Discount ?',
        tracking=True, default='nee')
    xaa_aa_discount_product = fields.Many2one('product.product', string='Select Discount',
        tracking=True)
    xaa_aa_need_schouw = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do a look?',
        tracking=True, default='nee')
    xaa_aa_discount_qty = fields.Float(string='Discount Quantity', tracking=True)
    xaa_aa_quote_template_id = fields.Many2one('sale.order.template',
        string='Choose your quote template', tracking=True)
    xaa_aa_cost_price_total = fields.Float(string='Cost price')

    def formulier_website_quote(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/formulier/quote/'+str(self.id)+'/'+str(self.xaa_aa_pf_access),
            'target': 'self',
        }

    def get_house_info(self):
        house_info = self.env['house.info'].sudo().search([])
        return house_info

    def get_roof_info(self):
        roof_info = self.env['roof.info'].sudo().search([])
        return roof_info

    def get_solar_products(self):
        solar_products = self.env['product.product'].sudo().search([
            ('xaa_aa_is_solar_panel_product', '=' , True)])
        return solar_products

    def online_pf_dictionary(self):
        values = super(ProjectFormulier, self).online_pf_dictionary()
        user = self.env['res.users'].browse(self._context.get('uid'))
        Product = self.env['product.product'].sudo()

        if user.has_group('base.group_user'):
            domain = ['|',('xaa_aa_show_product_user','=','yes'),'|',
                ('xaa_aa_show_product_user','=',False),
                ('xaa_aa_product_portal_user','in', user.id)]
        else:
            domain = ['|',('xaa_aa_product_portal_user','in', user.id),
                ('xaa_aa_show_product_user','=',False)]
        discount_products = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Discount')], order='xaa_aa_priority')
        if not user.xaa_aa_template_id:
            quote_templates = self.env['sale.order.template'].sudo().search([])
        else:
            quote_templates = user.xaa_aa_template_id

        values.update({'quote_templates': quote_templates,
                        'discount_products': discount_products,
                        'user': user,
                        'internal_user': user.has_group('base.group_user')})
        return values

class HouseInfo(models.Model):
    _name = "house.info"
    _description = "Information about House"
    _rec_name = 'xaa_aa_house_type'

    xaa_aa_house_type = fields.Char(string='House type')
    xaa_aa_house_image = fields.Binary(string='Image', attachment=True)
    xaa_aa_is_iso = fields.Boolean(string='It is for ISO')
    xaa_aa_is_pv = fields.Boolean(string='It is for PV')

class HouseRootInfo(models.Model):
    _name = "roof.info"
    _description = "Information about Roof Of House"
    _rec_name = 'xaa_aa_roof_type'

    xaa_aa_roof_type = fields.Char(string='Roof type')
    xaa_aa_roof_image = fields.Binary(string='Roof Image', attachment=True)
