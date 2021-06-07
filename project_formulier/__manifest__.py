# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Project Formulier Base',
    'category': 'Website',
    'version': '1.0',
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'summary': '',
    'description': """
    main goal is get information from customer related to lead, quotation.
    1. Formulier record is created when lead is converted into opportunity.
    2. Add PF tab in opportunity, Task, Sale Order and also add create project formulier button in opportunity.
    3. Add buttons on opportunity for open online PF and form view of PF.
    4. Many fields filled from opportunity into PF record. like partner, address, mobile etc.
    5. Add project formulier tab on user form (many configuration), this values are useful for online pf operation.
    6. For the open online PF, user require PF ID and Access token.
    7. Back to edit and Back to opportunity link add on online PF for redirect on that.
    8. Upload many images on online pf(From Extra Images Tab), Also user can delete it.
    9. Upload many videos on online pf(From Videos Tab), Also user can delete it.
    10. Upload many Documents on online pf(From Documents Tab), Also user can delete it.
    11. Add many tabs on online PF and some are show based on some condition, like first phase is for opportunity data, and that phase only show when PF have 'opportunity' stage, there is total 3 phase, and 6 stages on PF, first stage is for get some details from customer, so ask some basic question on online pf, third phase is show when PF have created quotation and task.
    12. Online pf reload on click 'save' button.
    13. Streetview image add in 'overview' image field
    14. User can fill onlin form all fields, different type of fields.
    15. Add smart button on PF form view for show linked opportunity, sale order and task.
    16. Login user related PF records show in my account in website, user can open own PF record from my account.
    17. Dynamic value concept apply for online quote, user can get any field value on online quotation, (Quotation, opportunity, PF) => syntax => $(formulier:object.xxa_aa_name)
    18. Image fields updated from online PF.
    19. Add new tabs in edit media dialogue box on online quote page and show all images, documents and videos from linked PF records,  user also can select image from edit media dialogue box and put it in online quote.
    """,
    'depends': [
        'quote_print',
        'lead_category',
        'partner_salutation',
        'lead_source',
        'project',
        'website_form',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/crm_lead_view.xml',
        'views/project_formulier_view.xml',
        'views/res_users_view.xml',
        'views/access_assets.xml',
        'views/tabs_template.xml',
        'views/formulier_profile_template.xml',
        'views/formulier_media_template.xml',
        'views/opportunity_formulier_template.xml',
        'views/quote_formulier_template.xml',
        'views/task_formulier_template.xml',
        'views/main_formulier_template.xml',
        'views/website_template.xml',
        'views/snippets.xml',
        'report/formulier_task_stage_report.xml',
    ],
    'qweb': [
        'static/src/xml/wysiwyg.xml',
        ],
    'installable': True,
    'application': False,
}
