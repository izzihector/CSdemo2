# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _
from odoo.http import request


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    xaa_aa_sale_alias = fields.Many2one('mail.alias', 'Alias', readonly=True)
    xaa_aa_attachment_ids = fields.One2many('ir.attachment', 'xaa_aa_order_id', string='Attachments')

    @api.model
    def create(self, vals):
        res = super(SaleOrder,self).create(vals)
        MailAlias = self.env['mail.alias'].sudo()
        ir_model = self.env['ir.model'].search([('model','=','sale.order')])
        alias_id = MailAlias.create({
                    'alias_name':res.name,
                    'alias_model_id' : ir_model.id,
                    'alias_defaults' : {'xaa_aa_order_id' : res.id},
                    })
        res.xaa_aa_sale_alias = alias_id.id
        return res

    @api.model
    def message_new(self, msg, custom_values=None):
        if custom_values is None:
            custom_values = {}
        order = custom_values.get('xaa_aa_order_id')
        if order:
            order_id = self.env['sale.order'].browse(order)
            return order_id
        else:
            return super(SaleOrder, self).message_new(msg, custom_values=custom_values)

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, subtype_id=None, **kwargs):
        self.ensure_one()
        if kwargs.get('message_type') == 'email':
            subtype_id = request.env.ref('mail.mt_note').id
        return super(SaleOrder, self).message_post(subtype_id=subtype_id, **kwargs)


class Task(models.Model):
    _inherit = 'project.task'

    xaa_aa_task_alias = fields.Many2one('mail.alias', 'Alias', readonly=True)
    xaa_aa_attachment_ids = fields.One2many('ir.attachment', 'xaa_aa_task_id', string='Attachments')

    @api.model
    def create(self, vals):
        res = super(Task, self).create(vals)
        MailAlias = self.env['mail.alias'].sudo()
        ir_model = self.env['ir.model'].search([('model','=','project.task')])
        alias_id = MailAlias.create({
                    'alias_name':res.xaa_aa_code,
                    'alias_model_id' : ir_model.id,
                    'alias_defaults' : {'xaa_aa_task_id' : res.id},
                    'alias_user_id': res.user_id.id
                    })
        res.xaa_aa_task_alias = alias_id.id
        return res

    @api.model
    def message_new(self, msg, custom_values=None):
        if custom_values is None:
            custom_values = {}
        task = custom_values.get('xaa_aa_task_id', None)
        if task:
            task_id = self.browse(task)
            return task_id
        else:
            return super(Task, self).message_new(msg, custom_values=custom_values)

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, subtype_id=None, **kwargs):
        self.ensure_one()
        if kwargs.get('message_type') == 'email':
            subtype_id = request.env.ref('mail.mt_note').id
        return super(Task, self).message_post(subtype_id=subtype_id, **kwargs)


class Lead(models.Model):
    _inherit = 'crm.lead'

    xaa_aa_opp_alias = fields.Many2one('mail.alias', 'Alias', readonly=True)
    xaa_aa_attachment_ids = fields.One2many('ir.attachment', 'xaa_aa_lead_id', string='Attachments')

    @api.model
    def create(self, vals):
        res = super(Lead, self).create(vals)
        MailAlias = self.env['mail.alias'].sudo()
        ir_model = self.env['ir.model'].search([('model','=','crm.lead')])
        alias_id = MailAlias.create({
                    'alias_name':res.xaa_aa_code,
                    'alias_model_id' : ir_model.id,
                    'alias_defaults' : {'xaa_aa_lead_id' : res.id},
                    'alias_user_id': res.user_id.id
                    })
        res.xaa_aa_opp_alias = alias_id.id
        return res

    @api.model
    def message_new(self, msg, custom_values=None):
        if custom_values is None:
            custom_values = {}
        lead = custom_values.get('xaa_aa_lead_id', None)
        if lead:
            lead_id = self.browse(lead)
            return lead_id
        else:
            return super(Lead, self).message_new(msg, custom_values=custom_values)

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, subtype_id=None, **kwargs):
        self.ensure_one()
        if kwargs.get('message_type') == 'email' and self.type == 'opportunity':
            subtype_id = request.env.ref('mail.mt_note').id
        return super(Lead, self).message_post(subtype_id=subtype_id, **kwargs)


class ProjectFormulier(models.Model):
    _inherit = 'question.formulier'

    xaa_aa_formulier_alias = fields.Many2one('mail.alias', 'Alias', readonly=True)
    xaa_aa_attachment_ids = fields.One2many('ir.attachment', 'xaa_aa_formulier_id', string='Attachments')

    @api.model
    def create(self,vals):
        res = super(ProjectFormulier,self).create(vals)
        MailAlias = self.env['mail.alias'].sudo()
        ir_model = self.env['ir.model'].search([('model','=','question.formulier')])
        alias_id = MailAlias.create({
                    'alias_name': res.xaa_aa_code,
                    'alias_model_id' : ir_model.id,
                    'alias_defaults' : {'xaa_aa_formulier_id' : res.id},
                    })
        res.xaa_aa_formulier_alias = alias_id.id
        return res

    @api.model
    def message_new(self, msg, custom_values=None):
        if custom_values is None:
            custom_values = {}
        record = custom_values.get('xaa_aa_formulier_id')
        if record:
            order_id = self.env['question.formulier'].browse(record)
            return order_id
        else:
            return super(ProjectFormulier, self).message_new(msg, custom_values=custom_values)

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, subtype_id=None, **kwargs):
        self.ensure_one()
        if kwargs.get('message_type') == 'email':
            subtype_id = request.env.ref('mail.mt_note').id
        return super(ProjectFormulier, self).message_post(subtype_id=subtype_id, **kwargs)


class Attachments(models.Model):
    _inherit = 'ir.attachment'

    xaa_aa_task_id = fields.Many2one('project.task', string="Task")
    xaa_aa_order_id = fields.Many2one('sale.order', string="Sale Order")
    xaa_aa_lead_id = fields.Many2one('crm.lead', string="Opportunity")
    xaa_aa_formulier_id = fields.Many2one('question.formulier', string="Project Formulier")

    @api.model
    def create(self,vals):
        res = super(Attachments,self).create(vals)
        if res.res_model == 'project.task':
            task_id = self.env['project.task'].search([
                    ('id', '=', res.res_id)], limit=1)
            if task_id:
                task_id.xaa_aa_attachment_ids = [(4, res.id)]
        if res.res_model == 'sale.order':
            order_id = self.env['sale.order'].search([
                    ('id', '=', res.res_id)], limit=1)
            if order_id:
                order_id.xaa_aa_attachment_ids = [(4,res.id)]
        if res.res_model == 'crm.lead':
            lead_id = self.env['crm.lead'].search([
                    ('id', '=', res.res_id)], limit=1)
            if lead_id:
                lead_id.xaa_aa_attachment_ids = [(4,res.id)]
        if res.res_model == 'question.formulier':
            formulier_id = self.env['question.formulier'].search([
                    ('id', '=', res.res_id)], limit=1)
            if formulier_id:
                formulier_id.xaa_aa_attachment_ids = [(4,res.id)]
        return res
