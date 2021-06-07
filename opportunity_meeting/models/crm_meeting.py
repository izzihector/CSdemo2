# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from datetime import timedelta, datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.http import request

class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    xaa_aa_formulier_id = fields.Many2one('question.formulier', string='Project Formulier')
    xaa_aa_lead_category = fields.Many2one("lead.category", string="Lead Category", index=True)
    xaa_aa_phone = fields.Char(string='Phone')

    @api.model
    def _get_public_fields(self):
        return self._get_recurrent_fields() | self._get_time_fields() | self._get_custom_fields() | {
            'id', 'active', 'allday',
            'duration', 'user_id', 'interval',
            'count', 'rrule', 'recurrence_id', 'show_as', 'xaa_aa_lead_category'}

    def project_formulier_view(self):
        return {
            'name': 'Project Formulier',
            'res_model': 'question.formulier',
            'type': 'ir.actions.act_window',
            'res_id': self.xaa_aa_formulier_id.id,
            'context': {},
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('project_formulier.view_project_formulier_form').id,
            'target': 'current',
            }

    def opportunity_form(self):
        return {
            'name': 'Opportunity',
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'res_id': self.opportunity_id.id,
            'context': {},
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('crm.crm_lead_view_form').id,
            'target': 'current',
            }

    def project_formulier_online(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/project-formulier/'+str(self.xaa_aa_formulier_id.id)+'/'+str(self.xaa_aa_formulier_id.xaa_aa_pf_access),
            'target': 'self',
            }

    def save_calendar_data(self):
        vals = {
            'name': self.name,
            'partner_ids': [(6, 0, self.partner_ids.ids)] or False,
            'start_date': self.start_date,
            'stop_date': self.stop_date,
            'allday': self.allday,
            'description': self.description,
            'duration': self.duration,
            'start': self.start,
            'categ_ids': [(6, 0, self.categ_ids.ids)] or False,
            'alarm_ids': [(6, 0, self.alarm_ids.ids)] or False,
            'location': self.location,
            'privacy': self.privacy,
            'show_as': self.show_as,
            'recurrency': self.recurrency,
            'interval': self.interval,
            'rrule_type': self.rrule_type,
            'end_type': self.end_type,
            'count': self.count,
            'mo': self.mo,
            'tu': self.tu,
            'we': self.we,
            'th': self.th,
            'fr': self.fr,
            'sa': self.sa,
            'su': self.su,
            'attendee_ids': [(6, 0, self.attendee_ids.ids)] or False,
            'user_id': self.user_id and self.user_id.id,
            'xaa_aa_lead_category': self.xaa_aa_lead_category,
            'xaa_aa_phone': self.xaa_aa_phone,
            'recurrence_update': self.recurrence_update,
        }
        self.write(vals)
        return {
            'name': 'Meetings',
            'res_model': 'calendar.event',
            'type': 'ir.actions.act_window',
            'context': {},
            'view_type': 'calendar',
            'view_mode': 'calendar',
            'view_id': self.env.ref('calendar.view_calendar_event_calendar').id,
            'target': 'current',
            }


