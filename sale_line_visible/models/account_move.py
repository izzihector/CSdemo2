# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, api, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    xaa_aa_invisible = fields.Boolean(string='Not Visible')

    @api.model_create_multi
    def create(self, vals_list):
        res = super(AccountMoveLine, self).create(vals_list)
        for move_line in res:
            for line in move_line.sale_line_ids:
                move_line.xaa_aa_invisible = line.xaa_aa_invisible
        return res

    @api.onchange('product_id')
    def _onchange_product_id(self):
        super(AccountMoveLine, self)._onchange_product_id()
        for line in self:
            if not line.product_id or line.display_type in ('line_section', 'line_note'):
                continue
            line.xaa_aa_invisible = line.product_id.xaa_aa_invisible
