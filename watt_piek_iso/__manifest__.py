# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Watt Peak and ISO',
    'version': '14.0.1.0',
    'summary': 'Add Watt Peak and ISO in Product Template',
    'description': 
        """
        Features: 
          1.  This Module allows to you add Watt Peak and ISO Values
              on Product template.
          2.  And Later Used this Values on Sale order line .
          3.  Based On Product's qty and Watt Peak and ISO Values
              calculate Watt Peak and ISO values Of SO. 
        """,
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'depends': ['sale'],
    'data': [
            'views/product_sale.xml',
            ],
    'installable': True,
    'application': False,
}
