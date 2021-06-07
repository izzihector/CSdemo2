# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields

class LeadSource(models.Model):
    _inherit = 'lead.category'

    xaa_aa_marker_color = fields.Selection([
        ('green', 'Green'),
        ('black', 'Black'),
        ('blue', 'Blue'),
        ('brown', 'Brown'),
        ('cyan', 'Cyan'),
        ('grey', 'Grey'),
        ('lightgreen', 'Light-Green'),
        ('magenta', 'Magenta'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('red', 'Red'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
    ], string='Marker Color')
