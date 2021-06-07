# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': "E-Mail alias on Sales order, Task and Opportunity",
    'version': '14.0.0.1',
    'category': 'Sale, Project, CRM',
    'summary': 'SO configure with alias and mail body in SO chatter',
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'support': 'arosman@aardug.nl',
    'depends': ['mail','sale', 'opportunity_code', 'project_task_code', 'project_formulier_code'],
    'data': [
        'views/sale_view.xml',
    ],
    'auto_install': False,
    'installable': True
}
