# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Add Calculation in Quote',
    'category': 'Sale',
    'summary': '''In Quotation add new tab Calculations and 
                display it in Quotation''',
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'support': 'arosman@aardug.nl',
    'version': '14.0.1.0',
    'description': """
        1. In Quotation add new tab Calculations Which is calculated default.
        2. Add new snippet for show calculation table in online quote.
        3. snippet can add in quote template and also directly drag an drop on online quote, you will get all calculated value in that snippet table.
    """,
    'depends': ['website', 'quote_print', 'watt_piek_iso'],
    'data': ['views/access_assets.xml',
             'views/quotation.xml',
             'views/calculation_snippet.xml',
            ],
    'installable': True,
    'application': False,
}
