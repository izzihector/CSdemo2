# -*- coding: utf-8 -*-

from odoo import _, api, exceptions, fields, models, modules


class Crmlead(models.Model):
    _inherit = "crm.lead"

    def write(self, vals):
        if 'active' in vals and vals['active'] is True:
            self.env['bus.bus'].sendone(
                (self._cr.dbname, 'res.partner', self.user_id.partner_id.id),
                {'type': 'activity_updated', 'activity_created': True})
        if 'active' in vals and vals['active'] is False:
            self.env['bus.bus'].sendone(
                (self._cr.dbname, 'res.partner', self.user_id.partner_id.id),
                {'type': 'activity_updated', 'activity_deleted': True})
        return super(Crmlead, self).write(vals)

    def unlink(self):
        for lead in self:
            self.env['bus.bus'].sendone(
                (self._cr.dbname, 'res.partner', lead.user_id.partner_id.id),
                {'type': 'activity_updated', 'activity_deleted': True})
        return super(Crmlead, self).unlink()


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def systray_get_leads(self):
        query = """SELECT count(*), act.id, act.type, act.name
                    FROM crm_lead AS act
                    WHERE act.type = 'lead' AND act.active = 't'
                    GROUP BY act.id;
                    """
        self.env.cr.execute(query, {
            'user_id': self.env.uid,
        })
        lead_data = self.env.cr.dictfetchall()

        all_leads = {}
        for lead in lead_data:
            if not all_leads.get(lead['id']):
                module = self.env['crm.lead']._original_module
                icon = module and modules.module.get_module_icon(module)
                all_leads[lead['id']] = {
                    'name': lead['name'],
                    'id': lead['id'],
                    'model': 'crm.lead',
                    'type': 'activity',
                    'icon': icon,
                    'total_count': 0,
                }
           
            all_leads[lead['id']]['total_count'] += lead['count']

        return list(all_leads.values())