# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleLineConfig(models.Model):
    _inherit = "sale.line.config"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_four', 'PV projectform')])
