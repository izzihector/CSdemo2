# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    xaa_aa_order_watt_piek = fields.Float(string="Order Watt Peak")
    xaa_aa_order_iso = fields.Float(string="Order ISO")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['xaa_aa_order_watt_piek'] = ", sum(l.xaa_aa_total_watt_piek) as xaa_aa_order_watt_piek"
        fields['xaa_aa_order_iso'] = ",sum(l.xaa_aa_total_iso) as xaa_aa_order_iso"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
