# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    xaa_aa_cost_4_hours = fields.Integer(string='4 Hours Cost Price', default=150)
    xaa_aa_sale_4_hours = fields.Integer(string='4 Hours Sales Price', default=200)
    xaa_aa_cost_8_hours = fields.Integer(string='8 Hours Cost Price', default=300)
    xaa_aa_sale_8_hours = fields.Integer(string='8 Hours Sales Price', default=375)
    xaa_aa_cost_12_hours = fields.Integer(string='12 Hours Cost Price', default=450)
    xaa_aa_sale_12_hours = fields.Integer(string='12 Hours Sales Price', default=565)
    xaa_aa_cost_16_hours = fields.Integer(string='16 Hours Cost Price', default=600)
    xaa_aa_sale_16_hours = fields.Integer(string='16 Hours Sales Price', default=750)
    xaa_aa_cost_24_hours = fields.Integer(string='24 Hours Cost Price', default=900)
    xaa_aa_sale_24_hours = fields.Integer(string='24 Hours Sales Price', default=1125)
    xaa_aa_cost_30_hours = fields.Integer(string='30 Hours Cost Price', default=1050)
    xaa_aa_sale_30_hours = fields.Integer(string='30 Hours Sales Price', default=1300)
    xaa_aa_cost_32_hours = fields.Integer(string='32 Hours Cost Price', default=1200)
    xaa_aa_sale_32_hours = fields.Integer(string='32 Hours Sales Price', default=1500)
    xaa_aa_cost_36_hours = fields.Integer(string='36 Hours Cost Price', default=1350)
    xaa_aa_sale_36_hours = fields.Integer(string='36 Hours Sales Price', default=1650)
    xaa_aa_cost_40_hours = fields.Integer(string='40 Hours Cost Price', default=1500)
    xaa_aa_sale_40_hours = fields.Integer(string='40 Hours Sales Price', default=1875)

    xaa_aa_high_range =  fields.Integer(string='High', default=1000)
    xaa_aa_middle_range =  fields.Integer(string='Middle', default=500)
    xaa_aa_basic_range =  fields.Integer(string='Basic', default=200)
    xaa_aa_low_range =  fields.Integer(string='Low', default=0)

class FormulierConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    xaa_aa_cost_4_hours = fields.Integer(string='4 Hours Cost Price',
        related='company_id.xaa_aa_cost_4_hours', readonly=False)
    xaa_aa_sale_4_hours = fields.Integer(string='4 Hours Sales Price',
        related='company_id.xaa_aa_sale_4_hours', readonly=False)
    xaa_aa_cost_8_hours = fields.Integer(string='8 Hours Cost Price',
        related='company_id.xaa_aa_cost_8_hours', readonly=False)
    xaa_aa_sale_8_hours = fields.Integer(string='8 Hours Sales Price',
        related='company_id.xaa_aa_sale_8_hours', readonly=False)
    xaa_aa_cost_12_hours = fields.Integer(string='12 Hours Cost Price',
        related='company_id.xaa_aa_cost_12_hours', readonly=False)
    xaa_aa_sale_12_hours = fields.Integer(string='12 Hours Sales Price',
        related='company_id.xaa_aa_sale_12_hours', readonly=False)
    xaa_aa_cost_16_hours = fields.Integer(string='16 Hours Cost Price',
        related='company_id.xaa_aa_cost_16_hours', readonly=False)
    xaa_aa_sale_16_hours = fields.Integer(string='16 Hours Sales Price',
        related='company_id.xaa_aa_sale_16_hours', readonly=False)
    xaa_aa_cost_24_hours = fields.Integer(string='24 Hours Cost Price',
        related='company_id.xaa_aa_cost_24_hours', readonly=False)
    xaa_aa_sale_24_hours = fields.Integer(string='24 Hours Sales Price',
        related='company_id.xaa_aa_sale_24_hours', readonly=False)
    xaa_aa_cost_30_hours = fields.Integer(string='30 Hours Cost Price',
        related='company_id.xaa_aa_cost_30_hours', readonly=False)
    xaa_aa_sale_30_hours = fields.Integer(string='30 Hours Sales Price',
        related='company_id.xaa_aa_sale_30_hours', readonly=False)
    xaa_aa_cost_32_hours = fields.Integer(string='32 Hours Cost Price',
        related='company_id.xaa_aa_cost_32_hours', readonly=False)
    xaa_aa_sale_32_hours = fields.Integer(string='32 Hours Sales Price',
        related='company_id.xaa_aa_sale_32_hours', readonly=False)
    xaa_aa_cost_36_hours = fields.Integer(string='36 Hours Cost Price',
        related='company_id.xaa_aa_cost_36_hours', readonly=False)
    xaa_aa_sale_36_hours = fields.Integer(string='36 Hours Sales Price',
        related='company_id.xaa_aa_sale_36_hours', readonly=False)
    xaa_aa_cost_40_hours = fields.Integer(string='40 Hours Cost Price',
        related='company_id.xaa_aa_cost_40_hours', readonly=False)
    xaa_aa_sale_40_hours = fields.Integer(string='40 Hours Sales Price',
        related='company_id.xaa_aa_sale_40_hours', readonly=False)

    xaa_aa_high_range =  fields.Integer(string='High',
        related='company_id.xaa_aa_high_range', readonly=False)
    xaa_aa_middle_range =  fields.Integer(string='Middle',
        related='company_id.xaa_aa_middle_range', readonly=False)
    xaa_aa_basic_range =  fields.Integer(string='Basic',
        related='company_id.xaa_aa_basic_range', readonly=False)
    xaa_aa_low_range =  fields.Integer(string='Low',
        related='company_id.xaa_aa_low_range', readonly=False)
