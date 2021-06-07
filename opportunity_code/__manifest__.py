# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Sequential Code for Opportunity',
    'summary': 'Create Sequence Code for Lead/Opportunity',
    'description': """ Create Sequence Code for New and existing 
    Lead/Opportunity.""",
    'version': '14.0.0.1',
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['crm'],
    'data': [
        'data/opportunity_sequence.xml',
        'views/opportunity_view.xml',
    ],
    'installable': True,
    "pre_init_hook": "create_code_equal_to_id",
    "post_init_hook": "assign_old_sequences",
}
