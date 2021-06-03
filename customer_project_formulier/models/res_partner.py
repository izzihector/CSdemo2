# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class PartnerForumierTypeInstall(models.Model):
    """ Partner formulier type install"""

    _name = "partner.formulier.type.install"
    _description = "partner formulier type install"
    _rec_name = 'xaa_aa_formulier_type_install'

    xaa_aa_formulier_type = fields.Many2one('formulier.type', string='Formulier type')
    xaa_aa_formulier_type_install = fields.Many2one('formulier.type.install', string='Formulier type install')
    xaa_aa_partner_id = fields.Many2one('res.partner')

class PartnerForumierTypeOption(models.Model):
    """ Partner formulier type option"""

    _name = "partner.formulier.type.option"
    _description = "partner formulier type"
    _rec_name = 'xaa_aa_formulier_type_option'

    xaa_aa_formulier_type = fields.Many2one('formulier.type', string='Formulier type')
    xaa_aa_formulier_type_option = fields.Many2one('formulier.type.option', string='Formulier type option')
    xaa_aa_partner_id = fields.Many2one('res.partner')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    xaa_aa_formulier_type = fields.Many2many('formulier.type', string='Product Formulier')
    xaa_aa_formulier_type_option = fields.One2many('partner.formulier.type.option', 'xaa_aa_partner_id', string='Product Formulier Option')
    xaa_aa_formulier_type_install = fields.One2many('partner.formulier.type.install', 'xaa_aa_partner_id', string='Product Formulier Installation')
