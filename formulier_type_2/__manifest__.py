# -*- coding: utf-8 -*-

{
    'name': 'Formulier Two(ISO)',
    'version': '14.0.1.0',
    'summary': '',
    'description': """
        1) new formulier type add, it's called ISO.
        2) add some questions and images for opportunity stage on PF.
        3) Create quote from online PF, this is for salesman.
            - show some products based on some calculation in dropdown fields.
            - add images in product field dropdown on online PF.
            - user can get total amount and margin on online PF before create actual quote.
        4) add new url and page for create quote (you can called website quote), this is for customer(portal), simply create quotation based on some selected questions.
        5) add new page and show some questions (you can called website quote questions), this is also for customer(portal), this is for feedback about created website quote.
        6) add tabs design, next and previouse button and follow some rules.
        7) change opportunity stage after submit website quote and website quote questions.
    """,
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'depends': ['project_formulier',
                'project_formulier_quote',
                'formulier_quote_set_lines',
                'quote_print',
                'sale_margin',
                'sale_global_discounts',],
    'data': [
            'security/ir.model.access.csv',
            'data/data.xml',
            'views/access_assets.xml',
            'views/project_formulier_view.xml',
            'views/formulier_quote_view.xml',
            'views/product_template_view.xml',
            'views/opportunity_formulier_template.xml',
            'views/quote_formulier_template.xml',
            'views/task_formulier_template.xml',
            'views/online_formulier_quote.xml',
            'views/tabs_template.xml',
            'views/customer_quote_formulier_construction_year.xml',
            'views/customer_quote_formulier_cavity_thickness.xml',
            'views/customer_quote_formulier_home.xml',
            'views/customer_quote_formulier_extension.xml',
            'views/customer_quote_formulier_template.xml',
            'views/customer_question_accessibility.xml',
            'views/customer_question_property_design.xml',
            'views/customer_question_closing.xml',
            'views/customer_question_photos.xml',
            'views/customer_question_template.xml',
            ],
    'installable': True,
    'application': False,
}
