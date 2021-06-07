# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

# import babel
# from datetime import datetime, timedelta
from odoo import models
# from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTFORMAT
from odoo.tools import format_datetime


class Crm_Lead(models.Model):
    _inherit = 'crm.lead'


    def convert_date_based_on_lang(self):
        # meetingDate = datetime.strptime(self.xaa_aa_meeting_date, DTFORMAT)
        # meetingDate = datetime.strftime(self.xaa_aa_meeting_date, '%d %B %Y %H:%M:%S')
        meetingDate = format_datetime(self.env, self.xaa_aa_meeting_date, tz='CET', dt_format='medium')
        # print("MEttingdate!!!!!!!!!!!!!!!!!!!!!!!!!!!!!AAAAAAAAAAA", meetingDate)
        # print("typeeeeeeeeeeeeeeeeeeeeeee", type(meetingDate))
        # meetingDate.replace('Jan','jan')
        # meetingDate.replace('Feb','febr')
        # meetingDate.replace('Mar','mrt')
        # meetingDate.replace('Apr','apr')
        # meetingDate.replace('May','mei')
        # meetingDate.replace('Jun','juni')
        # meetingDate.replace('Jul','juli')
        # meetingDate.replace('Aug','aug')
        # meetingDate.replace('Sep','sep')
        # meetingDate.replace('Oct','okt')
        # meetingDate.replace('Nov','nov')
        # meetingDate.replace('Dec','dec')
        return meetingDate
