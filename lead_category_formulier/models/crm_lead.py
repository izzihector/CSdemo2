# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models

class FormulierTypeToCategory(models.Model):
    _inherit = "lead.category"

    xaa_aa_formulier_type = fields.Selection('_get_selection', string="Question Type", store=True)

    @api.model
    def _get_selection(self):
        """ dynamically get all selection field options"""
        cus_type = []
        CRM = self.env['crm.lead']
        if 'xaa_aa_formulier_type' in CRM._fields.keys():
            cus_type = self.env['crm.lead'].fields_get('xaa_aa_formulier_type')['xaa_aa_formulier_type']['selection']
        return cus_type

class UpdateCrmLead(models.Model):
    _inherit = "crm.lead"

    @api.onchange('xaa_aa_lead_category')
    def onchange_lead_category(self):
        """ use try catch beacuse if lead have not same customer type selection field options then it not give error"""
        try:
            self.xaa_aa_formulier_type = self.xaa_aa_lead_category.xaa_aa_formulier_type
        except Exception as e:
            pass

    @api.model
    def create(self, vals):
        res = super(UpdateCrmLead, self).create(vals)
        if not vals.get('xaa_aa_formulier_type'):
            if vals.get('xaa_aa_lead_category'):
                try:
                    res.xaa_aa_formulier_type = self.env['lead.category'].browse(vals['xaa_aa_lead_category']).xaa_aa_formulier_type
                except Exception as e:
                    pass
        return res

    def write(self, vals):
        res = super(UpdateCrmLead, self).write(vals)
        if vals.get('xaa_aa_lead_category') and not self.xaa_aa_formulier_type:
            try:
                self.xaa_aa_formulier_type = self.env['lead.category'].browse(vals['xaa_aa_lead_category']).xaa_aa_formulier_type
            except Exception as e:
                pass
        return res