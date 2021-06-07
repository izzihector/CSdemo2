# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Lead Category',
    'version': '14.0.1.0',
    'sequence': 4,
    'summary': 'Add Lead Category to Crm Lead',
    'description': """Add Lead Category to Crm Lead. and Send Lead Source 
    and Lead Category To Quotation From Opportunity.
    There is some Lead Category with this module.
    1. vloer
    2. muur
    3. dak
    4. PV
    5. MIX
    """,
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['lead_source','sale_crm'],
    'data': [
            'security/ir.model.access.csv',
            'data/lead_category_data.xml',
            'views/crm_lead_view.xml',
            ],
    'installable': True,
    'application': False,
}
