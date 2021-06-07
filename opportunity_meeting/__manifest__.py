# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Opportunity Meeting',
    'version': '14.0.0.1',
    'description': """
        This module usage is Create a calendar meeting to sync with Google.
        Add streetview map link on opportunity and appointment.
        Call button add in calendar event pop-up.
    """,
    'summary': 'Create a Opportunity Meeting For Calendar.',
    'category': 'CRM',
    'author': "Aardug",
    'website': "http://www.aardug.nl",
    'depends': ['crm', 'base_geolocalize', 'crm_sales_person_report','sale_custom'],
    'data': ['data/stage_and_activity_demo.xml',
             'views/assets.xml',
             'views/crm_meeting_view.xml',],
    'test': [],
    'qweb': [
        "static/src/xml/web_controller.xml",
    ],
    'installable': True,
    'auto_install': False,
}
