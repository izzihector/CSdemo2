# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Custom Header Footer',
    'version': '14.1',
    'category': 'Reports',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'description': """
        1) Create Trademark record on company for report and sale order configuration.
        2) Trademark dropdown field add in partner,crm,sale order,invoice, stock.
        3) Change header/footer image in reports from selected trademark on record.
        4) Pricelist get from trademark field in sale order.
        5) Add analytical account on sale order from trademark.
        6) Add email sent and reply to on sended mail on sale order.
        7) Trademark also helpfull for generate short code on sale order.
    """,
    'depends': ['sale_crm', 'account'],
    'data': [
            'security/ir.model.access.csv',
            'views/ir_sequence_view.xml',
            'data/paperformate_data.xml',
            'views/view_res_company.xml',
            'views/view_models.xml',
            'report/ec_layout.xml',
            'report/sale_invoice_reports.xml',
        ],
    'installable': True,
    'application': False,
}
