# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Mail send on convert lead to opportunity',
    'version': '14.0.1.0',
    'summary': '',
    'description': """
        1). Send different Mail format(template) to customer on Convert lead to opportunity.
        2). Add fields like lead source, lead category, email template and zip range in new model (opportunity.mail.configure),
        3). Based on some comparision of fields, get email template from model(opportunity.mail.configure) and using that template mail send to customer
        """,
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'depends': ['lead_source', 'lead_category'],
    'data': [
            'security/ir.model.access.csv',
            'views/crm_lead_view.xml',
            ],
    'installable': True,
    'application': False,
}
