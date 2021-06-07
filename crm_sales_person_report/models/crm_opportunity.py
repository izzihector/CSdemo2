# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models, _

class Crm_Lead(models.Model):
    _inherit = 'crm.lead' 
    
    xaa_aa_opportunity_by = fields.Many2one('res.users', 'Meeting', tracking=True, index=True)
    xaa_aa_phone_by = fields.Many2one('res.users', 'Call', tracking=True, index=True)
    xaa_aa_work_by = fields.Many2one('res.users', 'Work', tracking=True, index=True)
    xaa_aa_deal_by = fields.Many2one('res.users', 'Deal', tracking=True, index=True)
    xaa_aa_quote_by = fields.Many2one('res.users', 'Quote', tracking=True, index=True)
    xaa_aa_phone_date = fields.Datetime('Call Date')
    xaa_aa_quote_date = fields.Datetime('Quote Date')
    xaa_aa_work_date = fields.Datetime('Work Date')
    xaa_aa_deal_date = fields.Datetime('Deal Date')
    xaa_aa_opportunity_date = fields.Datetime('Meeting Date')
    xaa_aa_stage_name = fields.Char(string="Stage name", related="stage_id.name")