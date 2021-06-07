# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Base project formulier quote',
    'version': '14.0.1.0',
    'summary': '',
    'description': """ This module providing common configuration for 
        website quote create for PV and ISO type formulier""",
    'category': 'Sale',
    'author': 'Aardug, Arjan Rosman',
    'website': 'arosman@aardug.nl',
    'depends': ['project_formulier',
                'sale_management',
                'quote_calculation',
                'website',
                # 'website_portal_sale',
                # 'ob_website_calender_booking',
                ],
    'data': [
            'security/ir.model.access.csv',
            'data/data.xml',
            'data/houseinfo_data.xml',
            'data/roof_info_data.xml',
            'views/access_assets.xml',
            'views/formulier_config_settings_view.xml',
            'views/res_user_view.xml',
            'views/project_formulier_view.xml',
            'views/product_view.xml',
            'views/sale_order_view.xml',
            'views/customer_quote_template.xml',
            'views/customer_quotation_question_template.xml',
            'views/sale_portal_template.xml',
            ],
    'installable': True,
    'application': False,
}
