# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import http
from odoo.http import request


class QuoteController(http.Controller):

    @http.route(['/order/getCalculations'], type='json', auth="public", website=True, csrf=False)
    def get_sale_calculations(self, sale_id):
        order = request.env['sale.order'].browse(sale_id)
        if order:
            return {'xaa_aa_watt_piek': order.xaa_aa_watt_piek,
                    'xaa_aa_jaaropbrengst_prijs_van': order.xaa_aa_jaaropbrengst_prijs_van,
                    'xaa_aa_jaaropbrengsten': "%.2f" % order.xaa_aa_jaaropbrengsten,
                    'xaa_aa_rendement': order.xaa_aa_rendement,
                    'xaa_aa_verwachte_terugverdientijd': "%.2f" % order.xaa_aa_verwachte_terugverdientijd,
                    'xaa_aa_totale_verwachte_jaaropbrengst_van_de': order.xaa_aa_totale_verwachte_jaaropbrengst_van_de,
                    'xaa_aa_related_amount_untaxed': "%.2f" % order.xaa_aa_related_amount_untaxed,
                    'currency': order.pricelist_id.currency_id.symbol}
        else:
            return {}
