# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': "customer_project_formulier",
    'version': '14.1',
    'summary': """ customer form work """,
    'description': """ """,
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'category': 'website',
    'depends': ['crm','website','base_address_extended', 'project_formulier_quote', 'formulier_type_4'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/assets.xml',
        'views/product_view.xml',
        'views/partner_view.xml',
        'views/email_form.xml',
        'views/customer_form_data.xml',
        'views/product_choice_form.xml',
        'views/customer_project_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}
