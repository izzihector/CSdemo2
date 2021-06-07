# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Lead Source',
    'version': '14.0.1.0',
    'sequence': 4,
    'summary': 'Add Lead Source to Crm Lead',
    'description': """ Add Lead Source to Crm Lead. and Send Lead Source to
    quotation when create from Lead/Opportunity.""",
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['sale_crm'],
    'data': [
            'security/ir.model.access.csv',
            'views/crm_lead_view.xml',
            ],
    'installable': True,
    'application': False,
}
