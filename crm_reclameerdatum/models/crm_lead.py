from odoo import models, fields, api, tools
import datetime

class Lead_Source(models.Model):
    _inherit = "lead.source"

    xaa_aa_days = fields.Integer(string="Days")

class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_reclameer_date = fields.Date(string="Reclameerdatum")
    xaa_aa_log_reclameer = fields.Boolean(string="Log Reclameer")
    xaa_aa_log_attr = fields.Boolean(string="Log Attr")

    def write(self, vals):
        LeadSource = self.env['lead.source']
        present_date = datetime.datetime.today()
        res=super(CrmLead, self).write(vals)
        if vals.get('xaa_aa_lead_lead_source'):
            lead_source_id = LeadSource.browse(vals.get('xaa_aa_lead_lead_source'))
            date = datetime.datetime.strftime(self.create_date, "%Y-%m-%d %H:%M:%S")
            create_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            reclameer_date = create_date + datetime.timedelta(days=lead_source_id.xaa_aa_days)
            if (self.stage_id.xaa_aa_log_reclameer and 
                reclameer_date < present_date and self.type=='opportunity'):
                self.xaa_aa_log_attr = True
                self.xaa_aa_log_reclameer = True
            self.xaa_aa_reclameer_date = reclameer_date
        return res

    @api.model
    def _update_crm_reclameerdatum(self):
        CrmStage = self.env['crm.stage']
        stage_ids = CrmStage.search([('xaa_aa_log_reclameer', '=', True)])
        present_date = datetime.date.today()
        opportunity_ids = self.search([('xaa_aa_reclameer_date','<',present_date),
                                        ('stage_id','in',stage_ids.ids),
                                        ('type','=','opportunity'),
                                        ('xaa_aa_log_attr','=',False)])
        for opp_id in opportunity_ids:
            opp_id.xaa_aa_log_attr = True
            opp_id.xaa_aa_log_reclameer = True

    @api.model
    def _calculate_reclameerdatum(self):
        LeadSource = self.env['lead.source']
        lead_source_ids = LeadSource.search([])
        for lead_source_id in lead_source_ids:
            if lead_source_id.xaa_aa_days:
                opportunity_ids = self.search([
                    ('type','=','opportunity'),
                    ('xaa_aa_lead_lead_source','=',lead_source_id.id),
                ])
                for opp_id in opportunity_ids:
                    date = datetime.datetime.strftime(opp_id.create_date, "%Y-%m-%d %H:%M:%S")
                    create_date = datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
                    reclameer_date = create_date + datetime.timedelta(
                        days=lead_source_id.xaa_aa_days)
                    opp_id.xaa_aa_reclameer_date = reclameer_date


class CrmStage(models.Model):
    _inherit = "crm.stage"

    xaa_aa_log_reclameer = fields.Boolean(string="Log Reclameer")
