# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields


class Lead(models.Model): 
    _inherit = 'crm.lead'

    xaa_aa_sale_order_id = fields.Many2one('sale.order', string='Sale Order')