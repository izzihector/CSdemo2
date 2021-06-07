# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
{
    'name': 'Product Type',
    'version': '14.0.1.0',
    'summary': 'Add Product Type field on Product,Sale order line and sale report',
    'description': """Add Product Type field on Product and sal order line, also add it in report""",
    'category': 'Product',
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'depends': ['product','sale'],
    'data': [
            'view/product_view.xml',
            ],
    'installable': True,
    'application': False,
}
