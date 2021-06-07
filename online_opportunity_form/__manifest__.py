# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Online Opportunity Form',
    'version': '14.0.0.0.1',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'summary': '',
    'description': """
        1. Design opportunity form on website for create opportunity -> PF , this is useful for portal user.
        2. Add 'Opportunity' menu on website for redirect on opportunity form. it's put after my account menu.
        3. on opportunity form some fields get from login user form,(lead category, lead source and question type)
    """,
    'depends': ['project_formulier','lead_category','partner_salutation'],
    'data': [
        'data/crm_stage_data.xml',
        'views/access_assets.xml',
        'views/opportunity_template.xml'
    ],
    'qweb': [],
    'installable': True,
    'application': False,
}
