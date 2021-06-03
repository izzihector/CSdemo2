# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class FormulierTypeOptions(models.Model):
    """ Formulier type option"""

    _name = "formulier.type.option"
    _description = "formulier type option"
    _rec_name = 'xaa_aa_name'

    xaa_aa_name = fields.Char('product option')


class FormulierTypeInstall(models.Model):
    """ Formulier type option"""

    _name = "formulier.type.install"
    _description = "formulier type installation"
    _rec_name = 'xaa_aa_name'

    xaa_aa_name = fields.Char('product installation')


class FormulierType(models.Model):
    """ Formulier type """

    _name = "formulier.type"
    _description = "formulier type"
    _rec_name = 'xaa_aa_name'

    xaa_aa_name = fields.Char('Type')
    option_ids = fields.Many2many('formulier.type.option', string='Option')
    install_ids = fields.Many2many('formulier.type.install', string='installation')


class ProductTemplate(models.Model):
    _inherit = "product.template"

    xaa_aa_formulier_type = fields.Many2one('formulier.type',string='Formulier Type')