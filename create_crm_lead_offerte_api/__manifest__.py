# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Offerte Api for CRM Lead',
    'version': '14.0.1.0',
    'category': 'Customer Relationship Management',
    'sequence': 3,
    'summary': 'Lead Create From Offerte API',
    'description': """ """,
    'website': 'http://www.aardug.nl/',
    'author': 'Aardug',
    'support': 'info@aardug.nl',
    'depends': [
        'base_setup',
        'crm',
        'website_crm_partner_assign',
        'lead_category',
        'lead_source',
        'partner_salutation',
        ],
    'data': [
        'views/res_config.xml',
        'views/crm_lead_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
