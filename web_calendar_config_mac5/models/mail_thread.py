import json
from lxml import etree

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(MailThread, self).fields_view_get(view_id=view_id, view_type=view_type,
                                                         toolbar=toolbar, submenu=submenu)
        if view_type == 'calendar':
            company_domain = [('id', '=', self.env.user.company_id.id)]
            company_fields = [
                'calendar_weekends',
                'calendar_weeknumber',
                'calendar_weekday',
                'calendar_allow_overlap',
                'calendar_disable_dragging',
                'calendar_disable_resizing',
                'calendar_snap_minutes',
                'calendar_slot_minutes',
                'calendar_min_time',
                'calendar_max_time',
                'calendar_start_time',
            ]
            company_data = self.env['res.company'].search_read(domain=company_domain,
                                                               fields=company_fields)
            company_data = company_data and company_data[0] or {}

            doc = etree.XML(result['arch'])
            for node in doc.xpath("//calendar"):
                node.set('company_data', json.dumps(company_data))
            result['arch'] = etree.tostring(doc)
        return result
