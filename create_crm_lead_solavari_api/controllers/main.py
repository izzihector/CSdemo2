# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

import json
import logging
from odoo import http, _
from odoo.http import request

_logger = logging.getLogger(__name__)


class LeadSolvari(http.Controller):

    @http.route('/create_lead_from_solvari', type='http', auth="public")
    def create_lead_from_solvari(self, **kwargs):
        token = request.env['ir.config_parameter'].sudo().get_param('create_crm_lead_solavari_api.solvari_token')
        title_obj = request.env['res.partner.title'].sudo()
        source_obj = request.env['lead.source'].sudo()
        categ_obj = request.env['lead.category'].sudo()
        mail_lead_categ = request.env['lead.email.lead.category'].sudo()
        title = False
        country_id = False
        tag_ids = []
        if token and kwargs.get('secret') and (token == kwargs['secret']):
            if kwargs.get('gender') == 'M':
                title = title_obj.search([('name', '=ilike', _('Heer'))], limit=1)
            elif kwargs.get('gender') == 'F':
                title = title_obj.search([('name', '=ilike', _('Mevrouw'))], limit=1)
            lead_source = source_obj.search([('xaa_aa_name', '=ilike', 'Solvari')], limit=1)
            lead_category = categ_obj.search([('xaa_aa_name', '=ilike', 'PV')], limit=1)
            if lead_category:
                tag_ids = lead_category.xaa_aa_tag_ids.ids
            country_id = request.env['res.country'].sudo().search([
                ('code', '=ilike', kwargs.get('country'))])
            kwargs.pop('secret', None)
            values = {
                'type': 'lead',
                'title': title and title.id or False,
                'xaa_aa_lead_lead_source': lead_source and lead_source.id or False,
                'xaa_aa_lead_category': lead_category and lead_category.id or False,
                'tag_ids': tag_ids,
                'name': kwargs.get('description', ''),
                'xaa_aa_firstname': kwargs.get('first_name', ''),
                'xaa_aa_lastname': kwargs.get('last_name', ''),
                'contact_name': kwargs.get('first_name', '') + kwargs.get('last_name', ''),
                'street': kwargs.get('street', '') + ',' + kwargs.get('house_nr', ''),
                'zip': kwargs.get('zip_code', ''),
                'city': kwargs.get('city', ''),
                'partner_latitude': (kwargs.get('location[lat]') or
                                   0.00000),
                'partner_longitude': (kwargs.get('location[lng]') or
                                   0.00000),
                'phone': kwargs.get('phone', ''),
                'email_from': kwargs.get('email', ''),
                'xaa_aa_message_by_solvari': kwargs.get('message_by_solvari', ''),
                'xaa_aa_spoken_by_solvari': kwargs.get('spoken_by_solvari', False),
                'xaa_aa_competitors': kwargs.get('competitors', 0),
                'xaa_aa_solvari_product_title': kwargs.get('products[0][title]'),
                'xaa_aa_solvari_product_id': kwargs.get('products[0][id]'),
                'country_id': country_id and country_id.id or False
            }
            try:
                lead_id = request.env['crm.lead'].sudo().create(values)
                partner_id = request.env['res.partner'].sudo().search([('name','ilike','Api-user')],limit=1)
                if partner_id:
                    lead_id.message_subscribe(partner_id.ids)
                lead_id.sudo().message_post(body=_("solvari json data: %s" % json.dumps(kwargs)))
                _logger.info("lead id======================= %s, %s" %(lead_id, kwargs))
                return json.dumps({'success': True})
            except Exception as e:
                # if anything goes wrong then atleast create lead with json data
                # save in internal note field of lead.
                _logger.info('solvari lead failed =====%s' %e)
                kwargs.pop('secret', None)
                values = {
                    'name': 'Solvari Lead, Please Check Chatter of lead'
                }
                lead_id = request.env['crm.lead'].sudo().create(values)
                lead_id.message_post(_(
                    "solvari json data: %s" % json.dumps(kwargs)))
                return json.dumps({'message': 'Lead Push Failed'})
        else:
            return json.dumps({'Message': 'Invalid Token'})
        