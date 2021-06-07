# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _
from odoo.http import request


class CrmLead(models.Model):
    """ Project Formulier Tab in CRM"""

    _inherit = "crm.lead"

    xaa_aa_formulier_id = fields.Many2one('question.formulier', string='Project Formulier', readonly=True)
    xaa_aa_formulier_type = fields.Selection([], string='Question Type')
    xaa_aa_soort = fields.Selection(string='Soort', selection=[('aanbouw', 'aanbouw'),
        ('hoek', 'hoek'), ('gevel', 'kopgevel'), ('groot deel', 'groot deel')],
        default='aanbouw')
    xaa_aa_lead_number = fields.Integer(compute='_compute_opportunity', string="Number of opportunities")
    opportunity_count = fields.Integer("Number of opportunities", compute='_opportunity_count')
    total_quote_count = fields.Integer("Number of quote", compute='_total_quote_count')


    def _opportunity_count(self):
        for record in self:
            if record.partner_id:
                count_oppo = self.env['crm.lead'].search_count([
                    ('partner_id','=',record.partner_id.id)])
                record.opportunity_count = count_oppo or 0
            else:
                record.opportunity_count = 0

    def _total_quote_count(self):
        for record in self:
            if record.partner_id:
                count_quote = self.env['sale.order'].search_count([
                    ('partner_id','=',record.partner_id.id)])
                record.total_quote_count = count_quote or 0
            else:
                record.total_quote_count = 0

    def act_res_partner_2_opportunity(self):
        if self.partner_id:
            ctx = {
                'default_partner_id': self.partner_id.id,
                'search_default_partner_id': self.partner_id.id,
            }
            return {
                'type': 'ir.actions.act_window',
                'name': _('Opportunities'),
                'view_mode': 'tree,form',
                'res_model': 'crm.lead',
                'target': 'current',
                'context': ctx,
            }
        else:
            return False

    def act_res_partner_2_quote(self):
        if self.partner_id:
            ctx = {
                'default_partner_id': self.partner_id.id,
                'search_default_partner_id': self.partner_id.id,
            }
            return {
                'type': 'ir.actions.act_window',
                'name': 'Sale Order',
                'view_mode': 'tree,form',
                'res_model': 'sale.order',
                'target': 'current',
                'context': ctx,
            }
        else:
            return False

    def add_soort(self):
        if self.xaa_aa_lead_category:
            if self.xaa_aa_lead_category.xaa_aa_name in ['aanbouw','hoek','gevel','groot deel']:
                self.xaa_aa_soort = self.xaa_aa_lead_category.xaa_aa_name

    @api.model
    def create(self, vals):
        res = super(CrmLead,self).create(vals)
        res.add_soort()
        return res

    def _convert_opportunity_data(self, customer, team_id=False):
        res = super(CrmLead,self)._convert_opportunity_data(customer, team_id)
        ProjectFormulier = self.env['question.formulier']

        # soort fill-up base on lead category and planned revenue default value set base on soort
        self.add_soort()

        partner = self.partner_id or customer
        name = res.get('name') or self.name or ''
        if partner:
            formulier_id = ProjectFormulier.create({
                                                    'xaa_aa_name': name +' PF',
                                                    'xaa_aa_partner_id': partner.id or False,
                                                    'xaa_aa_street': partner.street or '',
                                                    'xaa_aa_street2': partner.street2 or '',
                                                    'xaa_aa_zip': partner.zip or '',
                                                    'xaa_aa_city': partner.city or '',
                                                    'xaa_aa_state_id': partner.state_id.id or False,
                                                    'xaa_aa_country_id': partner.country_id.id or False,
                                                    'xaa_aa_phone': partner.phone,
                                                    'xaa_aa_mobile': partner.mobile,
                                                    'xaa_aa_lead_id': self.id,
                                                    'xaa_aa_state': 'opportunity',
                                                    'xaa_aa_user_id': self.user_id.id or False,
                                                    'xaa_aa_created_by': request.env.user.id,
                                                    })
            self.xaa_aa_formulier_id = formulier_id.id
        return res

    def create_project_formulier(self):
        ProjectFormulier = self.env['question.formulier']
        partner = self.partner_id
        name = self.name or ''
        formulier_id = ProjectFormulier.create({
                                                'xaa_aa_name': name +' PF',
                                                'xaa_aa_partner_id': partner.id or False,
                                                'xaa_aa_street': partner.street or '',
                                                'xaa_aa_street2': partner.street2 or '',
                                                'xaa_aa_zip': partner.zip or '',
                                                'xaa_aa_city': partner.city or '',
                                                'xaa_aa_state_id': partner.state_id.id or False,
                                                'xaa_aa_country_id': partner.country_id.id or False,
                                                'xaa_aa_phone': partner.phone,
                                                'xaa_aa_mobile': partner.mobile,
                                                'xaa_aa_lead_id': self.id,
                                                'xaa_aa_state': 'opportunity',
                                                'xaa_aa_user_id': self.user_id.id or False,
                                                'xaa_aa_created_by': request.env.user.id,
                                                })
        self.xaa_aa_formulier_id = formulier_id.id
        return True

    def project_formulier_form_view(self):
        return {
            'name': 'Project Formulier',
            'res_model': 'question.formulier',
            'type': 'ir.actions.act_window',
            'res_id': self.xaa_aa_formulier_id.id,
            'context': {},
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('project_formulier.view_project_formulier_form').id,
            'target': '_blank',
            }

    def project_formulier_online(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/project-formulier/'+str(self.xaa_aa_formulier_id.id)+'/'+str(self.xaa_aa_formulier_id.xaa_aa_pf_access),
            'target': '_blank',
            }