class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_meeting_date = fields.Datetime(string="Meeting date", help="Customer Meeting Start Date")
    xaa_aa_note = fields.Text('Notes')
    xaa_aa_streetview_link = fields.Char(string='Streetview Link', compute='_compute_streetview_link', store=True)
    xaa_aa_meeting_dur = fields.Selection([
        ('30','30'),
        ('45','45'),
        ('60','60'),
        ('75','75'),
        ('90','90'),
        ('105','105'),
        ('120','120'),
        ],string='Duration', default='45')

    @api.depends('partner_id.partner_longitude','partner_id.partner_latitude','partner_id')
    def _compute_streetview_link(self):
        apikey = self.env['ir.config_parameter'].sudo().get_param('base_geolocalize.google_map_api_key')
        for rec in self:
            if apikey and rec.partner_id:
                rec.partner_id.geo_localize()
                if rec.partner_id.partner_latitude and rec.partner_id.partner_longitude:
                    url = 'https://maps.googleapis.com/maps/api/streetview?size=1500x900&location='+str(rec.partner_id.partner_latitude)+','+str(rec.partner_id.partner_longitude)+'&heading=360&pitch=-0.76&key='+apikey
                    rec.xaa_aa_streetview_link = url

    def create_meeting(self):
        current_date = datetime.now()
        if self.xaa_aa_meeting_date < datetime.now():
            raise UserError(_('Meeting date is always greater than present date.'))
        if self.user_id:
            custName = ''
            address = ''
            phone = ''
            mobile = ''
            note = ''
            streetview_link = ''
            formulier = ''
            formulier_alias = ''
            customer = self.partner_id
            if self.xaa_aa_meeting_dur:
                stop = self.xaa_aa_meeting_date + timedelta(minutes=int(self.xaa_aa_meeting_dur))
            else:
                stop = self.xaa_aa_meeting_date + timedelta(minutes=45)
            self.xaa_aa_opportunity_by = self.user_id.id
            if self.xaa_aa_meeting_date:
                self.xaa_aa_opportunity_date = self.xaa_aa_meeting_date
            if customer:
                if customer.name:
                    custName = '\n'.join([_('Customer Name:'), customer.name])
                addressVal = '\n'.join(
                    [x for x in [
                        customer.street,
                        customer.street2,
                        customer.city,
                        customer.zip,
                        customer.state_id.name if customer.state_id else '',
                        customer.country_id.name if customer.country_id else '']
                     if x])
                if addressVal:
                    address = '\n'.join([_('Address:'), addressVal])
                if customer.phone:
                    phone = '\n'.join([_('Customer Phone:'), customer.phone])
                if customer.mobile:
                    mobile = '\n'.join([_('Customer Mobile:'), customer.mobile])
            if self.xaa_aa_note:
                note = '\n'.join([_('Opportunity Note:'), self.xaa_aa_note])
            if self.xaa_aa_streetview_link:
                streetview_link = '\n'.join([_('Location:'), self.xaa_aa_streetview_link])

            if self.xaa_aa_formulier_id:
                self.xaa_aa_formulier_id.xaa_aa_date_opportunity = self.xaa_aa_meeting_date.date()
                formulierId= self.xaa_aa_formulier_id
                formulierLink = request.httprequest.url_root + 'project-formulier/'+str(formulierId.id)+'/'+str(formulierId.xaa_aa_pf_access)
                formulier = '\n'.join([_('Formulier Url:'), formulierLink])
                if self.xaa_aa_formulier_id.xaa_aa_formulier_alias and self.xaa_aa_formulier_id.xaa_aa_formulier_alias.alias_domain:
                    alias_name = self.xaa_aa_formulier_id.xaa_aa_formulier_alias.alias_name +'@'+ self.xaa_aa_formulier_id.xaa_aa_formulier_alias.alias_domain
                    formulier_alias = '\n'.join([_('Alias email:'), alias_name])

            description = '\n\n'.join(
                [x for x in [custName, address, phone, mobile, note, streetview_link, formulier, formulier_alias] if x])
            meeting = {'name': self.name,
                       'start': self.xaa_aa_meeting_date,
                       'stop': stop,
                       'opportunity_id': self.id,
                       'xaa_aa_lead_category': self.xaa_aa_lead_category.id or False,
                       'xaa_aa_phone': self.phone or self.mobile,
                       'xaa_aa_formulier_id': self.xaa_aa_formulier_id.id or False,
                       'user_id': self.user_id and self.user_id.id or self.env.user.id,
                       'description': description}

            if self.user_id and self.user_id.partner_id:
                meeting.update({'partner_ids': [[6, False, [self.user_id.partner_id.id]]],
                                'user_id': self.user_id.id})
            self.env['calendar.event'].create(meeting)

            activityType = self.env['mail.activity.type'].search([
                ('name', '=', 'Bezoekverslag maken')], limit=1)
            if not activityType.ids:
                activityType = self.env['mail.activity.type'].search([
                    ('category', '=', 'meeting')], limit=1)
            stage_id = self.env.ref('opportunity_meeting.stage_lead_appoinment', False)
            if not stage_id:
                stage_id = self.env['crm.stage'].search([('name','in',['Appointment','Afspraak'])], limit=1)
            if stage_id:
                self.stage_id = stage_id.id
            model = self.env['ir.model'].search([('model', '=', 'crm.lead')], limit=1)
            if model and activityType:
                activity = self.env['mail.activity'].create({
                                 'res_name': self.name,
                                 'activity_type_id': activityType.id,
                                 'summary': activityType.name,
                                 'note': self.xaa_aa_note,
                                 'user_id': self.user_id and self.user_id.id or self.env.user.id,
                                 'res_id': self.id,
                                 'res_model_id': model.id,
                                 'date_deadline': stop.date()
                            })
        else:
            raise UserError(_('Please Select Salesperson!!!.'))
