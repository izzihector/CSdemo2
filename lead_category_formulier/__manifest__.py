# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Lead Category Formulier',
    'version': '14.0.0.1',
    'summary': 'Add dropdown(Question Type) field In Lead Category',
    'description': """
        1) Add Selection(Question Type) field In Lead Category.
        2) Question type selection field get dynamically all options from project formulier question type field.
        3) lead fill question type field from category field.
        """,
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'depends': ['lead_category', 'project_formulier'],
    'data': [
                'views/crm_lead_view.xml',
            ],
    'installable': True,
    'application': False,
}
