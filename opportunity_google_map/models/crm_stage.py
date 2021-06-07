# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields

class CrmStage(models.Model):
    _inherit = 'crm.stage'

    xaa_aa_show_in_google_map = fields.Boolean(string='Show Opportunity in Google Map')
