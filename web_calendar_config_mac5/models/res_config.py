from odoo import api, fields, models

from odoo.addons.web_calendar_config_mac5.models.res_company import WEEKDAYS


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def _get_default_calendar_weekends(self):
        return self.env.user.company_id.calendar_weekends

    @api.model
    def _get_default_calendar_weeknumber(self):
        return self.env.user.company_id.calendar_weeknumber

    @api.model
    def _get_default_calendar_weekday(self):
        return self.env.user.company_id.calendar_weekday

    @api.model
    def _get_default_calendar_allow_overlap(self):
        return self.env.user.company_id.calendar_allow_overlap

    @api.model
    def _get_default_calendar_disable_dragging(self):
        return self.env.user.company_id.calendar_disable_dragging

    @api.model
    def _get_default_calendar_disable_resizing(self):
        return self.env.user.company_id.calendar_disable_resizing

    @api.model
    def _get_default_calendar_snap_minutes(self):
        return self.env.user.company_id.calendar_snap_minutes

    @api.model
    def _get_default_calendar_slot_minutes(self):
        return self.env.user.company_id.calendar_slot_minutes

    @api.model
    def _get_default_calendar_min_time(self):
        return self.env.user.company_id.calendar_min_time

    @api.model
    def _get_default_calendar_max_time(self):
        return self.env.user.company_id.calendar_max_time

    @api.model
    def _get_default_calendar_start_time(self):
        return self.env.user.company_id.calendar_start_time

    calendar_weekends = fields.Boolean(string='Show weekends',
                                       default=_get_default_calendar_weekends)
    calendar_weeknumber = fields.Boolean(string='Show week number',
                                         default=_get_default_calendar_weeknumber)
    calendar_weekday = fields.Selection(selection=WEEKDAYS, string='First day of the week is',
                                        required=True, default=_get_default_calendar_weekday)
    calendar_allow_overlap = fields.Boolean(string='Allow events overlap',
                                            default=_get_default_calendar_allow_overlap)
    calendar_disable_dragging = fields.Boolean(string='Disable drag and drop',
                                               default=_get_default_calendar_disable_dragging)
    calendar_disable_resizing = fields.Boolean(string='Disable resizing',
                                               default=_get_default_calendar_disable_resizing)
    calendar_snap_minutes = fields.Integer(string='Default minutes when creating and resizing an event',
                                           default=_get_default_calendar_snap_minutes)
    calendar_slot_minutes = fields.Integer(string='Minutes per row',
                                           default=_get_default_calendar_slot_minutes)
    calendar_min_time = fields.Float(string='Calendar time range from',
                                     default=_get_default_calendar_min_time)
    calendar_max_time = fields.Float(string='Calendar time range to',
                                     default=_get_default_calendar_max_time)
    calendar_start_time = fields.Float(string='Start time',
                                       default=_get_default_calendar_start_time)

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env.user.company_id.update({
            'calendar_weekends': self.calendar_weekends,
            'calendar_weeknumber': self.calendar_weeknumber,
            'calendar_weekday': self.calendar_weekday,
            'calendar_allow_overlap': self.calendar_allow_overlap,
            'calendar_disable_dragging': self.calendar_disable_dragging,
            'calendar_disable_resizing': self.calendar_disable_resizing,
            'calendar_snap_minutes': self.calendar_snap_minutes,
            'calendar_slot_minutes': self.calendar_slot_minutes,
            'calendar_min_time': self.calendar_min_time,
            'calendar_max_time': self.calendar_max_time,
            'calendar_start_time': self.calendar_start_time,
        })
