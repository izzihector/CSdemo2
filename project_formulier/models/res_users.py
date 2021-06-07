# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class FormulierCustomerType(models.Model):
    _name = 'formulier.customer.type'
    _description = 'formulier customer type add many2many on user form'
    _rec_name = "xaa_aa_name"

    xaa_aa_name = fields.Char('Name')
    xaa_aa_technical_name = fields.Char('Technical Name')


class ResUsers(models.Model):
    """ Add project formulier tab on user form """

    _inherit = "res.users"

    xaa_aa_formulier_type = fields.Many2many('formulier.customer.type', string="Formulier Type")
    xaa_aa_template_id = fields.Many2many('sale.order.template', string='Quotation Template')
    xaa_aa_lead_category = fields.Many2many("lead.category", string="Lead Category")
    xaa_aa_lead_lead_source = fields.Many2many("lead.source", string="Lead Source")
    xaa_aa_redirect_pf_url = fields.Selection([('website_offerte', 'Website offerte'),
                                        ('project_formulier_offerte', 'Project formulier offerte')],
                                        string='Succession')
