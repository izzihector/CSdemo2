# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Opportunity Name',
    'version': '14.0.1.0',
    'summary': 'Convert Lead to Opportunity with Customer Details',
    'description': """When Convert Lead To Opportunity Then Customer name, city,
    street Fields Merge in Name Field""",
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'depends': ['crm','base_address_extended','lead_category'],
    'data': [
            'views/crm_lead_view.xml',
            ],
    'installable': True,
    'application': False,
}