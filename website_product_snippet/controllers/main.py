# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import fields, http, _
from odoo.http import request

class ProductSnippet(http.Controller):
    @http.route(['/product/snippet/dynamic_value'], type='json', auth="public", website=True, csrf=False)
    def get_productsnippet_dynamic_value(self, product_id):
        product = request.env['product.template'].sudo().browse(product_id)
        data = {}
        if product:
            data.update({
                'product_id': product.id,
                # 'aa_wb_logo': product.aa_wb_logo,
                # 'aa_wb_product_image': product.aa_wb_product_image,
                # 'aa_wb_title': product.aa_wb_title,
                # 'aa_wb_text': product.aa_wb_text,
                'aa_sp_logo': product.aa_sp_logo,
                'aa_sp_name': product.name,
                'aa_sp_product_image': product.aa_sp_product_image,
                'aa_point1_icon': product.aa_point1_icon,
                'aa_point1_title': product.aa_point1_title,
                'aa_point1_desc': product.aa_point1_desc,
                'aa_point2_icon': product.aa_point2_icon,
                'aa_point2_title': product.aa_point2_title,
                'aa_point2_desc': product.aa_point2_desc,
                'aa_point3_icon': product.aa_point3_icon,
                'aa_point3_title': product.aa_point3_title,
                'aa_point3_desc': product.aa_point3_desc,
                'aa_point4_icon': product.aa_point4_icon,
                'aa_point4_title': product.aa_point4_title,
                'aa_point4_desc': product.aa_point4_desc,
                'aa_point5_icon': product.aa_point5_icon,
                'aa_point5_title': product.aa_point5_title,
                'aa_point5_desc': product.aa_point5_desc
            })
            return data
        else:
            data.update({'product_id': False})
            return data
