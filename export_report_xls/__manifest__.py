# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Export Report for Partner & Invoice',
    'category': 'Hidden',
    'description': """Add menus to export report for the Partner and Invoice in excel file""",
    'version': '14.0.1.0',
    'depends':['account','sale'],
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'data' : [
        'security/ir.model.access.csv',
        'views/partner_invoice_view.xml',
        'wizard/partner_wizard.xml',
        'wizard/account_invoice_wizard.xml',
    ],
    'auto_install': False,
    'installable': True,
}
