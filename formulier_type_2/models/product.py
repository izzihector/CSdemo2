# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    xaa_aa_product_type = fields.Selection(selection_add=[
        ('I am Isolation', 'I am Isolation'),
        ('ISO wall service', 'ISO wall service'),
        ('ISO wall material', 'ISO wall material'),
        ('ISO floor service', 'ISO floor service'),
        ('ISO floor material 1', 'ISO floor material 1'),
        ('ISO floor material 2', 'ISO floor material 2'),
        ('ISO roof service', 'ISO roof service'),
        ('ISO roof material', 'ISO roof material'),
        ('SKG IKOB Certification payment', 'SKG IKOB Certification payment'),
        ('Ventilation grid', 'Ventilation grid'),
        ('Cavity boundary','Cavity boundary'),
        ('Extra option iso','Extra option iso')],
        string='PF quote type')
    xaa_aa_tickness_of_wall = fields.Selection([
        ('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),
        ('9', '9'),('10', '10'),('11', '11'),('12', '12'),],
        string='Cavity thickness')
