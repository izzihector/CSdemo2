# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Field Service Resource',
    'summary': 'Field Service and Project Resource Bridge',
    'description': '''
    ''',
    'author': 'Aardug',
    'website': 'http://www.aardug.nl/',
    'support': 'info@aardug.nl',
    'category': 'Resource',
    'version': '14.0.1.0',
    'depends': ['industry_fsm', 'project_resource', 'sale_timesheet'],
    'data': [
        'views/task.xml',
        'views/task_data.xml'
    ],
    'application': False,
}
