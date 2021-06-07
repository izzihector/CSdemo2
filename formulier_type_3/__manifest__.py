# -*- coding: utf-8 -*-

{
    'name': 'Formulier Three(PV)',
    'version': '14.0.1.0',
    'summary': '',
    'description': """
    1) new formulier type add, it's called intake PV.
    2) add some questions and images for opportunity stage on PF.
    3) Create quote from online PF, this is for salesman.
        - show some products based on some calculation in dropdown fields.
        - add images in product field dropdown on online PF.
        - user can get total amount and margin on online PF before create actual quote.
    4) add new url and page for create quote (you can called website quote), this is for customer(portal), simply create quotation based on some selected questions.
    5) add new page and show some questions (you can called website quote questions), this is also for customer(portal), this is for feedback about created website quote.
    6) add tabs design, next and previouse button and follow some rules.
    7) change opportunity stage after submit website quote and website quote questions.
    8) Add snippet for dynamic value for online quote.
    9) Add Task stage report for show all questions/answers of PF.
    """,
    'category': 'CRM',
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'depends': ['project_formulier',
                'project_formulier_quote',
                'formulier_quote_set_lines',
                'quote_print',
                'sale_margin',
                'sale_global_discounts',
            ],
    'data': [
            'security/ir.model.access.csv',
            'data/data.xml',
            'views/access_assets.xml',
            'views/project_formulier_view.xml',
            'views/formulier_quote_view.xml',
            'views/sale_order_view.xml',
            'views/opportunity_formulier_template.xml',
            'views/quote_formulier_template.xml',
            'views/task_formulier_template.xml',
            'views/online_formulier_quote.xml',
            'views/tabs_template.xml',
            'views/snippets.xml',
            'views/customer_question_template.xml',
            'views/customer_question_accessibility.xml',
            'views/customer_question_roof.xml',
            'views/customer_question_placement.xml',
            'views/customer_question_conclusion.xml',
            'views/customer_quote_formulier_data.xml',
            'views/customer_quote_formulier_energy.xml',
            'views/customer_quote_formulier_quotation_energy.xml',
            'views/customer_quote_formulier_summery.xml',
            'views/customer_quote_formulier_template.xml',
            'report/formulier_task_stage_report.xml',
        ],
    'installable': True,
    'application': False,
}
