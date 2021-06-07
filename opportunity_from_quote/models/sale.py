# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    xaa_aa_formulier_type = fields.Selection('_get_selection', string='Question Type')

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        formulier_id = res.xaa_aa_formulier_id or False
        if formulier_id:
            res.xaa_aa_lead_category = formulier_id.xaa_aa_lead_id.xaa_aa_lead_category.id
            res.xaa_aa_lead_lead_source = formulier_id.xaa_aa_lead_id.xaa_aa_lead_lead_source.id
            res.xaa_aa_formulier_type = formulier_id.xaa_aa_formulier_type
        elif res.opportunity_id and not vals.get('xaa_aa_formulier_type'):
            res.xaa_aa_formulier_type = res.opportunity_id.xaa_aa_formulier_type or False
        return res

    def write(self, vals):
        if vals.get('xaa_aa_formulier_id'):
            formulier_id = self.env['question.formulier'].browse(
                vals.get('xaa_aa_formulier_id'))
            vals.update({
                'xaa_aa_lead_category': formulier_id.xaa_aa_lead_id.xaa_aa_lead_category.id,
                'xaa_aa_lead_lead_source': formulier_id.xaa_aa_lead_id.xaa_aa_lead_lead_source.id,
                'xaa_aa_formulier_type': formulier_id.xaa_aa_formulier_type,
                })
        res = super(SaleOrder, self).write(vals)
        if vals.get('state') and vals.get('state') == 'cancel':
            stage_id = self.env['crm.stage'].sudo().search([('name','=','Verloren (18)')],limit=1)
            for record in self:
                if record.opportunity_id:
                    if stage_id.id != record.opportunity_id.stage_id.id:
                        record.opportunity_id.stage_id = stage_id.id
        return res

    @api.model
    def _get_selection(self):
        """ dynamically get all selection field options"""

        cus_type = []
        CRM = self.env['crm.lead']
        if 'xaa_aa_formulier_type' in CRM._fields.keys():
            cus_type = self.env['crm.lead'].fields_get('xaa_aa_formulier_type')['xaa_aa_formulier_type']['selection']
        return cus_type

    def action_set_opportunity(self):
        """ Create opportunity from quotation """
        result = self.env['crm.lead'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'user_id': self.user_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'expected_revenue': self.amount_total,
            'xaa_aa_sale_order_id' : self.id,
            'xaa_aa_lead_category' : self.xaa_aa_lead_category.id,
            'xaa_aa_lead_lead_source' : self.xaa_aa_lead_lead_source.id,
            'xaa_aa_formulier_type' : self.xaa_aa_formulier_type,
            'xaa_aa_formal_salutation_result' : self.xaa_aa_sale_order_partner_result,
            'tag_ids': self.tag_ids
        })
        result._onchange_par_formal_salutation()
        result._onchange_informal_salutation()
        result._onchange_crmpartner_salutation()
        result.convert_opportunity(self.partner_id.id)
        self.opportunity_id = result.id

    def preview_opportunity(self):
        """ redirect form view of  opportunity from quotation """
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'crm.lead',
            'target': 'current',
            'res_id': self.opportunity_id.id,
            'type': 'ir.actions.act_window'
        }

    # opportunity auto create from quotation when quote send and set
    # send quote stage on opportunity.
    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get('mark_so_as_sent'):
            self.filtered(lambda o: o.state == 'draft').with_context(tracking_disable=True).write({'state': 'sent'})
        if not self.opportunity_id:
            self.action_set_opportunity()
        return super(SaleOrder, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.opportunity_id:
            self.opportunity_id.action_set_won_rainbowman()
        return res

    def action_cancel(self):
        res = super(SaleOrder, self).action_cancel()
        order_cancelled_id = self.env.ref('opportunity_from_quote.lost_reason1', False)
        if self.opportunity_id:
            self.opportunity_id.action_set_lost(lost_reason=order_cancelled_id)
        return res

    def action_draft(self):
        res = super(SaleOrder, self).action_draft()
        if self.opportunity_id:
            self.opportunity_id.stage_id = self.env.ref('crm.stage_lead1', False)
        return res

    def action_quotation_send(self):
        # TODO: Dhaval
        ''' this method use to set email template which is set in Quotation Template  '''
        res = super(SaleOrder, self).action_quotation_send()
        crm_stage_id = self.env.ref('opportunity_from_quote.stage_lead6')
        if crm_stage_id and self.opportunity_id:
            if self.opportunity_id.stage_id.id != crm_stage_id.id:
                self.opportunity_id.stage_id = crm_stage_id.id
        return res
