# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Formulier one',
    'version': '14.0.1.0',
    'summary': '',
    'description': """ 
        1. Add Formulier one option in question type field in crm.
        2. if user select this formulier one option in lead and convert it into opportunity, then they will see all images and fields related to this formulier type on PF form view and online version.
        3. PF show fields based on question type, there is many question type and many different fields.
        4. Create many custom snippets for online quote and that snippets values filled dynamically if quote is linked with PF record, like image snippet get image from PF record and other fields value.
        5. you can add custom snippet from quotation template or directly on online quote, both are working fine and show you latest values.
     """,
    'category': 'sale',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'depends': ['project_formulier'],
    'data': [
            'security/ir.model.access.csv',
            'data/data.xml',
            'views/access_assets.xml',
            'views/formulier_view.xml',
            'views/formulier_media_template.xml',
            'views/opportunity_formulier_template.xml',
            'views/quote_formulier_template.xml',
            'views/task_formulier_template.xml',
            'views/snippets.xml',
            ],
    'installable': True,
    'application': False,
}
