# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields, api

class crmLead(models.Model):
    _inherit = 'crm.lead'

    xaa_aa_contact_address_complete = fields.Char(
        related='partner_id.contact_address_complete')
    xaa_aa_in_valid_stage = fields.Boolean(compute='_get_in_valid_stage', string='In Valid Stage',store=True)
    xaa_aa_lead_marker_color = fields.Selection([
        ('green', 'Green'),
        ('black', 'Black'),
        ('blue', 'Blue'),
        ('brown', 'Brown'),
        ('cyan', 'Cyan'),
        ('grey', 'Grey'),
        ('lightgreen', 'Light-Green'),
        ('magenta', 'Magenta'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('red', 'Red'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
    ], string='Lead Marker Color', related='xaa_aa_lead_category.xaa_aa_marker_color')

    @api.depends('stage_id','stage_id.xaa_aa_show_in_google_map')
    def _get_in_valid_stage(self):
        CrmStageObj = self.env['crm.stage']
        stage_ids = CrmStageObj.search([('xaa_aa_show_in_google_map','=',True)])
        for opp in self:
            if opp.stage_id.id in stage_ids.ids:
                opp.xaa_aa_in_valid_stage = True
            else:
                opp.xaa_aa_in_valid_stage = False

