# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'


    xaa_aa_message_by_offerte = fields.Text(string='Message By Offerte')
    xaa_aa_spoken_by_offerte = fields.Boolean(string='Spoken By Offerte')
    xaa_aa_competitors_offerte = fields.Integer(string='Competitors')
    xaa_aa_offerte_product_id = fields.Integer(string='Product Id',
        help='Prduct in Offerte Lead')
    xaa_aa_offerte_product_title = fields.Text(string='Product Title',
        help='Prduct in Offerte Lead')
    xaa_aa_offerte_question = fields.Text(string='Offerte Lead Question')
    xaa_aa_offerte_ans = fields.Text(string='Offerte Lead Ans')
