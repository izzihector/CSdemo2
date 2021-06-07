    # -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _


#----------------------------------------------------------
# Trademark for Company
#----------------------------------------------------------
class CompanyTrademark(models.Model):
    _name = "company.trademark"
    _description = "Trade mark decide report header/footer"
    _rec_name = "xaa_aa_name"

    xaa_aa_name = fields.Char('Name')
    xaa_aa_report_header = fields.Binary('Header')
    xaa_aa_report_footer = fields.Binary('Footer')
    xaa_aa_analytic_account_group_id = fields.Many2one('account.analytic.group',
                                            'Analytic Account Group')
    xaa_aa_company_id = fields.Many2one('res.company',
                                 default=lambda self: self.env.user.company_id)
    xaa_aa_pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
    xaa_aa_short_code = fields.Char('Short Code')
    xaa_aa_email_sent = fields.Char('Email Sent')
    xaa_aa_email_reply = fields.Char('Email Reply')


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _default_trademark_id(self):
        """set default trademark on partner"""

        return self.env['company.trademark'].search([], limit=1).id

    xaa_aa_trademark_id = fields.Many2one('company.trademark', string='Trademark',
                                   default=_default_trademark_id)

class CrmLeadStage(models.Model):
    _inherit = "crm.stage"

    xaa_aa_trademark_id = fields.Many2one('company.trademark', string='Trademark')

class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_trademark_id = fields.Many2one('company.trademark', string='Trademark')

    @api.model
    def create(self,vals):
        res = super(CrmLead, self).create(vals)
        if res.stage_id and res.stage_id.xaa_aa_trademark_id:
            res.xaa_aa_trademark_id = res.stage_id.xaa_aa_trademark_id.id or False
        return res

    def write(self,vals):
        res = super(CrmLead, self).write(vals)
        if vals.get('stage_id'):
            stage_id = self.env['crm.stage'].browse(vals.get('stage_id'))
            if stage_id.xaa_aa_trademark_id:
                self.xaa_aa_trademark_id = stage_id.xaa_aa_trademark_id.id or False
        return res

    def action_new_quotation(self):
        res = super(CrmLead, self).action_new_quotation()
        res['context'].update({
            'default_xaa_aa_trademark_id': self.xaa_aa_trademark_id and self.xaa_aa_trademark_id.id or False,
        })
        return res


class SaleOrderLineInherit(models.Model):
    _inherit = "sale.order.line"

    analytic_account_id = fields.Many2one(related='order_id.analytic_account_id',
                                          string='Analytic Account',
                                          store = True)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _default_trademark_id(self):
        """set default trademark on sale order"""

        if self.opportunity_id:
            return self.opportunity_id.xaa_aa_trademark_id.id

    xaa_aa_trademark_id = fields.Many2one('company.trademark', string = 'Trademark',default=_default_trademark_id)
    xaa_aa_analytic_account_group_id = fields.Many2one(string='Analytic Account Group',
                                               related ='xaa_aa_trademark_id.xaa_aa_analytic_account_group_id',
                                               store = True)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Pricelist for current sales order.")

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(SaleOrder, self).onchange_partner_id()
        if self.partner_id.xaa_aa_trademark_id:
            self.xaa_aa_trademark_id = self.partner_id.xaa_aa_trademark_id and self.partner_id.xaa_aa_trademark_id.id or False
        return res

    @api.model
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        if res:
            res.update({'xaa_aa_trademark_id': self.xaa_aa_trademark_id.id or False,
                        #'pricelist_id': self.pricelist_id.id or False
                        })
        return res

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if '%(shortcode)s' in res.name:
            code = ''
            if res.xaa_aa_trademark_id and res.xaa_aa_trademark_id.xaa_aa_short_code:
                code = res.xaa_aa_trademark_id.xaa_aa_short_code
            res.name = res.name.replace('%(shortcode)s',code)
        return res

    def _action_confirm(self):
        for order in self:
            if not order.analytic_account_id:
                order._create_analytic_account()
        return super(SaleOrder, self)._action_confirm()

    def action_quotation_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('sale', 'email_template_edi_sale')[1]
            temp_id = self.env['mail.template'].search([('id', "=", template_id)])
            if temp_id and self.xaa_aa_trademark_id and self.xaa_aa_trademark_id.xaa_aa_email_sent and self.xaa_aa_trademark_id.xaa_aa_email_reply:
                temp_id.write({'email_from': self.xaa_aa_trademark_id.xaa_aa_email_sent,
                               'reply_to': self.xaa_aa_trademark_id.xaa_aa_email_reply})
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = {
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

    def _create_analytic_account(self, prefix=None):
        for order in self:
            name = order.name
            if prefix:
                name = prefix + ": " + order.name
            analytic = self.env['account.analytic.account'].create({
                'name': name,
                'code': order.client_order_ref,
                'company_id': order.company_id.id,
                'partner_id': order.partner_id.id,
                'group_id':order.xaa_aa_analytic_account_group_id.id
            })
            order.analytic_account_id = analytic


class AccountMove(models.Model):
    _inherit = "account.move"

    def _default_trademark_id(self):
        """set default trademark on invoice"""
        return self.env['company.trademark'].search([], limit=1).id

    xaa_aa_trademark_id = fields.Many2one('company.trademark', string='Trademark',
                                   default=_default_trademark_id)

    def action_invoice_sent(self):
        """ Open a window to compose an email, with the edi invoice template
            message loaded by default
        """
        self.ensure_one()
        template = self.env.ref('account.email_template_edi_invoice', False)
        if self.xaa_aa_trademark_id.xaa_aa_email_sent and self.xaa_aa_trademark_id.xaa_aa_email_reply:
            template.write({'email_from': self.xaa_aa_trademark_id.xaa_aa_email_sent,
                            'reply_to': self.xaa_aa_trademark_id.xaa_aa_email_reply})
        compose_form = self.env.ref('account.account_invoice_send_wizard_form', False)
        ctx = dict(
            default_model='account.move',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_composition_mode='comment',
            mark_invoice_as_sent=True,
            custom_layout="mail.mail_notification_paynow",
            force_email=True
        )
        return {
            'name': _('Send Invoice'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.invoice.send',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }
