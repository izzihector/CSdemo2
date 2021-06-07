# -*- coding: utf-8 -*-

from odoo import fields, http, _
from odoo.http import request
from odoo.addons.project_formulier.controllers.main import ProjectFormulier


class ProjectFormulier(ProjectFormulier):

    @http.route(['/project/formulier/submit/<int:xaa_aa_formulier_id>/<string:model_name>'], type='http',
                auth='public', methods=['POST'], website=True)
    def project_formulier_submit(self, xaa_aa_formulier_id, model_name, **kwargs):
        """ Project Formulier web form submit """

        if xaa_aa_formulier_id:
            formulier_id = request.env['question.formulier'].browse(xaa_aa_formulier_id)
            if kwargs.get('xaa_aa_foundation_name'):
                for foundation_img in formulier_id.xaa_aa_foundation_construction_ids:
                    if foundation_img.id == int(kwargs.get('xaa_aa_foundation_name')):
                        foundation_img.xaa_aa_is_selected = True
                    else:
                        foundation_img.xaa_aa_is_selected = False
            xaa_aa_formulier_id = formulier_id.id

        return super(ProjectFormulier, self).project_formulier_submit(xaa_aa_formulier_id,model_name,**kwargs)

    @http.route(['/order/snippet/dynamic_value'], type='json', auth="public", website=True, csrf=False)
    def get_snippet_dynamic_value(self, sale_id):
        order = request.env['sale.order'].sudo().browse(sale_id)
        my_dict = {}
        data = {}
        if order and order.xaa_aa_formulier_id:
            formulier_id = order.xaa_aa_formulier_id
            data.update({'formulier_id': formulier_id.id,
                        'xaa_aa_image': formulier_id.xaa_aa_image or False,
                        'quot_name': formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.user_id.name or 'Dhr Ferry Nieuwboer',
                        'customer_city': formulier_id.xaa_aa_partner_id.city,
                        'customer_street': formulier_id.xaa_aa_partner_id.street,
                        'quote_date': formulier_id.xaa_aa_date_opportunity,
                        'quote_soort': formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.xaa_aa_soort,
                        'quotation_template_id': order.sale_order_template_id and order.sale_order_template_id.id,
                        'pdf_name': order.sale_order_template_id and order.sale_order_template_id.xaa_aa_file_name_pdf,
                        })
            if formulier_id.xaa_aa_formulier_type == 'formulier_one':
                for foundation_construction_id in formulier_id.xaa_aa_foundation_construction_ids:
                    if foundation_construction_id.xaa_aa_is_selected == True:
                        my_dict['foundation_construction_name'] = foundation_construction_id.xaa_aa_name
                        my_dict['foundation_construction_image']= foundation_construction_id.xaa_aa_image
                data.update({
                        'xaa_aa_plattegrond_img': formulier_id.xaa_aa_plattegrond_img or False,
                        'xaa_aa_fundering_img': formulier_id.xaa_aa_fundering_img or False,
                        'xaa_aa_blueprint_img': formulier_id.xaa_aa_blueprint_img or False,
                        'xaa_aa_lot_img': formulier_id.xaa_aa_lot_img or False,
                        'xaa_aa_extra_drawing_1_img': formulier_id.xaa_aa_extra_drawing_1_img or False,
                        'xaa_aa_extra_drawing_2_img': formulier_id.xaa_aa_extra_drawing_2_img or False,
                        'xaa_aa_image_1': formulier_id.xaa_aa_image_1 or False,
                        'xaa_aa_image_2': formulier_id.xaa_aa_image_2 or False,
                        'xaa_aa_image_3': formulier_id.xaa_aa_image_3 or False,
                        'xaa_aa_image_4': formulier_id.xaa_aa_image_4 or False,
                        'xaa_aa_image_5': formulier_id.xaa_aa_image_5 or False,
                        'xaa_aa_image_6': formulier_id.xaa_aa_image_6 or False,
                        'xaa_aa_image_7': formulier_id.xaa_aa_image_7 or False,
                        'xaa_aa_image_8': formulier_id.xaa_aa_image_8 or False,
                        'xaa_aa_house_info': formulier_id.xaa_aa_house_info,
                        'xaa_aa_analysis_settlement': formulier_id.xaa_aa_analysis_settlement,
                        'xaa_aa_floor_construction': formulier_id.xaa_aa_floor_construction or '',
                        'leads': formulier_id.xaa_aa_leads or '',
                        'xaa_aa_goal_owner': formulier_id.xaa_aa_goal_owner,
                        'xaa_aa_faced_construction': formulier_id.xaa_aa_faced_construction or '',
                        'xaa_aa_floor_construction_verd': formulier_id.xaa_aa_floor_construction_verd or '',
                        'xaa_aa_inspection_foundation_depth': formulier_id.xaa_aa_inspection_foundation_depth,
                        'xaa_aa_possible_settings': formulier_id.xaa_aa_possible_settings,
                        'xaa_aa_action_resident': formulier_id.xaa_aa_action_resident,
                        'xaa_aa_location_pipping_ground': formulier_id.xaa_aa_location_pipping_ground,
                        'xaa_aa_action_total_wall': formulier_id.xaa_aa_action_total_wall,
                        'xaa_aa_parkeren': formulier_id.xaa_aa_parkeren,
                        'xaa_aa_toegang': formulier_id.xaa_aa_toegang,
                        'xaa_aa_tuin': formulier_id.xaa_aa_tuin,
                        'xaa_aa_bomen': formulier_id.xaa_aa_bomen,
                        'xaa_aa_kraan': formulier_id.xaa_aa_kraan,
                        'xaa_aa_grondwerk': formulier_id.xaa_aa_grondwerk,
                        'xaa_aa_aanvullend': formulier_id.xaa_aa_aanvullend,
                        'xaa_aa_faced_construction': formulier_id.xaa_aa_faced_construction or '',
                        'xaa_aa_floor_construction_verd_2': formulier_id.xaa_aa_floor_construction_verd_2 or '',
                        'xaa_aa_dakbouw': formulier_id.xaa_aa_dakbouw or '',
                        'foundation_construction_name': my_dict.get("foundation_construction_name"),
                        'foundation_construction_image': my_dict.get("foundation_construction_image"),
                    })
            return data
        else:
            data.update({'formulier_id': False,})
            return data
