# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class MailActivityPopup(models.TransientModel):
    _name = 'sh.mail.activity'
    _description = 'SH Mail Activity'

    @api.model
    def default_company_id(self):
        return self.env.company

    sh_activity_type_id = fields.Many2one(
        'mail.activity.type', string='Activity Type', required=True)
    sh_summary = fields.Char(string='Summary')
    sh_date_deadline = fields.Date('Due Date', required=True, default=lambda self: fields.Date.today())
    sh_user_id = fields.Many2one(
        'res.users', string='Assigned to', required=True, default=lambda self: self.env.user.id)
    sh_note = fields.Html('Note')
    sh_supervisor_id = fields.Many2one(
        'res.users', string='Supervisor', default=lambda self: self.env.user.id)
    sh_user_ids = fields.Many2many('res.users', string="Assign Multi Users")
    sh_display_multi_user = fields.Boolean(compute='_compute_sh_display_multi_user')
    company_id = fields.Many2one('res.company',string='Company',default=default_company_id)
    sh_create_individual_activity = fields.Boolean('Individual activities for multi users ?')

    @api.depends('company_id')
    def _compute_sh_display_multi_user(self):
        if self:
            for rec in self:
                rec.sh_display_multi_user = False
                if rec.company_id and rec.company_id.sh_display_multi_user:
                    rec.sh_display_multi_user = True

    def action_schedule_activity(self):
        if self.env.context.get('active_ids'):
            model_id = self.env['ir.model'].sudo().search(
                [('model', '=', self.env.context.get('active_model'))], limit=1)
            for partner in self.env.context.get('active_ids'):
                self.env['mail.activity'].sudo().create({
                        'res_model_id': model_id.id,
                        'res_id': partner,
                        'user_id': self.sh_user_id.id,
                        'date_deadline': self.sh_date_deadline,
                        'sh_user_ids':[(6,0,self.sh_user_ids.ids)],
                        'supervisor_id':self.sh_supervisor_id.id,
                        'activity_type_id': self.sh_activity_type_id.id,
                        'summary': self.sh_summary,
                        'res_model': self.env.context.get('active_model'),
                        'note': self.sh_note,
                })
                if self.sh_user_ids and self.sh_create_individual_activity:
                    for user in self.sh_user_ids:
                        if self.sh_user_id.id != user.id:
                            self.env['mail.activity'].sudo().create({
                                'res_model_id': model_id.id,
                                'res_id': partner,
                                'user_id': self.sh_user_id.id,
                                'date_deadline': self.sh_date_deadline,
                                'sh_user_ids':[(6,0,user.ids)],
                                'supervisor_id':self.sh_supervisor_id.id,
                                'activity_type_id': self.sh_activity_type_id.id,
                                'summary': self.sh_summary,
                                'res_model': self.env.context.get('active_model'),
                                'note': self.sh_note,
                            })
