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
try:
    import pyPostcode
except ImportError as err:  # pragma: no cover
    _logger.debug(err)


class CustomerProjectFormulier(http.Controller):

    @http.route(['/create_new_lead'], type='json',
                auth="public", methods=['POST'], website=True)
    def create_new_lead(self, data, **kw):

        Lead = request.env['crm.lead'].sudo()
        Partner = request.env['res.partner']
        SourceObj = request.env['lead.source'].sudo()
        CategObj = request.env['lead.category'].sudo()
        lead_source = SourceObj.search([('xaa_aa_name', '=ilike', 'Solvari')], limit=1)
        lead_category = CategObj.search([('xaa_aa_name', '=ilike', 'PV')], limit=1)

        partner_id = Partner.sudo().search([('email', '=ilike', data['filled_email'])], limit=1)
        lead_id = Lead.create({
            'name': 'Created from website',
            'partner_id': partner_id.id or False,
            'xaa_aa_formulier_type': 'formulier_four',
            'xaa_aa_lead_category': lead_source and lead_source.id or False,
            'xaa_aa_lead_lead_source': lead_category and lead_category.id or False
        })
        lead_id._onchange_par_formal_salutation()
        lead_id._onchange_informal_salutation()
        lead_id.convert_opportunity(partner_id.id)
        return lead_id.project_formulier_online()

    @http.route(['/update_contact_data'], type='json',
                auth="public", methods=['POST'], website=True)
    def update_contact_data(self, data, **kw):

        Partner = request.env['res.partner']
        partner_id = Partner.sudo().search([('email', '=ilike', data['filled_email'])], limit=1)
        if partner_id:
            partner_id.write({
                'xaa_aa_lastname': data['last_name'].capitalize(),
                'xaa_aa_firstname': data['first_name'].capitalize(),
                'phone': data['phone'],
                'zip': data['zip'].upper(),
                'title': data['title'] or False,
                'city': data['city'],
                'street_name': data['street_name'],
                'street_number': data['street_number'],
                'street_number2': data['street_number2'],
                })
        else:
            Partner.create({
                'name': data['first_name'].capitalize()+' '+data['last_name'].capitalize(),
                'xaa_aa_lastname': data['last_name'].capitalize(),
                'xaa_aa_firstname': data['first_name'].capitalize(),
                'email': data['filled_email'].lower(),
                'phone': data['phone'],
                'zip': data['zip'].upper(),
                'title': data['title'] or False,
                'city': data['city'],
                'street_name': data['street_name'],
                'street_number': data['street_number'],
                'street_number2': data['street_number2'],
                })
        return True

    @http.route(['/update_contact_product_data'], type='json',
                auth="public", methods=['POST'], website=True)
    def update_contact_product_data(self, data, **kw):

        Partner = request.env['res.partner'].sudo()
        FormulierType = request.env['formulier.type'].sudo()
        formulier_type = FormulierType
        FormulierTypeOption = request.env['partner.formulier.type.option'].sudo()
        FormulierTypeInstall = request.env['partner.formulier.type.install'].sudo()
        partner_id = Partner.search([('email', '=ilike', data['filled_email'])], limit=1)
        for option in partner_id.xaa_aa_formulier_type_option:
            option.unlink()
        for install in partner_id.xaa_aa_formulier_type_install:
            install.unlink()
        partner_id.xaa_aa_formulier_type = data.get('formulier_type')

        for k in data.get('type_option'):
            formulier_type = FormulierType.search([('xaa_aa_name', 'ilike', k)],limit=1)
            if formulier_type and formulier_type.id in data.get('formulier_type'):
                option_id = FormulierTypeOption.create({
                    'xaa_aa_partner_id': partner_id.id,
                    'xaa_aa_formulier_type': formulier_type.id,
                    'xaa_aa_formulier_type_option': data['type_option'][k],
                    })
        for k in data.get('type_install'):
            formulier_type = FormulierType.search([('xaa_aa_name', 'ilike', k)],limit=1)
            if formulier_type and formulier_type.id in data.get('formulier_type'):
                for j in data['type_install'][k]:
                    install_id = FormulierTypeInstall.create({
                        'xaa_aa_partner_id': partner_id.id,
                        'xaa_aa_formulier_type': formulier_type.id,
                        'xaa_aa_formulier_type_install': j,
                        })
        return True

    @http.route('/customer_opportunity_form', type="http", auth="public", website=True)
    def patient_webform(self, **kw):
        titles = request.env['res.partner.title'].sudo().search([])
        data = {
            'titles': titles,
        }
        return http.request.render('customer_project_formulier.customer_opportunity_form', data)


    @http.route(['/search_customer'], type='json',
                auth="public", methods=['POST'], website=True)
    def search_customer(self, email, **kw):

        data = {}
        partner_id = request.env['res.partner'].sudo().search([('email', '=ilike', email)], limit=1)
        if partner_id:
            data.update({
                'name': partner_id.name,
                'last_name': partner_id.xaa_aa_lastname,
                'first_name': partner_id.xaa_aa_firstname,
                'phone': partner_id.phone,
                'zip': partner_id.zip,
                'title': partner_id.title and partner_id.title.id or False,
                'zip': partner_id.zip,
                'city': partner_id.city,
                'street_name': partner_id.street_name,
                'street_number': partner_id.street_number,
                'street_number2': partner_id.street_number2,
                'formulier_type': False,
                'type_option': {},
                'type_install': {},
                })
            if partner_id.xaa_aa_formulier_type:
                data.update({'formulier_type':partner_id.xaa_aa_formulier_type.ids})
            for f_option in partner_id.xaa_aa_formulier_type_option:
                data['type_option'].update({f_option.xaa_aa_formulier_type.xaa_aa_name: f_option.xaa_aa_formulier_type_option.id})
            for f_install in partner_id.xaa_aa_formulier_type_install:
                if f_install.xaa_aa_formulier_type.xaa_aa_name in data['type_install'].keys():
                    data['type_install'][f_install.xaa_aa_formulier_type.xaa_aa_name].append(f_install.xaa_aa_formulier_type_install.id)
                else:
                    data['type_install'].update({f_install.xaa_aa_formulier_type.xaa_aa_name: [f_install.xaa_aa_formulier_type_install.id]})
        return data


    @http.route(['/get_address'], type='json',
                auth="public", methods=['POST'], website=True)
    def get_address(self, house_number, postcode, **kw):

        data = {}
        apikey = request.env['ir.config_parameter'].sudo().get_param(
            'l10n_nl_postcodeapi.apikey', '').strip()
        if not apikey or apikey == 'Your API key':
            return {}
        provider_obj = pyPostcode.Api(apikey, (3, 0, 0))

        if not provider_obj:
            return {}
        pc_info = provider_obj.getaddress(postcode, house_number)
        if not pc_info or not pc_info._data:
            return {}
        data.update({
            'street_name': pc_info.street,
            'city': pc_info.city,
            })
        return data