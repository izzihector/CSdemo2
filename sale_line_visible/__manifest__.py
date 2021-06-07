# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name' : 'Sale Line Visible',
    'version': '14.0.0.0',
    'category': 'Sale',
    'description': """
        1. Add Not Visible field on product, sale order line and invoice line.
        2. Based on Not visible field, hide lines in sale and invoice reports, also online version.
     """,
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl',
    'depends': ['account','sale_management','quote_print'],
    'data': [
             'views/sale_order_view.xml',
             'views/sale_report.xml',
             'views/invoice_report.xml',
            ],
}
