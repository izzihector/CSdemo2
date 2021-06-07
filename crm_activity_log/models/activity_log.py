# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api
from datetime import datetime 


class LogActivity(models.Model):
    _name = 'activity.log'
    _description = 'Describe Activity Log'
    _rec_name = "xaa_aa_name"

    xaa_aa_name = fields.Char(related='xaa_aa_opportunity_id.name', string='Name')
    xaa_aa_opportunity_id = fields.Many2one('crm.lead', string='Opportunity')
    xaa_aa_stage = fields.Char(string="Stage Name")
    xaa_aa_date = fields.Datetime(string="Last Update Date", default=fields.Datetime.now)
    xaa_aa_activity_ids = fields.Many2many('mail.activity.type' , 'log_activity_rel',
        'oppotunity_activity', 'log_activity_id', string='Activities')
    xaa_aa_login_user = fields.Many2one('res.users',  string='Login User')
    xaa_aa_privious_stage = fields.Char(string="Previous Stage")
    xaa_aa_notes = fields.Char(string="Note")

class LeadActivity(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        ''' Create Activity Log Based on Lead/opportunity Create'''

        record = super(LeadActivity, self).create(vals)
        self.env['activity.log'].create({
                'xaa_aa_opportunity_id': record.id,
                'xaa_aa_stage': record.stage_id.name,
                'xaa_aa_date': datetime.today(),
                'xaa_aa_activity_ids': [(6, 0, [activity.activity_type_id.id for activity in self.activity_ids]) ],
                'xaa_aa_login_user': self.env.user.id,
                'xaa_aa_notes' : 'Opportunity Create',
        })
        return record


    def write(self, vals):
        ''' Create Activity Log When Stage change on Lead/Opportunity'''

        if vals.get('stage_id') and self.stage_id:
            stageId = self.env['crm.stage'].browse(vals.get('stage_id'))
            self.env['activity.log'].create({
                'xaa_aa_opportunity_id': self.id,
                'xaa_aa_stage': stageId.name,
                'xaa_aa_date': datetime.today(),
                'xaa_aa_activity_ids': [(6, 0, [activity.activity_type_id.id for activity in self.activity_ids]) ],
                'xaa_aa_login_user': self.env.user.id,
                'xaa_aa_privious_stage': self.stage_id.name,
                'xaa_aa_notes' : 'Stage changed from ' + self.stage_id.name+ ' to ' +stageId.name
            })
        return super(LeadActivity, self).write(vals)
