# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api


class LeadCategory(models.Model):
    _name = "lead.category"
    _description = 'Lead Category'
    _rec_name = "xaa_aa_name"

    xaa_aa_name = fields.Char(string="Lead Category")
    xaa_aa_tag_ids = fields.Many2many('crm.tag', string='Tags')


class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_lead_category = fields.Many2one("lead.category", string="Lead Category")

    @api.onchange('xaa_aa_lead_category')
    def set_tags(self):
        self.tag_ids = self.xaa_aa_lead_category.xaa_aa_tag_ids

class SaleOrder(models.Model):
    _inherit = "sale.order"

    xaa_aa_lead_category = fields.Many2one("lead.category", string="Lead Category")


    @api.model
    def create(self,vals):
        """ Set Lead Category based on opportunity if Lead Category not set on SO."""
        res = super(SaleOrder, self).create(vals)
        if res.opportunity_id and res.opportunity_id.xaa_aa_lead_category and not res.xaa_aa_lead_category:
            res.xaa_aa_lead_category = res.opportunity_id.xaa_aa_lead_category.id
        return res