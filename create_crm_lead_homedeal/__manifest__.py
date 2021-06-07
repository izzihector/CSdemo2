# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'Homedeal Template Parser For CRM Lead',
    'version': '14.0.1.0.0',
    'category': 'CRM',
    'sequence': 7,
    'summary': 'Homedeal Template Parser For Lead Update.',
    'description':
        """
            1. This module parse Homedeal mail template
               and build clean data to update lead's record 
               created by fetching Homedeal mail from configured 
               incoming mail server.
        """,
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['create_crm_lead'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
