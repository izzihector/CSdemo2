# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResUsers(models.Model):
    _inherit = "res.users"

    xaa_aa_show_score = fields.Boolean(string='Show Score on PF')

