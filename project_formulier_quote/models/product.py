# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductBrand(models.Model):
    """ product brand """

    _name = "product.brand"
    _description = "Product brand for Optimisers and converter type product"
    _rec_name = 'xaa_aa_name'

    xaa_aa_name = fields.Char('Brand')

class SolarProductType(models.Model):
    """ Solar product type """

    _name = "solar.type"
    _description = "Solar Product type"
    _rec_name = 'xaa_aa_name'

    xaa_aa_name = fields.Char('Solar Type')

class ProductTemplate(models.Model):
    """ add priority field for sorting products, product type field add """

    _inherit = "product.template"

    xaa_aa_priority = fields.Integer(string='Priority')
    xaa_aa_product_type = fields.Selection([('Solar Panel', 'Solar Panel'),
                                    ('Converter', 'Converter'),
                                    ('Optimisers', 'Optimisers'),
                                    ('Discount', 'Discount'),
                                    ('Flat Roof', 'Flat Roof'),
                                    ('Slanted Roof', 'Slanted Roof'),
                                    ('Mix Roof', 'Mix Roof'),
                                    ('Stekkers', 'Stekkers'),
                                    ('Overige Materialen', 'Overige Materialen'),
                                    ('BTW teruggave', 'BTW teruggave')],
                                    string='PF quote type')
    xaa_aa_min_product_range = fields.Float(string='Minimum Range')
    xaa_aa_max_product_range = fields.Float(string='Maximum Range')
    xaa_aa_wq_min_range = fields.Float(string='WQ Minimum Range',
                                help='This range only use for Website Quote')
    xaa_aa_wq_max_range = fields.Float(string='WQ Maximum Range',
                                help='This range only use for Website Quote')
    xaa_aa_solar_type = fields.Many2many('solar.type', string='Solar type')
    xaa_aa_product_brand = fields.Many2one('product.brand', string='Brand')
    xaa_aa_is_solar_panel_product = fields.Boolean(string='Solar Pannel Product?')
    xaa_aa_show_product_user = fields.Selection([('yes', 'yes'),
                                            ('no', 'no')],
                                            string='Show to all users')
    xaa_aa_product_portal_user = fields.Many2many('res.users', string='Show only to specific user')

    #product name tab fields
    xaa_aa_wq_header_1 = fields.Char('Header one')
    xaa_aa_wq_header_2 = fields.Char('Header two')
    xaa_aa_wq_line1 = fields.Char('Line one')
    xaa_aa_wq_line2 = fields.Char('Line two')
    xaa_aa_wq_line3 = fields.Char('Line three')
    xaa_aa_wq_line4 = fields.Char('Line four')
    xaa_aa_wq_image = fields.Binary('Image')

    @api.model
    def create(self, vals):
        if not vals.get('xaa_aa_wq_header_1'):
            vals.update({'xaa_aa_wq_header_1': vals.get('name')})
        if not vals.get('xaa_aa_wq_image'):
            vals.update({'xaa_aa_wq_image': vals.get('image')})
        return super(ProductTemplate, self).create(vals)

