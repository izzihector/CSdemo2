# -*- coding: utf-8 -*-


from odoo import fields, models, tools

class CrmSalesPersonReport(models.Model):
    _name = "crm.sales.person.report"
    _description = "CRM Statistics"
    _auto = False

    xaa_aa_quote = fields.Many2one('res.users', string='Quote')
    xaa_aa_user_id = fields.Many2one('res.users', string='Sales Person')
    xaa_aa_opportunity = fields.Many2one('res.users', string='Meeting')
    xaa_aa_deal = fields.Many2one('res.users', string='Deal')
    xaa_aa_work = fields.Many2one('res.users', string='Work')
    xaa_aa_phone = fields.Many2one('res.users', string='Call')
    xaa_aa_work_date = fields.Datetime(string='Work Date')
    xaa_aa_deal_date = fields.Datetime(string='Deal Date')
    xaa_aa_opportunity_date = fields.Datetime(string='Meeting Date')
    xaa_aa_quote_date = fields.Datetime(string='Quote Date')
    xaa_aa_phone_date = fields.Datetime(string='Call Date')
    xaa_aa_user_by_total = fields.Integer(string='Total Created')
    xaa_aa_deal_by_total = fields.Integer(string='Total Deal')
    xaa_aa_opportunity_by_total = fields.Integer(string='Total Meeting')
    xaa_aa_work_by_total = fields.Integer(string='Total Work')
    xaa_aa_phone_by_total = fields.Integer(string='Total Call')
    xaa_aa_quote_by_total = fields.Integer(string='Total Quote')
    
    def init(self):
        tools.drop_view_if_exists(self._cr, 'crm_sales_person_report')
        self._cr.execute("""CREATE OR REPLACE VIEW crm_sales_person_report AS (
                                                        SELECT
                                                        max(id) as id,
                                                        user_id as xaa_aa_user_id,
                                                        xaa_aa_quote_by as xaa_aa_quote,
                                                        xaa_aa_phone_by as xaa_aa_phone,
                                                        xaa_aa_deal_by as  xaa_aa_deal,
                                                        xaa_aa_work_by as xaa_aa_work,
                                                        xaa_aa_opportunity_by as xaa_aa_opportunity,
                                                        xaa_aa_deal_date as xaa_aa_deal_date,
                                                        xaa_aa_work_date as xaa_aa_work_date,
                                                        xaa_aa_phone_date as xaa_aa_phone_date,
                                                        xaa_aa_opportunity_date as xaa_aa_opportunity_date,
                                                        xaa_aa_quote_date as xaa_aa_quote_date,
                                                        count(user_id) as xaa_aa_user_by_total,
                                                        count(xaa_aa_quote_by) as xaa_aa_quote_by_total,
                                                        count(xaa_aa_phone_by) as xaa_aa_phone_by_total,
                                                        count(xaa_aa_deal_by) as  xaa_aa_deal_by_total,
                                                        count(xaa_aa_work_by) as xaa_aa_work_by_total,
                                                        count(xaa_aa_opportunity_by) as xaa_aa_opportunity_by_total
                                                        FROM
                                                        crm_lead 
                                                        WHERE type = 'opportunity'
                                                        GROUP BY 
                                                        id,
                                                        user_id,
                                                        xaa_aa_quote_by,
                                                        xaa_aa_phone_by,
                                                        xaa_aa_deal_by,
                                                        xaa_aa_work_by,
                                                        xaa_aa_deal_date, 
                                                        xaa_aa_work_date,
                                                        xaa_aa_phone_date,
                                                        xaa_aa_opportunity_date,
                                                        xaa_aa_quote_date
)""" )


