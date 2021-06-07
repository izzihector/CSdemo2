# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'CRM Activity Log',
    'version': '14.0.0.1',
    'summary': 'CRM Activity Log Create Based On Lead',
    'description': """Create CRM Activity Log When Stage changes 
     on CRM Lead/Opportunity""",
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'depends': ['crm'],
    'data': [
            'security/ir.model.access.csv',
            'views/activity_log_view.xml',
            ],
}
