# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'Base Module for Email Templates',
    'version': '14.0.1.0.0',
    'category': 'CRM',
    'sequence': 1,
    'summary': '',
    'description':
        """
        Configuration:
            Activate Lead group from crm configueation setting.
        Features:
            1. This module enables automatic lead creation in v14 community from 
               fetched email's body content using the server action named
               Create lead from fetched email's body(created by this module).
               This server action need to be used in fetchmail configuration
               to enable automatic lead creation from the body content.
            2. This module also sends an email to the
               generated lead's email address if there is any active outgoing 
               email server configured, otherwise it will have those emails in
               exception state under 'Setting/Technical/Email/Emails', 
               which then can be send manually when any outgoing email server
               is configured.
            3. Email Description tab added in lead/opportunity form view
               which store email data of fetched lead mail.
            4. Heer, Mevrouw, Familie partner title data added by data files
            5. New menu Lead Email Lead Category and Lead Email Lead Source added
               under CRM configuration menu
            7. Lead Source of Lead gets updated by fetched lead's company mail
               if configured Lead Email Lead Source's Domain matched.
            6. Lead Category field gets updated by Lead Email Lead Category's Lead
               Category which has matched Lead Email Lead Source.
            7. Tags get updated if matched Lead Email Lead Category's Lead
               category has tags
        """,
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'support': 'arosman@aardug.nl',
    'depends': [
        'crm', 'mail', 'lead_category', 'lead_source', 'sales_team', 'mail_add_action'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_action_rule_data.xml',
        'data/server_action_data.xml',
        'data/res_partner_title_data.xml',
        'views/crm_lead_tree_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
