# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def cron_geo_localize(self):
        partners = self.env['res.partner'].search([])
        for partner in partners:
            partner.geo_localize()

    @api.model_create_multi
    def create(self, vals_list):
        results = super(ResPartner, self).create(vals_list)
        prov_id = self.env['ir.config_parameter'].sudo().get_param('base_geolocalize.geo_provider')
        if prov_id:
            for res in results:
                res.geo_localize()
        return results

    def write(self, vals):
        res = super(ResPartner, self).write(vals)
        if 'street' in vals.keys() or 'zip' in vals.keys() or 'city' in vals.keys():
            prov_id = self.env['ir.config_parameter'].sudo().get_param('base_geolocalize.geo_provider')
            if prov_id:
                self.geo_localize()
        return res