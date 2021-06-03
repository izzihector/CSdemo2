# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'


    company_ids = fields.Many2many('res.company', 'res_company_partner_rel', 'partner_id', 'cid',
        string='Companies')
