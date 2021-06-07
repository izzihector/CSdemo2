# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

import datetime
from odoo import api, fields, models, _
from odoo.exceptions import Warning, UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

_MAP_FIELDS_DATE=[]
_MAP_FIELDS_DATETIME = ['date_last_stage_update','close_date','assign_date','create_date']
_MAP_COLORS = {
    'orange': 8,
    'red': 9,
    'green': 7,
    'purple': 6,
    'yellow': 5,
    'blue': 4,
}

class HelpdeskSupport(models.Model):
    """ Helpdesk Support """

    _inherit = 'helpdesk.ticket'

    xaa_aa_remainder_mail = fields.Boolean(string='FollowUp Mail')
    xaa_aa_warning_mail = fields.Boolean(string='Reminder Mail')

    def write(self, vals):
        if 'stage_id' in vals:
            vals.update(xaa_aa_remainder_mail=False,
                        xaa_aa_warning_mail=False)
        return super(HelpdeskSupport,self).write(vals)

    @api.model
    def send_mail(self, custom):
        ''' send mail to opportunity customer based on helpdesk stage configuration'''

        Mail = self.env['mail.mail']
        Fields = ['subject', 'body_html', 'email_from', 'email_to', 'partner_to', 'email_cc',  'reply_to', 'attachment_ids', 'mail_server_id']
        template = self.env['mail.compose.message'].generate_email_for_composer(
            custom.template_id.id, self.id, Fields)
        vals = {'auto_delete': True,
                'email_to': self.email,
                'subject': template.get('subject'),
                'body_html': template.get('body'),
                'email_cc': custom.xaa_aa_template_id.email_cc
                }
        mail_id = Mail.create(vals)
        self.message_post(body=_('sent mail is %s.') % (mail_id.body_html,))
        mail_id.send()
        return True 

    def compare_date(self, date, after_before, real_date):
        duration, unit = date.split('_')
        if(unit == "m"):
            return real_date + datetime.timedelta(minutes=int(duration))
        hours = int(duration) if unit == "h" else int(duration) * 24
        hours = hours * -1 if after_before == 'before' else hours * 1
        return real_date + datetime.timedelta(hours=hours)

    @api.model
    def email_send_stages(self):
        """ This cron job send mail to customer according configuration on helpdesk stage"""

        stage_custom_ids = self.env['helpdesk.stage.custom'].search([
            ('xaa_aa_send_mail','=',True),('xaa_aa_helpdesk_stage_id','!=',False)])
        for stage in stage_custom_ids:
            if stage.xaa_aa_mail_action == 'remainder':
                rec_ids = self.search([
                    ('stage_id', '=', stage.xaa_aa_helpdesk_stage_id.id),
                    ('remainder_mail','=',False)],)
            else:
                rec_ids = self.search([
                    ('stage_id', '=', stage.xaa_aa_helpdesk_stage_id.id),
                    ('warning_mail','=',False)],)
            when = stage.xaa_aa_action_when
            field = stage.xaa_aa_action_perform
            for rec in rec_ids:
                try:
                    value = getattr(rec, field) if hasattr(rec, field) else False
                    if value:
                        if field in _MAP_FIELDS_DATETIME:
                            date = datetime.datetime.strptime(value.strftime('%Y-%m-%d %H:%M:%S'), DEFAULT_SERVER_DATETIME_FORMAT)
                            date_to_compare = self.compare_date(stage.xaa_aa_action_time, when, date)
                            current_date = datetime.datetime.now()
                        else:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                            date_to_compare = self.compare_date(stage.xaa_aa_action_time, when, date)
                            current_date = datetime.date.today()
                        if ((date >= current_date >= date_to_compare and when == "before") or
                            (when == "after" and current_date >= date_to_compare)):
                            if stage.xaa_aa_mail_action == 'remainder':
                                rec.send_mail(stage)
                                rec.xaa_aa_remainder_mail = True
                            if stage.xaa_aa_mail_action=='warning':
                                rec.send_mail(stage) 
                                rec.xaa_aa_warning_mail = True
                except Exception as e:
                    _logger.error("Error in record <%s>, so skipped this record to fix mail issue ", rec.id)
                    continue

    def read(self, fields=None, load='_classic_read'):
        ''' Add color in helpdesk kanban records based on helpdesk stage configuration'''

        records = super(HelpdeskSupport, self).read(fields=fields, load=load)
        helpdesk_stage = self.env['helpdesk.stage']
        def compare_date(date, after_before, real_date):
            duration, unit = date.split('_')
            if(unit == "m"):
                return real_date + datetime.timedelta(minutes=int(duration))
            hours = int(duration) if unit == "h" else int(duration) * 24
            hours = hours * -1 if after_before == 'before' else hours * 1
            return real_date + datetime.timedelta(hours=hours)
        for rec in records:
            stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
            helpdesk_browse = helpdesk_stage.browse(stage_id)
            if rec.get('color') in [4,5,6,7,8,9]: rec['color'] = 0
            for custom in helpdesk_browse.xaa_aa_custom_ids:
                when, field = custom.xaa_aa_action_when, custom.xaa_aa_action_perform
                value = rec.get(field)
                if value:
                    if field in _MAP_FIELDS_DATETIME:
                        date = datetime.datetime.strptime(value.strftime('%Y-%m-%d %H:%M:%S'), DEFAULT_SERVER_DATETIME_FORMAT)
                        date_to_compare = compare_date(custom.xaa_aa_action_time, when, date)
                    else:
                        date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                        date_to_compare = compare_date(custom.xaa_aa_action_time, when, date)
                    current_date = datetime.datetime.now()
                    if ((date >= current_date >= date_to_compare and when == "before") or
                        (when == "after" and current_date >= date_to_compare)):
                        rec['color'] = _MAP_COLORS[custom.xaa_aa_action_color]
        return records


