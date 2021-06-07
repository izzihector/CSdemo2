# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
from odoo import tools, models, fields


class SaleLineWizard(models.TransientModel):
    _name = "sale.line.config.wizard"
    _description = "sale line config wizard"
    _rec_name = 'xaa_aa_qty_hours'

    xaa_aa_formulier_type = fields.Char(string='Question Type')
    xaa_aa_qty_hours = fields.Selection([
        ('1', '1 Hours'),
        ('2', '2 Hours'),
        ('3', '3 Hours'),
        ('4', '4 Hours'),
        ('5', '5 Hours'),
        ('6', '6 Hours'),
        ('7', '7 Hours'),
        ('8', '8 Hours'),
        ('9', '9 Hours'),
        ('10', '10 Hours'),
        ('11', '11 Hours'),
        ('12', '12 Hours'),
        ('13', '13 Hours'),
        ('14', '14 Hours'),
        ('15', '15 Hours'),
        ('16', '16 Hours'),
        ('17', '17 Hours'),
        ('18', '18 Hours'),
        ('19', '19 Hours'),
        ('20', '20 Hours'),
        ('21', '21 Hours'),
        ('22', '22 Hours'),
        ('23', '23 Hours'),
        ('24', '24 Hours'),
        ('25', '25 Hours'),
        ('26', '26 Hours'),
        ('27', '27 Hours'),
        ('28', '28 Hours'),
        ('29', '29 Hours'),
        ('30', '30 Hours'),
        ('31', '31 Hours'),
        ('32', '32 Hours'),
        ('33', '33 Hours'),
        ('34', '34 Hours'),
        ('35', '35 Hours'),
        ('36', '36 Hours'),
        ('37', '37 Hours'),
        ('38', '38 Hours'),
        ('39', '39 Hours'),
        ('40', '40 Hours'),
        ('41', '41 Hours'),
        ('42', '42 Hours'),
        ('43', '43 Hours'),
        ('44', '44 Hours'),
        ('45', '45 Hours'),
        ('46', '46 Hours'),
        ('47', '47 Hours'),
        ('48', '48 Hours'),
        ('49', '49 Hours'),
        ('50', '50 Hours'),
        ], string='Qnty hours')
    xaa_aa_sale_id = fields.Many2one('sale.order', string='Order ID')
    xaa_aa_product_qty = fields.Char(string='Product QTY')

    def add_lines(self):
        return True
