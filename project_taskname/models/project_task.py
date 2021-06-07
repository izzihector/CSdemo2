# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api, tools

class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def create(self, vals):
        res = super(ProjectTask,self).create(vals)
        if res.sale_order_id:
            order = res.sale_order_id
            partner_name = res.partner_id.name
            city = res.partner_id.city or ''
            merge = ''.join([
                            tools.ustr(partner_name) if partner_name else '',
                            tools.ustr('-'+city) if city else '',
                            tools.ustr('-'+order.name),
                            tools.ustr('-'+res.sale_line_id.name),
                            ])
            res.name = merge
        return res