class HelpdeskStageConfig(models.Model):

    _inherit = "helpdesk.stage"

    xaa_aa_custom_ids = fields.One2many('helpdesk.stage.custom', 'xaa_aa_helpdesk_stage_id', string='Kanban Custom')

class HelpdeskStageCustom(models.Model):
    _name = "helpdesk.stage.custom"
    _order = 'xaa_aa_priority desc'
    _description = "Helpdesk Stage Lines"

    xaa_aa_priority = fields.Integer(string='Priority', default=1, required=True)
    xaa_aa_send_mail = fields.Boolean('Send mail')
    xaa_aa_template_id = fields.Many2one('mail.template', string='Template')
    xaa_aa_helpdesk_stage_id = fields.Many2one('helpdesk.stage', string='Stage')
    xaa_aa_action_when = fields.Selection([
                                    ('before','Before'),
                                    ('after','After')],
                                    string='Before/After', required=True)
    xaa_aa_mail_action = fields.Selection([
                                    ('remainder','FollowUp Mail'),
                                    ('warning','Reminder Mail')],
                                     string='Mail Action')
    xaa_aa_action_time = fields.Selection([
                                    ('1_m','1 Minute'),
                                    ('5_m','5 Minutes'),
                                    ('15_m','15 Minutes'),
                                    ('30_m','30 Minutes'),
                                    ('1_h','1 Hour'),
                                    ('2_h','2 Hours'),
                                    ('4_h','4 Hours'),
                                    ('8_h','8 Hours'),
                                    ('1_d','1 Day'),
                                    ('2_d','2 Days'),
                                    ('3_d','3 Days'),
                                    ('4_d','4 Days'),
                                    ('5_d','5 Days'),
                                    ('7_d','7 Days'),
                                    ('10_d','10 Days'),
                                    ('20_d','20 Days'),
                                    ('30_d','30 Days'),
                                    ('180_d','180 Days'),
                                    ('365_d','365 Days'),],
                                    string='Time', required=True)
    xaa_aa_action_color = fields.Selection([('orange', 'Orange'),
                                    ('red','Red'),
                                    ('green','Green'),
                                    ('purple','Purple'),
                                    ('yellow','Yellow'),
                                    ('blue','Blue')],
                                    string='Colors', required=True)
    xaa_aa_action_perform = fields.Selection([('date_last_stage_update', 'Last Stage Update'),
                                       ('assign_date', 'Assign Date'),
                                       ('close_date', 'Close date'),
                                       ('create_date', 'Created on')],
                                      string='Field', required=True)

    @api.constrains('xaa_aa_action_time', 'xaa_aa_action_perform')
    def _check_action_time(self):
        if self.xaa_aa_action_perform in _MAP_FIELDS_DATE and self.xaa_aa_action_time in ['1_m','5_m','15_m','30_m','1_h','2_h','4_h','8_h']:
            raise Warning(_('Misconfiguration, check Field and Time.'))
