# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Fill Salutation from email template',
    'version': '14.0.0.1',
    'category': 'CRM',
    'sequence': 1,
    'summary': '',
    'description': 
        """
            This module Allows to make automatic fill-up
            fields value of firstname , lastname, partner 
            salutation when lead create from email template.
        """,
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'depends': [
        'create_crm_lead', 'partner_salutation',
    ],
    'data': [],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
