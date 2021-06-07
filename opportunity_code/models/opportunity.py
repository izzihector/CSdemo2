# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    xaa_aa_code = fields.Char(string='Opportunity Number', 
        required=True, default="/", readonly=True)

    _sql_constraints = [
        ('opportunity_unique_code', 'UNIQUE (xaa_aa_code)',
         _('The code must be unique!')),
    ]

    @api.model
    def create(self, vals):
        """ Create Sequence while lead/opportunity create"""
        if vals.get('xaa_aa_code', '/') == '/':
            vals['xaa_aa_code'] = self.env['ir.sequence'].next_by_code('crm.lead')
        return super(CrmLead, self).create(vals)

    def copy(self, default=None):
        """ Create Sequence while lead/opportunity duplicate"""
        if default is None:
            default = {}
        default['xaa_aa_code'] = self.env['ir.sequence'].next_by_code('crm.lead')
        return super(CrmLead, self).copy(default)
