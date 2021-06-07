# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _


class ProjectFormulier(models.Model):
    _inherit = 'question.formulier'

    xaa_aa_code = fields.Char(
        string='Formulier Number', required=True, default="/", readonly=True)

    _sql_constraints = [
        ('project_formulier_unique_code', 'UNIQUE (xaa_aa_code)',
         _('The code must be unique!')),
    ]

    @api.model
    def create(self, vals):
        if vals.get('xaa_aa_code', '/') == '/':
            vals['xaa_aa_code'] = self.env['ir.sequence'].next_by_code('question.formulier')
        return super(ProjectFormulier, self).create(vals)

    def copy(self, default=None):
        if default is None:
            default = {}
        default['xaa_aa_code'] = self.env['ir.sequence'].next_by_code('question.formulier')
        return super(ProjectFormulier, self).copy(default)
