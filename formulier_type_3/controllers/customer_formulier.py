# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import math
import json

class FormulierQuote(http.Controller):

    @http.route(['/customer/pv/quote/submit'], type='json',
                auth="public", methods=['POST'], website=True)
    def customer_formulier_quote_submit(self, quoteData, formulier_id, **kw):
        """  save PV type PF fields value from website quote"""

        if formulier_id and quoteData:
            values = {
                    "xaa_aa_details_are_correct": quoteData['xaa_aa_details_are_correct'],
                    "xaa_aa_energy_consumption": quoteData['xaa_aa_energy_consumption'],
                    "xaa_aa_count_people_in_house": quoteData['xaa_aa_count_people_in_house'],
                    "xaa_aa_type_of_house_id": quoteData['xaa_aa_type_of_house_id'],
                    "xaa_aa_type_of_roof_ids" : quoteData['xaa_aa_type_of_roof_ids'],
                    "xaa_aa_how_roof_covered" : quoteData['xaa_aa_how_roof_covered'],
                    "xaa_aa_how_flat_roof_covered" : quoteData['xaa_aa_how_flat_roof_covered'],
                    "xaa_aa_location_of_roof" : quoteData['xaa_aa_location_of_roof'],
                    "xaa_aa_obstacles_on_roof" : quoteData['xaa_aa_obstacles_on_roof'],
                    "xaa_aa_shadow_cast_solar_panels" : quoteData['xaa_aa_shadow_cast_solar_panels'],
                    "xaa_aa_tree" : quoteData['xaa_aa_tree'],
                    "xaa_aa_another_building" : quoteData['xaa_aa_another_building'],
                    "xaa_aa_obstacle_dormer" : quoteData['xaa_aa_obstacle_dormer'],
                    "xaa_aa_obstacle_chimney_or_air_inlet" : quoteData['xaa_aa_obstacle_chimney_or_air_inlet'],
                    "xaa_aa_obstacle_otherwise_namely" : quoteData['xaa_aa_obstacle_otherwise_namely'],
                    "xaa_aa_explain_otherwise_namely" : quoteData['xaa_aa_explain_otherwise_namely'],
                    "xaa_aa_solar_pannel_product_id" : quoteData['xaa_aa_solar_pannel_product_id'],
                    "xaa_aa_choosen_panel_qty" : quoteData['xaa_aa_choosen_panel_qty'],
                    "xaa_aa_calculated_panel_qty" :quoteData["xaa_aa_calculated_panel_qty"],
                    "xaa_aa_percentage_correction" :quoteData["xaa_aa_percentage_correction"],
                    "xaa_aa_calculated_energy" :quoteData["xaa_aa_calculated_energy"],
                    "xaa_aa_energy_production" :quoteData["xaa_aa_energy_production"],
            }
            formulier_id = request.env['question.formulier'].browse(formulier_id)
            formulier_id.sudo().write(values)
        return True

    @http.route(['/formulier/panels/count'], type='json',
                auth="public", methods=['POST'], website=True)
    def formulier_panels_count(self, quoteData, **kw):
        """ Calculate number of panels and energy consumption for online PF"""

        energy_con_table = {'1': 1925,'2': 3005,'3': 3605,'4': 4155,'5': 4375,'6': 4385}
        roof_factor = {'Zuid': {'schuin dak': 0.86,'plat dak': 0.91,},
                        'Zuidoost': {'schuin dak': 0.84,'plat dak': 0.86,},
                        'West': {'schuin dak': 0.71,'plat dak': 0.8,},
                        'Zuidwest': {'schuin dak': 0.84,'plat dak': 0.86,},
                        'Oost': {'schuin dak': 0.72,'plat dak': 0.8,},
                        'Noordoost': {'schuin dak': 0.64,'plat dak': 0.75,},
                        'Noord': {'schuin dak': 0.44,'plat dak': 0.73,},
                        'Noordwest': {'schuin dak': 0.54,'plat dak': 0.75,}}

        panels,percentage_correction = 1,0
        calculated_energy,calculated_panel = 0,0
        energy_consumption,energy_production = 0,0
        Product = request.env['product.product'].sudo()
        solar_product = Product.browse(quoteData['xaa_aa_solar_pannel_product_id'])

        if quoteData['xaa_aa_energy_consumption']:
            energy_consumption = quoteData['xaa_aa_energy_consumption']
        else:
            if quoteData['xaa_aa_count_people_in_house'] and (
                quoteData['xaa_aa_count_people_in_house'] in energy_con_table.keys()):
                energy_consumption = energy_con_table.get(
                                        quoteData['xaa_aa_count_people_in_house'])
        if energy_consumption > 0 and (
            quoteData['xaa_aa_location_of_roof'] and quoteData['xaa_aa_type_of_roof_name']):
            percentage_correction = roof_factor.get(quoteData['xaa_aa_location_of_roof']).get(
                                                    quoteData['xaa_aa_type_of_roof_name'])
            if percentage_correction:
                # slanted roof and Zuid Oost is 0.86, then needed 5000/0.86=5814
                calculated_energy = energy_consumption/percentage_correction
                if solar_product.xaa_aa_watt_piek > 0:
                    # Solar Panel Product is 1 is 310 Watt then 5814/310 = 18,75 means 19 panels
                    panels = math.ceil(calculated_energy/solar_product.xaa_aa_watt_piek)
        return {'xaa_aa_energy_consumption': energy_consumption,
                'xaa_aa_percentage_correction': percentage_correction,
                'xaa_aa_calculated_energy': round(calculated_energy),
                'xaa_aa_panel_name': solar_product.name,
                'xaa_aa_panel_watt': solar_product.xaa_aa_watt_piek,
                'xaa_aa_panels': panels,
                }

    @http.route(['/customer/pv/quote/create'], type='json',
                auth="public", methods=['POST'], website=True)
    def customer_formulier_quote_create(self, quoteData, formulier_id, **kw):
        """ Create quote for PV type PF and also change opportunity stage"""

        QuoteTemplate = request.env['sale.order.template'].sudo()
        hours,hours_cost,hours_sales,overhead_total,overhead_sale_total=0,0,0,0,0
        if quoteData['xaa_aa_choosen_panel_qty']:
            sale_conf = request.env['sale.line.config'].sudo().search([
                ('xaa_aa_qty', '=', int(quoteData['xaa_aa_choosen_panel_qty'])),
                ('xaa_aa_formulier_type', '=', 'formulier_three')], limit=1)
            if sale_conf:
                hours_sales = sale_conf.xaa_aa_team_sale
                hours_cost = sale_conf.xaa_aa_team_cost
                overhead_total = sale_conf.xaa_aa_overhead_total
                overhead_sale_total = sale_conf.xaa_aa_sales_overhead_total

        if formulier_id and quoteData:
            SaleOrder = request.env['sale.order'].sudo()
            SaleOrderLine = request.env['sale.order.line'].sudo()
            Product = request.env['product.product'].sudo()
            ProductBrand = request.env['product.brand'].sudo()

            formulier_id = request.env['question.formulier'].sudo().browse(formulier_id)
            solar_product = Product.browse(quoteData['xaa_aa_solar_pannel_product_id'])
            converter_product = Product
            optimiser_product = Product
            roof_product = Product

            if solar_product.xaa_aa_watt_piek > 0:
                energy_production = quoteData['xaa_aa_choosen_panel_qty']*solar_product.xaa_aa_watt_piek
                # energy production of 19 * 310 =5890
                if quoteData['xaa_aa_shadow_cast_solar_panels'] == 'ja':
                    brand_id = ProductBrand.search([('xaa_aa_name','ilike','solar edge')],limit=1)
                    optimiser_product = Product.search([
                            ('name','ilike', 'Solar Edge Optimizer P370'),
                            ('xaa_aa_product_type','=', 'Optimisers')],limit=1)
                    if brand_id:
                        converter_product = Product.search([
                            '&', ('xaa_aa_wq_min_range', '<=', energy_production),
                            ('xaa_aa_wq_max_range', '>=', energy_production),
                            ('xaa_aa_product_type', '=', 'Converter'),
                            ('xaa_aa_product_brand','=',brand_id.id)], limit=1)
                    else:
                        converter_product = Product.search([
                            '&', ('xaa_aa_wq_min_range', '<=', energy_production),
                            ('xaa_aa_wq_max_range', '>=', energy_production),
                            ('xaa_aa_product_type', '=', 'Converter')], limit=1)
                else:
                    brand_id = ProductBrand.search([
                        ('xaa_aa_name','ilike','Goodwe')], limit=1)
                    if brand_id:
                        converter_product = Product.search([
                                '&', ('xaa_aa_wq_min_range', '<=', energy_production),
                                ('xaa_aa_wq_max_range', '>=', energy_production),
                                ('xaa_aa_product_type', '=', 'Converter'),
                                ('xaa_aa_product_brand','=', brand_id.id)], limit=1)
            if formulier_id.xaa_aa_partner_id:
                quote_template_id = QuoteTemplate.search([
                    ('name','ilike','Zonnepanelen')],limit=1)
                quote = SaleOrder.create({
                        'partner_id': formulier_id.xaa_aa_partner_id.id,
                        'xaa_aa_formulier_id': formulier_id.id,
                        'opportunity_id': formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.id,
                        'xaa_aa_show_only_total': True,
                        'sale_order_template_id': quote_template_id and quote_template_id.id or False,
                    })
                quote.user_id = request.env.user.id
                if quote_template_id:
                    quote.onchange_sale_order_template_id()
                    quote.fill_drawing_images()

                vat_id = Product.search([
                    ('xaa_aa_product_type', '=', 'BTW teruggave')], limit=1)
                # material_id = Product.search([
                #     ('xaa_aa_product_type', '=', 'Overige Materialen')], limit=1)
                stekkers_id = Product.search([
                    ('xaa_aa_product_type', '=', 'Stekkers')], limit=1)
                installation_product = Product.search([
                    ('name', 'ilike', 'Montage kosten zonnepanelen')], limit=1)
                if quoteData['xaa_aa_type_of_roof_name'] == 'plat dak':
                    roof_product = Product.search([
                        ('name', 'ilike', 'Esdec Flatfix - Fusion'),
                        ('xaa_aa_product_type','=','Flat Roof')],limit=1)
                if quoteData['xaa_aa_type_of_roof_name'] == 'schuin dak':
                    roof_product = Product.search([
                        ('name', 'ilike', 'Esdec ClickFit - Evo'),
                        ('xaa_aa_product_type','=','Slanted Roof')],limit=1)
                if vat_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': vat_id.id,
                        'product_uom_qty': 1,
                        'discount': 100,
                    })
                SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_solar_pannel_product_id'],
                        'product_uom_qty': quoteData['xaa_aa_choosen_panel_qty'] or 1,
                })
                if converter_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': converter_product.id,
                        'product_uom_qty': 1,
                    })
                if optimiser_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': optimiser_product.id,
                        'product_uom_qty': quoteData['xaa_aa_choosen_panel_qty'] or 1,
                    })
                if roof_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': roof_product.id,
                        'product_uom_qty': quoteData['xaa_aa_choosen_panel_qty'] or 1,
                    })
                if stekkers_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': stekkers_id.id,
                        'product_uom_qty': 1,
                    })
                if installation_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': installation_product.id,
                        'product_uom_qty': 1,
                        'price_unit': hours_sales or installation_product.lst_price,
                        'purchase_price': hours_cost or installation_product.standard_price,
                    })
                task_product = Product.search([
                    ('name','ilike','Projectbegeleiding PV')], limit=1)
                if task_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': task_product.id,
                        'product_uom_qty': 1,
                    })
                overhead_product = request.env.ref('formulier_quote_set_lines.overhead_product', False)
                if overhead_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': overhead_product.id,
                        'product_uom_qty': 1,
                        'purchase_price': overhead_total or overhead_product.standard_price,
                        'price_unit': overhead_sale_total or overhead_product.lst_price,
                        })
                # if material_id:
                #     SaleOrderLine.create({
                #         'order_id': quote.id,
                #         'product_id': material_id.id,
                #         'product_uom_qty': 1,
                #     })
                formulier_id.xaa_aa_state = 'quotation'
                crm_stage_id = request.env['crm.stage'].sudo().search([
                    ('name','in',['Website offerte gemaakt (5)','Website offerte gemaakt (14)'])],limit=1)
                if formulier_id.xaa_aa_lead_id:
                    lead = formulier_id.xaa_aa_lead_id
                    quote.xaa_aa_lead_category = lead.xaa_aa_lead_category and lead.xaa_aa_lead_category.id
                    quote.xaa_aa_lead_lead_source = lead.xaa_aa_lead_lead_source and lead.xaa_aa_lead_lead_source.id
                    if crm_stage_id and lead.stage_id.id != crm_stage_id.id:
                        lead.stage_id = crm_stage_id.id
                if quote_template_id:
                    quote.fill_calculations_value()
                email_act = quote.action_quotation_send()
                email_ctx = email_act.get('context', {})
                quote.with_context(**email_ctx).message_post_with_template(email_ctx.get('default_template_id'))
                return quote.preview_sale_order()
        return False


    @http.route(['/customer/pv/question/submit/<int:formulier_id>/<string:model_name>'],
        type='http', auth="public", methods=['POST'], website=True)
    def customer_pv_question_submit(self, formulier_id,model_name, **kwargs):
        """ Save PV type PF fields value from website quote questionnier"""

        if formulier_id:
            values = {'xaa_aa_quote_scaffolding': kwargs.get('xaa_aa_quote_scaffolding'),
                    'xaa_aa_quote_place_scaffolding': kwargs.get('xaa_aa_quote_place_scaffolding'),
                    'xaa_aa_quote_place_scaffolding_text': kwargs.get('xaa_aa_quote_place_scaffolding_text'),
                    'xaa_aa_quote_home_accessible': kwargs.get('xaa_aa_quote_home_accessible'),
                    'xaa_aa_quote_home_parking': kwargs.get('xaa_aa_quote_home_parking'),
                    'xaa_aa_quote_type_of_roof': kwargs.get('xaa_aa_quote_type_of_roof'),
                    'xaa_aa_quote_type_of_roof_text': kwargs.get('xaa_aa_quote_type_of_roof_text'),
                    'xaa_aa_quote_schuin_roof_covered': kwargs.get('xaa_aa_quote_schuin_roof_covered'),
                    'xaa_aa_quote_plat_roof_covered': kwargs.get('xaa_aa_quote_plat_roof_covered'),
                    'xaa_aa_quote_condition_roof': kwargs.get('xaa_aa_quote_condition_roof'),
                    'xaa_aa_quote_edge_relevant_roof': kwargs.get('xaa_aa_quote_edge_relevant_roof'),
                    'xaa_aa_quote_incorporated_roof': kwargs.get('xaa_aa_quote_incorporated_roof'),
                    'xaa_aa_quote_slope_roof': kwargs.get('xaa_aa_quote_slope_roof'),
                    'xaa_aa_quote_description': kwargs.get('xaa_aa_quote_description'),
                    'xaa_aa_quote_inverter_hang': kwargs.get('xaa_aa_quote_inverter_hang'),
                    'xaa_aa_quote_meter_cupboard': kwargs.get('xaa_aa_quote_meter_cupboard'),
                    'xaa_aa_quote_lay_cable_description': kwargs.get('xaa_aa_quote_lay_cable_description'),
                    'xaa_aa_quote_building_permit_required': kwargs.get('xaa_aa_quote_building_permit_required'),
                    'xaa_aa_quote_occupied_home': kwargs.get('xaa_aa_quote_occupied_home'),
                    'xaa_aa_quote_entrepreneur': kwargs.get('xaa_aa_quote_entrepreneur'),
                    'xaa_aa_quote_solar_panel_description': kwargs.get('xaa_aa_quote_solar_panel_description'),
                    'xaa_aa_quote_final_approval': kwargs.get('xaa_aa_quote_final_approval'),
                    'xaa_aa_quote_final_approval_text': kwargs.get('xaa_aa_quote_final_approval_text'),
                    'xaa_aa_quote_final_approval_date': kwargs.get('xaa_aa_quote_final_approval_date'),
            }

            formulier_id = request.env['question.formulier'].sudo().browse(formulier_id)
            que_lead = formulier_id.xaa_aa_lead_id
            stage = request.env['crm.stage'].sudo().search([
                ('name','in',['Vragen Ingevuld[7]','Richtprijs verstuurd'])],limit=1)
            if stage and que_lead:
                if que_lead.stage_id.id != stage.id:
                    que_lead.stage_id = stage.id
            formulier_id.write(values)
            return json.dumps({'id': formulier_id.id})
        return False
