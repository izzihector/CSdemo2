# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'New Lead Created - Welcome Email Template.',
    'version': '14.0.1.0.0',
    'category': 'CRM',
    'summary': 'Lead - Welcome Email!',
    'description': 
        """
            If set in crm kanban stage lines template fields. then send Welcome Email.
        """,
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['mail'],
    'data': ['data/lead_welcome.xml'],
    'installable': True,
    'application': False,
}
