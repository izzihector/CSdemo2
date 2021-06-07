# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    xaa_aa_show_only_total = fields.Boolean('Show Only Total', default=True)

    @api.onchange('xaa_aa_show_only_total')
    def _onchange_partner_id(self):
        user = self.env['res.users'].search([('name', 'ilike', 'Niels Pikkemaat')],limit=1)
        if user:
            self.invoice_user_id = user.id
        return super(AccountMove, self)._onchange_partner_id()

    @api.model_create_multi
    def create(self, vals_list):
        rslt = super(AccountMove, self).create(vals_list)
        for res in rslt:
            if res.invoice_origin:
                user = self.env['res.users'].search([('name', 'ilike', 'Niels Pikkemaat')],limit=1)
                if user:
                    res.invoice_user_id = user.id
        return rslt

    def action_post(self):
        order_amount = 0
        if self.invoice_origin and not self._context.get('warning'):
            sale_id = self.env['sale.order'].search([('name', '=', self.invoice_origin)], limit=1)
            if sale_id:
                order_amount = sale_id.amount_total
                if self.amount_total != order_amount:
                    message = 'Sale amount({0}) and invoice amount({1}) is not equal'.format(order_amount,self.amount_total)
                    return {
                        'name': 'Invoice amount compare',
                        'view_mode': 'form',
                        'res_model': 'account.move.amount',
                        'view_id': self.env.ref('quote_print.account_move_amount_view_form').id,
                        'type': 'ir.actions.act_window',
                        'context': {'default_move_id': self.id, 'default_warning_message': message},
                        'target': 'new'
                    }
        return super(AccountMove, self).action_post()

class AccountMoveAmount(models.TransientModel):
    _name = 'account.move.amount'
    _description = "Account Move Amount"

    move_id = fields.Many2one('account.move',
        string='Account Move', required=True, ondelete='cascade')
    warning_message = fields.Char(string='Warning message')

    def action_cancel(self):
        return self.move_id.with_context({'warning': True}).action_post()
