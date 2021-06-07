from odoo import fields, models

WEEKDAYS = [('0', 'Sunday'), ('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'),
            ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday')]


class Company(models.Model):
    _inherit = 'res.company'

    calendar_weekends = fields.Boolean(string='Show weekends?', default=True)
    calendar_weeknumber = fields.Boolean(string='Show week number?', default=True)
    calendar_weekday = fields.Selection(selection=WEEKDAYS, string='First day of week?',
                                        required=True, default='0')
    calendar_allow_overlap = fields.Boolean(string='Allow events overlap?', default=True)
    calendar_disable_dragging = fields.Boolean(string='Disable drag and drop?', default=False)
    calendar_disable_resizing = fields.Boolean(string='Disable resizing?', default=False)
    calendar_snap_minutes = fields.Integer(string='Default minutes when creating and resizing',
                                           default=15)
    calendar_slot_minutes = fields.Integer(string='Minutes per row', default=30)
    calendar_min_time = fields.Float(string='Calendar time range from', default=0.0)
    calendar_max_time = fields.Float(string='Calendar time range to', default=24.0)
    calendar_start_time = fields.Float(string='Start time', default=6.0)
