# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Formulier Quote Set Lines',
    'version': '14.0.1.0',
    'summary': '',
    'description': """ """,
    'category': 'Sale',
    'author': 'Aardug, Arjan Rosman',
    'website': 'arosman@aardug.nl',
    'depends': [
            'sale',
            'opportunity_from_quote',
        ],
    'data': [
            'security/ir.model.access.csv',
            'data/data.xml',
            'views/sale_configure_view.xml',
            'wizard/sale_config_wizard.xml',
            ],
    'installable': True,
    'application': False,
}
