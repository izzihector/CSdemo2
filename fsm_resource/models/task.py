# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields, api


class Task(models.Model):
    _inherit = 'project.task'

    user_id = fields.Many2one(string='Assigned Leader')

    @api.model
    def create(self, values):
        """Sync Start Date, End Date with Planning Dates of task."""
        update_values = {}
        if 'date_start' in values:
            update_values['planned_date_begin'] = values.get('date_start', False)
        if 'date_end' in values:
            update_values['planned_date_end'] = values.get('date_end', False)
        values.update(update_values)
        return super(Task, self).create(values)

    def write(self, values):
        """Sync Start Date, End Date with Planning Dates of task."""
        update_values = {}
        if 'date_start' in values:
            update_values['planned_date_begin'] = values.get('date_start', False)
        if 'date_end' in values:
            update_values['planned_date_end'] = values.get('date_end', False)
        values.update(update_values)
        return super(Task, self).write(values)

    @api.onchange('date_start')
    def change_date_end(self):
        """When user change Start Date only if End Date is before Start Date
        this method will set 17:00 of same day for End Date.
        """
        for record in self:
            if (record.date_end and record.date_start) and record.date_end < record.date_start:
                record.date_end = self.clientSeventeen(record.date_start.date())
