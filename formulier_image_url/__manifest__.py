# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name' : 'Image From URL',
    'version': '14.0.0.1',
    'summary': 'Upload image from URL',
    'category': 'Website',
    'description': """Upload image from URL in website and backend""",
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'depends': ['project_formulier', 'crm'],
    'data': [
             'views/templates.xml',
             'views/views.xml',
            ],
    'installable': True
}
