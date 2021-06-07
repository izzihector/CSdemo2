# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    xaa_aa_offerte_token = fields.Char(
        string='Offerte Token',
        config_parameter='create_crm_lead_offerte_api.offerte_token',
        readonly=False)
