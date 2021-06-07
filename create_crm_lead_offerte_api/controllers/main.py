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
from odoo.http import request, JsonRequest

_logger = logging.getLogger(__name__)


def __init__(self, *args):
    super(JsonRequest, self).__init__(*args)

    self.params = {}

    args = self.httprequest.args
    request = None
    request_id = args.get('id')

    # regular jsonrpc2
    request = self.httprequest.get_data().decode(self.httprequest.charset)

    # Read POST content or POST Form Data named "request"
    try:
        self.jsonrequest = json.loads(request)
    except ValueError:
        msg = 'Invalid JSON data: %r' % (request,)
        _logger.info('%s: %s', self.httprequest.path, msg)
        raise werkzeug.exceptions.BadRequest(msg)
    if self.httprequest.path == '/create_lead_from_offerte':
        self.params = dict(self.jsonrequest)
    else:
        self.params = dict(self.jsonrequest.get("params", {}))
    self.context = self.params.pop('context', dict(self.session.context))

setattr(JsonRequest,'__init__',__init__)

class LeadSolvari(http.Controller):

    @http.route('/create_lead_from_offerte', type='json', auth='public')
    def create_lead_from_offerte(self, **kwargs):
        token = request.env['ir.config_parameter'].sudo().get_param('create_crm_lead_offerte_api.offerte_token')
        _logger.info("data...........=======================%s",kwargs)
        values = {
            'type': 'lead',
            'name': kwargs.get('name', ''),
            'contact_name': kwargs.get('name', ''),
            'street': kwargs.get('street', '') + ',' + kwargs.get('housenumber', ''),
            'zip': kwargs.get('postcode', ''),
            'phone': kwargs.get('phone', ''),
            'email_from': kwargs.get('email', ''),
            'city': kwargs.get('city', ''),
            'description': kwargs.get('notes', ''),
        }
        try:
            lead_id = request.env['crm.lead'].sudo().create(values)
            lead_id.sudo().message_post(body=_("Offerte.nl json data: %s" % json.dumps(kwargs)))
            _logger.info("lead id======================= %s, %s" %(lead_id, kwargs))
            return json.dumps({'success': True})
        except Exception as e:
            # if anything goes wrong then atleast create lead with json data
            # save in internal note field of lead.
            _logger.info('Offerte.nl lead failed =====%s' %e)
            kwargs.pop('secret', None)
            values = {
                'name': 'Offerte.nl Lead, Please Check Chatter of lead'
            }
            lead_id = request.env['crm.lead'].sudo().create(values)
            lead_id.message_post(_(
                "Offerte.nl json data: %s" % json.dumps(kwargs)))
            return json.dumps({'message': 'Lead Push Failed'})
