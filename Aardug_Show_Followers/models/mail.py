# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################


from odoo import api, models, fields

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    follower_names = fields.Char()

    @api.model
    def default_get(self, fields):
        result = super(MailComposeMessage, self).default_get(fields)
        follower_list = []
        if self._context.get('default_model'):
            model = self._context.get('default_model')
            record_id = self._context.get('default_res_id')
            main_record_id = self.env[model].browse(record_id)
            for partner in main_record_id.message_partner_ids:
                p_id = follower_list.append(partner.name)
            follower_lists = ',  '.join(follower_list)
            result['follower_names'] = follower_lists
        return result
