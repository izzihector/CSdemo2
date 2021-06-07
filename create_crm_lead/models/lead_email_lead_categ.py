# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class LeadEmailLeadCategory(models.Model):
    _name = 'lead.email.lead.category'
    _description = 'Email Lead Category'
    _rec_name = 'xaa_aa_lead_category'

    xaa_aa_lead_category = fields.Many2one('lead.category', string='Lead Category')
    xaa_aa_lead_email_lead_source = fields.Many2one(
        'lead.email.lead.source', string='Lead Email Lead Source')
    xaa_aa_content = fields.Char('Content')
    xaa_aa_priority = fields.Char('Priority')


class LeadEmailLeadSource(models.Model):
    _name = 'lead.email.lead.source'
    _description = 'Email Lead Source'
    _rec_name = 'xaa_aa_name'

    xaa_aa_name = fields.Char(compute='_compute_name', store=True, string='Name')
    xaa_aa_lead_source = fields.Many2one('lead.source', string="Lead Source")
    xaa_aa_domain = fields.Char(string='Domain')

    @api.depends(
        'xaa_aa_lead_source', 'xaa_aa_lead_source.xaa_aa_name', 'xaa_aa_domain')
    def _compute_name(self):
        for rec in self:
            rec.xaa_aa_name = ' '.join(
                [x for x in [rec.xaa_aa_lead_source and
                             rec.xaa_aa_lead_source.xaa_aa_name,
                             rec.xaa_aa_domain] if x])
