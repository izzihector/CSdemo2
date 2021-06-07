# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'CRM Opportunity kanban Customization',
    'version': '14.0.1.0.1',
    'category': 'CRM',
    'sequence': 2,
    'summary': 'CRM Opportunity kanban view count display',
    'description':
        """
           CRM Opportunity kanban view count display
        """,
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['crm'],
    'data': [
            'views/crm_lead_views.xml',
            ],
    'installable': True,
    'application': False,
    'auto_install': False,
}