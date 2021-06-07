# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields, api, _
import datetime


class ResPartner(models.Model):
    _inherit = 'res.partner'

    xaa_aa_export = fields.Boolean('Exported')
    xaa_aa_export_date = fields.Date('Export Date')


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    xaa_aa_export = fields.Boolean('Exported')
    xaa_aa_export_date = fields.Date('Export Date')


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    xaa_aa_ac_code = fields.Char('Accountview Code')


class AccountAccount(models.Model):
    _inherit = 'account.account'

    xaa_aa_ac_code = fields.Integer('Accountview Code', default=10300)
