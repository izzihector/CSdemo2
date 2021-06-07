# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'CRM Lead Activity Customization',
    'version': '14.0.1.0.1',
    'category': 'CRM',
    'sequence': 2,
    'summary': 'CRM lead actiity displays on the topbar',
    'description':
        """
           CRM lead actiity displays on the topbar
        """,
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['crm'],
    'data': [
            'views/assets.xml',
            ],
    'qweb': [
        'static/src/xml/systray.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}