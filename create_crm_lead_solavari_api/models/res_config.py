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

    xaa_aa_solvari_token = fields.Char(
        string='Solvari Token',
        config_parameter='create_crm_lead_solavari_api.solvari_token',
        readonly=False)
