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


    xaa_aa_message_by_solvari = fields.Text(string='Message By Solvari')
    xaa_aa_spoken_by_solvari = fields.Boolean(string='Spoken By Solvari')
    xaa_aa_competitors = fields.Integer(string='Competitors')
    xaa_aa_solvari_product_id = fields.Integer(string='Product Id',
        help='Prduct in Solvari Lead')
    xaa_aa_solvari_product_title = fields.Text(string='Product Title',
        help='Prduct in Solvari Lead')
    xaa_aa_solvari_question = fields.Text(string='Solvari Lead Question')
    xaa_aa_solvari_ans = fields.Text(string='Solvari Lead Ans')
