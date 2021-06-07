# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import fields, http, _
from odoo.http import request

class OpportunityForm(http.Controller):

    @http.route(['/opportunity_form'], type='http', auth='user', website=True)
    def opportunity_details(self, **post):
        countries = request.env['res.country'].sudo().search([])
        Formulier = request.env['question.formulier'].sudo()
        titles = request.env['res.partner.title'].sudo().search([])
        formulier_type = Formulier.fields_get('xaa_aa_formulier_type')['xaa_aa_formulier_type']['selection']
        user = request.env.user
        if user.xaa_aa_formulier_type:
            formulier_type = []
            for user_formulier in user.xaa_aa_formulier_type:
                formulier_type.append((user_formulier.xaa_aa_technical_name,user_formulier.xaa_aa_name))
        values = {
            'titles': titles,
            'countries': countries,
            'user': user,
            'formulier_type': formulier_type
        }
        return request.render('online_opportunity_form.opportunity_template', values)

    @http.route(['/opportunity_form/create'], type='json', auth="user", methods=['POST'], website=True)
    def opportunity_create(self, data, **kw):
        Lead = request.env['crm.lead'].sudo()
        Partner = request.env['res.partner']
        lead_id = Lead.create({
            'name': 'Created from website',
            'title': data['title'] or False,
            'xaa_aa_lead_category': data['xaa_aa_lead_category'] or False,
            'xaa_aa_formulier_type': data['xaa_aa_formulier_type'],
            'xaa_aa_firstname': data['xaa_aa_firstname'],
            'xaa_aa_lastname': data['xaa_aa_lastname'],
            'xaa_aa_informal_salutation': 'best',
            'xaa_aa_formal_salutation': 'dear',
            'street': data['street'],
            'zip': data['zip'],
            'city': data['city'],
            'country_id': data['country'] or False,
            'email_from': data['email'],
            'phone': data['phone'],
            'xaa_aa_lead_lead_source': data['xaa_aa_lead_lead_source'] or False
        })
        lead_id._onchange_par_formal_salutation()
        lead_id._onchange_informal_salutation()
        partner_id = False
        if lead_id.email_from:
            partner_id = Partner.sudo().search([('email', '=', lead_id.email_from)], limit=1).id
        elif lead_id.contact_name:
            partner_id = Partner.sudo().search([('name', 'ilike', '%' + lead_id.contact_name+'%')], limit=1).id
        if partner_id:
            lead_id.partner_id = partner_id
        if not partner_id and (lead_id.partner_name or lead_id.contact_name):
            partner_id = lead_id.handle_partner_assignment()
            if not partner_id:
                if lead_id.email_from:
                    partner_id = Partner.sudo().search([('email', '=', lead_id.email_from)], limit=1).id
                elif lead_id.contact_name:
                    partner_id = Partner.sudo().search([('name', 'ilike', '%' + lead_id.contact_name+'%')], limit=1).id
                if partner_id:
                    lead_id.partner_id = partner_id
        stage_id = request.env.ref('online_opportunity_form.stage_quote_external', False)
        lead_id.convert_opportunity(partner_id)
        if stage_id:
            lead_id.sudo().write({'stage_id': stage_id.id})
        return lead_id.project_formulier_online()
