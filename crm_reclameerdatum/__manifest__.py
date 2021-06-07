# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
{
    'name': 'Reclameerdatum On Lead / Opportunity',
    'version': '14.0.1.0',
    'summary': 'Add EC Reclameerdatum in Lead / Opportunity',
    'description': """Add Reclameerdatum in Lead / Opportunity, also add some filters""",
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['create_crm_lead','lead_source','opportunity_meeting'],
    'data': [
            'data/lead_reclameer_data.xml',
            'views/crm_lead_reclameerdatum.xml',
            ],
    'installable': True,
    'application': False,
}
