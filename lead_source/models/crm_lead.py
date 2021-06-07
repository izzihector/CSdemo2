# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api


class LeadSource(models.Model):
    _name = "lead.source"
    _description = 'Lead Source'
    _rec_name = "xaa_aa_name"

    xaa_aa_name = fields.Char(string="Lead Source")

class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_lead_lead_source = fields.Many2one("lead.source", string="Lead Source")

class SaleOrder(models.Model):
    _inherit = "sale.order"

    xaa_aa_lead_lead_source = fields.Many2one("lead.source", string="Lead Source")

    @api.model
    def create(self,vals):
        """ Set Lead Source based on opportunity if Lead Source not set on SO."""
        res = super(SaleOrder, self).create(vals)
        if res.opportunity_id and res.opportunity_id.xaa_aa_lead_lead_source and not res.xaa_aa_lead_lead_source:
            res.xaa_aa_lead_lead_source = res.opportunity_id.xaa_aa_lead_lead_source.id
        return res