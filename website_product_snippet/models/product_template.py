# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # aa_wb_logo = fields.Binary('Logo')
    # aa_wb_product_image = fields.Binary('Product Image')
    # aa_wb_title = fields.Char('Title')
    # aa_wb_text = fields.Text('Product Description')

    #Solar Panel Snippet
    aa_sp_logo = fields.Binary('Logo ')
    aa_sp_product_image = fields.Binary('Item Picture')
    aa_point1_icon = fields.Binary('Point 1 Icon')
    aa_point1_title = fields.Char('Point 1 Title')
    aa_point1_desc = fields.Text('Point 1 Description')
    aa_point2_icon = fields.Binary('Point 2 Icon')
    aa_point2_title = fields.Char('Point 2 Title')
    aa_point2_desc = fields.Text('Point 2 Description')
    aa_point3_icon = fields.Binary('Point 3 Icon')
    aa_point3_title = fields.Char('Point 3 Title')
    aa_point3_desc = fields.Text('Point 3 Description')
    aa_point4_icon = fields.Binary('Point 4 Icon')
    aa_point4_title = fields.Char('Point 4 Title')
    aa_point4_desc = fields.Text('Point 4 Description')
    aa_point5_icon = fields.Binary('Point 5 Icon')
    aa_point5_title = fields.Char('Point 5 Title')
    aa_point5_desc = fields.Text('Point 5 Description')
