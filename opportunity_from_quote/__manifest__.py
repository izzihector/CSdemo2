# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': "Opportunity from Quote",
    'summary': """
                Create New Opportunity from Quotation
            """,
    'description': """
        This module  create opportunity On quotation form if opportunity is not
        set on quotation
        Some of the features are :
        1. When you Send quotation at that time if opportunity is not created, then it will
        create opportunity and move it to send quote stage.
        2. When you confirm Quotation at that time it also set opportunity to won.
        3. And if quotation cancel then it will set opportunity to lost. """,
    'author': 'Aardug',
    'website': 'http://www.aardug.nl/',
    'support': 'info@aardug.nl',
    'category': 'Sale',
    'version': '14.0.0.1',
    'depends': ['crm',
                'sale_crm',
                'project_formulier',
                'partner_salutation',
                'custom_header_footer',
                'lead_source',
                'lead_category'],
    'data': [
        'views/sale_view.xml',
        'data/crm_stage.xml',
        ],
    'installable': True,
    'application': False,
}
