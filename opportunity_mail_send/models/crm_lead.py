# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api, tools

class OpportunityMail(models.Model):

    _name = "opportunity.mail.configure"
    _description = "Configure for mail send on convert lead to opportunity"

    xaa_aa_name = fields.Char(string="Name")
    xaa_aa_lead_lead_source = fields.Many2one("lead.source", string="Lead Source")
    xaa_aa_lead_category = fields.Many2one("lead.category", string="Lead Category")
    xaa_aa_email_template_id = fields.Many2one("mail.template", string="Email Template")
    xaa_aa_zip_range_from = fields.Integer(string="Zip code range from")
    xaa_aa_zip_range_to = fields.Integer(string="Zip code range to")

class CrmLead(models.Model): 
    _inherit = "crm.lead"

    def _convert_opportunity_data(self, customer, team_id=False):
        res = super(CrmLead,self)._convert_opportunity_data(customer, team_id)
        OpportunityConfig = self.env['opportunity.mail.configure']
        if self.xaa_aa_lead_lead_source and self.xaa_aa_lead_category and self.partner_id and len(self.zip) > 1 if self.zip else '':
            opportunity_config = OpportunityConfig.search([('xaa_aa_lead_lead_source', '=', self.xaa_aa_lead_lead_source.id),
                                        ('xaa_aa_lead_category', '=', self.xaa_aa_lead_category.id),
                                        ('xaa_aa_zip_range_from', '<=', int(self.zip[0:2])),
                                        ('xaa_aa_zip_range_to', '>=', int(self.zip[0:2])),], limit=1)
            if opportunity_config and opportunity_config.xaa_aa_email_template_id:
                template_id = opportunity_config.xaa_aa_email_template_id
                template_id.send_mail(self.id, force_send=True)
        return res
