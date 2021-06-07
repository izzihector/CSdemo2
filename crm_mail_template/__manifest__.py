# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Crm mail template ',
    'version': '14.0.0.1',
    'summary': '',
    'author': 'Aardug, Arjan Rosman',
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'description': """
    """,
    'depends': ['mail', 'crm', 'project_formulier_quote', 'website', 'opportunity_meeting'],
    'data': [
            # 'data/calendar_data.xml',
            'data/crm_stage_data.xml',
            'data/remote_customer_requests_and_receives_mail_version.xml',
            'data/her_quote_sent_advisor.xml',
            'data/phone_video_call_reminder.xml',
            'data/customer_in_region_requests_and_receives.xml',
            'data/mail_template_h.xml',
            'data/mail_template_j.xml',
            'data/online_quote_confirmation.xml',
            'data/confirmation_visit_advisor.xml',
            'data/reminder_visit_advisor.xml',
            'data/reminder_supplement_living.xml',
            'data/confirmation_call_appointment_advisor.xml',
            'data/quotation_questions_completed.xml',
            'data/no_contact_3x_calls.xml',
            'data/future_memory_version.xml',
            'data/re_quote_x_number_of_days_valid.xml',
            'data/last_advisor_sent_quotation.xml',
            'data/customer_wants_more_information.xml',
            'data/system_cleaning.xml',
            'data/confirmation_of_work.xml',
            'views/customer_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}