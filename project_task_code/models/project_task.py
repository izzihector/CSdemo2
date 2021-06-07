# -*- coding: utf-8 -*-
# Copyright 2016 Tecnativa <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _

class ProjectTask(models.Model):
    _inherit = 'project.task'

    xaa_aa_code = fields.Char(
        string='Task Number', required=True, default="/", readonly=True)

    _sql_constraints = [
        ('project_task_unique_code', 'UNIQUE (xaa_aa_code)',
         _('The code must be unique!')),
    ]

    @api.model
    def create(self, vals):
        if vals.get('xaa_aa_code', '/') == '/':
            vals['xaa_aa_code'] = self.env['ir.sequence'].next_by_code('project.task')
        return super(ProjectTask, self).create(vals)

    def copy(self, default=None):
        if default is None:
            default = {}
        default['xaa_aa_code'] = self.env['ir.sequence'].next_by_code('project.task')
        return super(ProjectTask, self).copy(default)
