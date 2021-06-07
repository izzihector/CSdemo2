# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import http
from odoo.http import request
from datetime import datetime
from dateutil.relativedelta import relativedelta

class CrmLead(http.Controller):

    @http.route(['/crm/stage/<int:lead_id>/<string:stage>'],
                type='http', auth="public", website=True)
    def ChangeCrmStage(self, lead_id, stage, **kw):
        """ this controller change stage of lead   """
        if lead_id:
            lead = request.env['crm.lead'].sudo().browse(lead_id)
            stage_id = False
            if stage == 'future':
                stage_id = request.env['crm.stage'].sudo().search([('name','in',['Toekomst [18]', 'Future [18]'])], limit=1)
            elif stage == 'review':
                stage_id = request.env['crm.stage'].sudo().search([('name','in',['Beoordelen [3]','Rate [3]'])], limit=1)
            elif stage == 'complaints':
                stage_id = request.env['crm.stage'].sudo().search([('name','ilike','Reclameren')], limit=1)
            elif stage == 'pf_website_quote_sent':
                stage_id = request.env.ref('project_formulier_quote.stage_website_quote_questions', False)
                if stage_id:
                    lead.stage_id = stage_id.id
                    if lead.xaa_aa_formulier_id:
                        return request.redirect('/formulier/quote/'+str(lead.xaa_aa_formulier_id.id)+'/'+str(lead.xaa_aa_formulier_id.xaa_aa_pf_access))
            elif stage == 'pf_question_complated':
                stage_id = request.env.ref('project_formulier_quote.stage_website_quote_questions',False)
                if stage_id:
                    lead.stage_id = stage_id.id
                    if lead.xaa_aa_formulier_id:
                        return request.redirect('/formulier/quote/'+str(lead.xaa_aa_formulier_id.id)+'/'+str(lead.xaa_aa_formulier_id.xaa_aa_pf_access))
            if stage_id:
                lead.stage_id = stage_id.id
        return request.render('crm_mail_template.customer_lead_template', {})

    @http.route(['/crm/lead/<int:lead_id>/<string:duration>'],
                type='http', auth="public", website=True)
    def ChangeCrm(self,lead_id,duration,**kw):
        """ this controller get value from mail template and set lead value as per click on button on mail template  """

        current_date = datetime.now()
        if lead_id:
            lead = request.env['crm.lead'].sudo().browse(lead_id)
            stage_id = request.env['crm.stage'].sudo().search([('name','in',['Toekomst [18]','Future [18]'])], limit=1)
            action_date = False
            if duration == 'three':
                action_date = current_date + relativedelta(months=3)
            elif duration == 'lost':
                lead.sudo().action_set_lost()
                return request.render('project_formulier_quote.close_lead_template', {})
            if action_date:
                if stage_id:
                    lead.stage_id = stage_id.id
                lead.date_action = action_date
            return request.render('crm_mail_template.customer_lead_template', {})
