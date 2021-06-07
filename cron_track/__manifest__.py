# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Cron Track',
    'version': '14.0.1.0',
    'summary': 'Cron Track',
    'category': '',
    'description': """"
         - This Module is Usefull for track all the Cron.
        - When Run any cron if that cron is failed some reason than you can see that error message.
        - you can also see the how many time cron is executed and how many time cron is failed.
    """,
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'http://www.caretit.com',
    'depends': ['base','mail'],
    'data': [
        'data/cron_status_email_template.xml',
        'security/ir.model.access.csv',
        'views/cron_track_views.xml',
        'views/cron_track_log_view.xml',
        'views/ir_cron_view.xml',
        'report/cron_track_report.xml',
        'report/cron_report.xml'
    ],
    'qweb': [],
    'images': ['static/description/banner.jpg'],
    'price': 19.00,
    'currency': 'USD',
}
