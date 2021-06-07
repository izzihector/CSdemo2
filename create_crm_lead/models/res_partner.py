# -*- encoding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def default_get(self, fields):
        res = super(ResPartner, self).default_get(fields)
        nlLang = self.env['res.lang'].search([
            ('code', '=', 'nl_NL')])
        if not nlLang:
            raise UserError(_('Please activate Dutch / Nederlands Language'))
        res['lang'] = 'nl_NL'
        ir_model_data = self.env['ir.model.data']
        res['country_id'] = ir_model_data.get_object_reference('base', 'nl')[1]
        return res


class MailMessage(models.Model):
    _inherit = 'mail.message'

    xaa_aa_company = fields.Char('Company Name')
