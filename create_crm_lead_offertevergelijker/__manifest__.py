# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'Offertevergelijker Template Parser for CRM Lead',
    'version': '14.0.1.0.1',
    'category': 'CRM',
    'sequence': 2,
    'summary': 'Offertevergelijker Template Parser For Lead  Update.',
    'description':
        """
            1. This module parse Offertevergelijker mail template
               and build clean data to update lead's record 
               created by fetching Offertevergelijker mail from configured 
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
