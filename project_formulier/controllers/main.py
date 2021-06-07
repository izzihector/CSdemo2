# -*- coding: utf-8 -*-

from odoo import fields, http, _
from odoo.http import request
import json
import base64


class ProjectFormulier(http.Controller):

    @http.route(['/web/video/<int:video_id>'], type='http', auth="public", website=True)
    def get_video_data(self, video_id, **kw):
        """ video binary data return """

        if video_id:
            order_video = request.env['order.video'].sudo().browse(video_id)
            video = base64.b64decode(order_video.xaa_aa_video)
            return video
        return False

    @http.route(['/project/formulier/submit/<int:xaa_aa_formulier_id>/<string:model_name>'], type='http',
                auth='public', methods=['POST'], website=True)
    def project_formulier_submit(self, xaa_aa_formulier_id, model_name, **kwargs):
        """ Project Formulier web form submit """

        if xaa_aa_formulier_id:
            formulier_id = request.env['question.formulier'].sudo().browse(xaa_aa_formulier_id)
            if formulier_id.xaa_aa_state == 'opportunity':
                formulier_id.xaa_aa_state = 'opportunity_output'
            elif formulier_id.xaa_aa_state == 'quotation':
                formulier_id.xaa_aa_state = 'quotation_output'
            elif formulier_id.xaa_aa_state == 'task':
                formulier_id.xaa_aa_state = 'task_output'
            new_dict = {}
            for key, value in kwargs.items():
                if key in formulier_id._fields:
                    new_dict.update({key:value})
            formulier_id.write(new_dict)
            return json.dumps({'id': formulier_id.id})

    @http.route(['/project-formulier/<int:xaa_aa_formulier_id>/<string:xaa_aa_pf_access>'],
        type='http', auth="public", website=True)
    def project_formulier_page(self, xaa_aa_formulier_id, xaa_aa_pf_access, **kw):
        """ Project Formulier view on web form """

        formulier_id = request.env['question.formulier'].sudo().search(
            [('id','=',xaa_aa_formulier_id),('xaa_aa_pf_access','=',xaa_aa_pf_access)])
        if formulier_id and formulier_id.xaa_aa_partner_id:
            values = formulier_id.sudo().online_pf_dictionary()
            return request.render('project_formulier.main_formulier_template', values)
        else:
            return request.redirect('/my')

    @http.route('/formulier/form/image/upload', auth="user", website=True, type="json", csrf=False)
    def formulier_image_upload_file(self, image, fileName, file_type, formulier_id, is_task):
        """ Project Formulier web form -> extra images directly create new record """

        order_image_id = request.env['order.image'].create({
                                                    'xaa_aa_name': fileName,
                                                    'xaa_aa_image': image,
                                                    'xaa_aa_file_type': file_type or 'application/png',
                                                    'xaa_aa_formulier_id': int(formulier_id),
                                                    'xaa_aa_is_task': is_task,
                                                    })
        return order_image_id.id

    @http.route('/formulier/form/video/upload',auth="user", website=True, type="json", csrf=False)
    def formulier_video_upload_file(self, video, fileName, file_type, formulier_id, is_task):
        """ Project Formulier web form -> extra videos directly create new record """

        order_video_id = request.env['order.video'].create({
                                                    'xaa_aa_name': fileName,
                                                    'xaa_aa_video': video,
                                                    'xaa_aa_file_type': file_type or 'application/mp4',
                                                    'xaa_aa_formulier_id': int(formulier_id),
                                                    'xaa_aa_is_task': is_task,
                                                    })
        return order_video_id.id

    @http.route('/formulier/form/document/upload',auth="user", website=True, type="json", csrf=False)
    def formulier_document_upload_file(self, document, fileName, file_type, formulier_id):
        """ Project Formulier web form -> extra document directly create new record """

        order_document_id = request.env['order.document'].create({
                                                    'xaa_aa_name': fileName,
                                                    'xaa_aa_file': document,
                                                    'xaa_aa_file_type': file_type or 'application/pdf',
                                                    'xaa_aa_formulier_id': int(formulier_id),
                                                    })
        return order_document_id.id,order_document_id.xaa_aa_name

    @http.route(['/sale_order/project_formulier/get'], type='json', auth="public", website=True)
    def get_formulier_images(self, order_id, res_model, **kw):
        """ quotation image tab on quotation preview""" 

        data = {'formulier_id': '', 'data':[], 'image_ids':[], 'document_ids': [], 'video_ids': []}
        if res_model == 'sale.order':
            order_id = request.env['sale.order'].browse(order_id)
            if order_id and order_id.xaa_aa_formulier_id:
                que_id = order_id.xaa_aa_formulier_id
                data.update({'formulier_id': que_id.id, 'data':[]})
                if que_id.xaa_aa_image_ids:
                    data['image_ids'].append(que_id.xaa_aa_image_ids.ids)
                for doc in que_id.xaa_aa_document_ids:
                    data['document_ids'].append([doc.id, doc.xaa_aa_name])
                for video in que_id.xaa_aa_video_ids:
                    data['video_ids'].append([video.id, video.xaa_aa_name])
                formulerModelId = request.env['ir.model'].search([('model', '=', 'question.formulier')])
                fields = request.env['ir.model.fields'].search([('ttype', '=', 'binary'),
                    ('model_id', '=', formulerModelId.id)])
                for field in fields:
                    imageData = request.env['question.formulier'].search_read(
                        [('id', '=', que_id.id)], [field.name])
                    if imageData[0].get(field.name):
                        data['data'].append(field.name)
        if res_model == 'sale.order.template':
            template_id = request.env['sale.order.template'].browse(order_id)
            if template_id:
                for video in template_id.xaa_aa_template_video_ids:
                    data['video_ids'].append([video.id, video.xaa_aa_name])
        return data
