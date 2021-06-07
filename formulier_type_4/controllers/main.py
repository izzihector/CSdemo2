# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.project_formulier.controllers.main import ProjectFormulier
import math

class ProjectFormulier(ProjectFormulier):

    @http.route(['/formulier/pv_quote_infos'], type='json', auth="public", methods=['POST'], website=True)
    def pv_quote_infos(self, solar_color=None, roof_type=None, **kw):
        """ Send Required data to Quote PV tab"""

        productObj = request.env['product.product'].sudo()
        solar_products = productObj
        roof_products = productObj
        if solar_color:
            solar_products = productObj.search([
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',[int(solar_color)])])
        if roof_type:
            if roof_type == 'Schuin':
                roof_products = productObj.search([
                    ('xaa_aa_product_type', 'ilike', 'Slanted Roof'),])
            else:
                roof_products = productObj.search([
                    ('xaa_aa_product_type', 'ilike', 'Flat Roof'),])
        return dict(
            solar_products=[(sp.id, sp.name, sp.list_price) for sp in solar_products],
            roof_products=[(rp.id, rp.name, rp.list_price) for rp in roof_products],
        )

    @http.route(['/formulier/panels_count'], type='json',
                auth="public", methods=['POST'], website=True)
    def formulier_four_panels_count(self, data, **kw):
        """ Calculate number of panels and energy consumption for online PF"""

        roof_factor = {'Zuid': {'Schuin': 0.86,'Plat': 0.91,},
                        'Zuidoost': {'Schuin': 0.84,'Plat': 0.86,},
                        'West': {'Schuin': 0.71,'Plat': 0.8,},
                        'Zuidwest': {'Schuin': 0.84,'Plat': 0.86,},
                        'Oost': {'Schuin': 0.72,'Plat': 0.8,},
                        'Noordoost': {'Schuin': 0.64,'Plat': 0.75,},
                        'Noord': {'Schuin': 0.44,'Plat': 0.73,},
                        'Noordwest': {'Schuin': 0.54,'Plat': 0.75,}}

        panels,percentage_correction = 1,0
        calculated_energy = 0
        energy_consumption = 0
        Product = request.env['product.product'].sudo()
        solar_product = Product.browse(data['solar_pannel_product_id'])

        if data['annual_consumption']:
            energy_consumption = data['annual_consumption']

        if energy_consumption > 0 and (
            data['orientaion_type'] and data['roof_type']):
            percentage_correction = roof_factor.get(data['orientaion_type']).get(
                                                    data['roof_type'])
            if percentage_correction:
                # slanted roof and Zuid Oost is 0.86, then needed 5000/0.86=5814
                calculated_energy = energy_consumption/percentage_correction
                if solar_product.xaa_aa_watt_piek > 0:
                    # Solar Panel Product is 1 is 310 Watt then 5814/310 = 18,75 means 19 panels
                    panels = math.ceil(calculated_energy/solar_product.xaa_aa_watt_piek)
        return {
                'percentage_correction': percentage_correction,
                'calculated_energy': round(calculated_energy),
                'panel_watt': solar_product.xaa_aa_watt_piek,
                'panels': panels,
                }
