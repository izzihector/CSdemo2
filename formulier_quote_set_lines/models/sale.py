# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleLineConfig(models.Model):
    _name = "sale.line.config"
    _description = "Add lines in order from configuration"
    _rec_name = 'xaa_aa_qty_hours'

    xaa_aa_qty = fields.Integer(string='Number of products')
    xaa_aa_formulier_type = fields.Selection([], string='Type product')
    xaa_aa_qty_hours = fields.Selection([
        ('1', '1 Hours'),
        ('2', '2 Hours'),
        ('3', '3 Hours'),
        ('4', '4 Hours'),
        ('5', '5 Hours'),
        ('6', '6 Hours'),
        ('7', '7 Hours'),
        ('8', '8 Hours'),
        ('9', '9 Hours'),
        ('10', '10 Hours'),
        ('11', '11 Hours'),
        ('12', '12 Hours'),
        ('13', '13 Hours'),
        ('14', '14 Hours'),
        ('15', '15 Hours'),
        ('16', '16 Hours'),
        ('17', '17 Hours'),
        ('18', '18 Hours'),
        ('19', '19 Hours'),
        ('20', '20 Hours'),
        ('21', '21 Hours'),
        ('22', '22 Hours'),
        ('23', '23 Hours'),
        ('24', '24 Hours'),
        ('25', '25 Hours'),
        ('26', '26 Hours'),
        ('27', '27 Hours'),
        ('28', '28 Hours'),
        ('29', '29 Hours'),
        ('30', '30 Hours'),
        ('31', '31 Hours'),
        ('32', '32 Hours'),
        ('33', '33 Hours'),
        ('34', '34 Hours'),
        ('35', '35 Hours'),
        ('36', '36 Hours'),
        ('37', '37 Hours'),
        ('38', '38 Hours'),
        ('39', '39 Hours'),
        ('40', '40 Hours'),
        ('41', '41 Hours'),
        ('42', '42 Hours'),
        ('43', '43 Hours'),
        ('44', '44 Hours'),
        ('45', '45 Hours'),
        ('46', '46 Hours'),
        ('47', '47 Hours'),
        ('48', '48 Hours'),
        ('49', '49 Hours'),
        ('50', '50 Hours'),
        ], string='Qnty hours')
    xaa_aa_team_time = fields.Selection([
        ('Halve dag', 'Halve dag'),
        ('Hele dag', 'Hele dag'),
        ('Hele dag + extra pers', 'Hele dag + extra pers'),
        ('Twee dagen', 'Twee dagen'),
        ], string='Expensive Team')
    xaa_aa_team_sale = fields.Float(string='Sales Team')
    xaa_aa_team_cost = fields.Float(string='Cost team')
    xaa_aa_overhead_one = fields.Float(string='Costs Overhead')
    xaa_aa_overhead_two = fields.Float(string='Costs Sales')
    xaa_aa_sales_overhead_one = fields.Float(string='Sales Overhead')
    xaa_aa_sales_overhead_two = fields.Float(string='Sell Sales')
    xaa_aa_sales_option_one = fields.Float(string='Sell Extra 1')
    xaa_aa_cost_option_one = fields.Float(string='Cost Extra 1')
    xaa_aa_sales_option_two = fields.Float(string='Sell Extra 2')
    xaa_aa_cost_option_two = fields.Float(string='Cost Extra 2')
    xaa_aa_commission = fields.Float(string='Commission')
    xaa_aa_overhead_total = fields.Monetary(string='Cost overhead total',
        store=True, readonly=True, compute='_amount_all')
    xaa_aa_total = fields.Monetary(string='Cost total',
        store=True, readonly=True, compute='_amount_all')
    xaa_aa_sales_overhead_total = fields.Monetary(string='Sales overhead total',
        store=True, readonly=True, compute='_sales_amount_all')
    xaa_aa_sales_total = fields.Monetary(string='Sales total',
        store=True, readonly=True, compute='_sales_amount_all')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one(related='company_id.currency_id', store=True)

    @api.depends('xaa_aa_team_cost', 'xaa_aa_overhead_one', 'xaa_aa_overhead_two', 'xaa_aa_cost_option_one', 'xaa_aa_cost_option_two')
    def _amount_all(self):
        for record in self:
            record.xaa_aa_overhead_total = record.xaa_aa_overhead_one + record.xaa_aa_overhead_two
            record.xaa_aa_total = record.xaa_aa_overhead_total + record.xaa_aa_team_cost + record.xaa_aa_cost_option_one + record.xaa_aa_cost_option_two

    @api.depends('xaa_aa_team_sale', 'xaa_aa_sales_overhead_one', 'xaa_aa_sales_overhead_two', 'xaa_aa_sales_option_one', 'xaa_aa_sales_option_two')
    def _sales_amount_all(self):
        for record in self:
            record.xaa_aa_sales_overhead_total = record.xaa_aa_sales_overhead_one + record.xaa_aa_sales_overhead_two
            record.xaa_aa_sales_total = record.xaa_aa_sales_overhead_total + record.xaa_aa_team_sale + record.xaa_aa_sales_option_one + record.xaa_aa_sales_option_two


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def add_formulier_lines(self):
        ''' use in formulier type modules '''
        return True
