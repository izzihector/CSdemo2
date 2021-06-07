# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json


class FormulierQuote(http.Controller):

    @http.route(['/customer/iso/quote/submit'], type='json',
                auth="public", methods=['POST'], website=True)
    def customer_formulier_iso_quote_submit(self, quoteData, formulier_id, **kw):
        """ save ISO type PF fields value from website quote"""

        if formulier_id and quoteData:
            formulier_id = request.env['question.formulier'].sudo().browse(formulier_id)
            formulier_id.write({
                    'xaa_aa_quote_construction_year': quoteData['xaa_aa_quote_construction_year'] or False,
                    'xaa_aa_quote_house_insulated': quoteData['xaa_aa_quote_house_insulated'] or False,
                    'xaa_aa_quote_cavity_thickness_home': quoteData['xaa_aa_quote_cavity_thickness_home'] or False,
                    'xaa_aa_quote_type_of_house_id': int(quoteData['xaa_aa_quote_type_of_house_id']) or False,
                    'xaa_aa_quote_need_insulated': quoteData['xaa_aa_quote_need_insulated'] or False,
                    'xaa_aa_quote_many_extension': quoteData['xaa_aa_quote_many_extension'] or 0,
                })
        return True

    @http.route(['/customer/iso/quote/create'], type='json',
                auth="public", methods=['POST'], website=True)
    def customer_formulier_iso_quote_create(self, quoteData, formulier_id, **kw):
        """ Create quote for ISO type PF and also change opportunity stage"""

        if formulier_id and quoteData:
            hours,hours_cost,hours_sales,overhead_total,overhead_sale_total=1,0,0,0,0
            if quoteData['xaa_aa_quote_many_extension']:
                sale_conf = request.env['sale.line.config'].sudo().search([
                    ('xaa_aa_qty', '=', int(quoteData['xaa_aa_quote_many_extension'])),
                    ('xaa_aa_formulier_type', '=', 'formulier_two')], limit=1)
                if sale_conf:
                    hours_cost = sale_conf.xaa_aa_team_cost
                    hours_sales = sale_conf.xaa_aa_team_sale
                    overhead_total = sale_conf.xaa_aa_overhead_total
                    overhead_sale_total = sale_conf.xaa_aa_sales_overhead_total

            formulier_id = request.env['question.formulier'].sudo().browse(formulier_id)
            if formulier_id.xaa_aa_partner_id:
                SaleOrder = request.env['sale.order'].sudo()
                SaleOrderLine = request.env['sale.order.line'].sudo()
                Product = request.env['product.product'].sudo()
                material_product_ids = Product
                quote_template_id = request.env['sale.order.template'].sudo().search([
                    ('name','ilike','Spouwmuurisolatie')], limit=1)

                quote = SaleOrder.create({
                        'partner_id': formulier_id.xaa_aa_partner_id.id,
                        'xaa_aa_formulier_id': formulier_id.id,
                        'opportunity_id': formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.id or False,
                        'xaa_aa_show_only_total': True,
                        'sale_order_template_id': quote_template_id and quote_template_id.id or False,
                    })
                quote.user_id = request.env.user.id
                if quote_template_id:
                    quote.onchange_sale_order_template_id()
                    quote.fill_drawing_images()

                service_product_id = Product.search([
                    ('name', 'ilike', 'Aanbrengen spouwmuurisolatie')], limit=1)
                if service_product_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': service_product_id.id,
                        'product_uom_qty': 1,
                        'purchase_price': hours_cost or service_product_id.standard_price,
                        'price_unit': hours_sales or service_product_id.lst_price,
                    })
                if quoteData['xaa_aa_quote_construction_year'] == 'na 1975':
                    material_product_ids = Product.search([
                            ('name', 'ilike', 'Enverifoam')])
                elif quoteData['xaa_aa_quote_construction_year'] == 'tussen 1935 en 1975':
                    if quoteData['xaa_aa_quote_house_insulated'] == 'Knauf Supafil minerals inblaaswol(aanbevolen)':
                        material_product_ids = Product.search([
                            ('name', 'ilike', 'Knauf Supafil')])
                    elif quoteData['xaa_aa_quote_house_insulated'] == 'HR++ Grijze EPS Parels':
                        material_product_ids = Product.search([
                            ('name', 'ilike', 'EPS Parels')])
                    elif quoteData['xaa_aa_quote_house_insulated'] == 'Energie Foam wit isolatieschuim':
                        material_product_ids = Product.search([
                            ('name', 'ilike', 'Enverifoam')])
                if material_product_ids:
                    cost_price = material_product_ids[0].standard_price
                    sell_price = material_product_ids[0].lst_price
                    material_name = material_product_ids[0].name
                    material_id = material_product_ids[0].id
                    if quoteData['xaa_aa_quote_cavity_thickness_home'] == 'Mind dan 5 cm':
                        tickness_of_wall = 5
                    elif quoteData['xaa_aa_quote_cavity_thickness_home'] == '5 tot 6 cm':
                        tickness_of_wall = 6
                    elif quoteData['xaa_aa_quote_cavity_thickness_home'] == '6 tot 8 cm':
                        tickness_of_wall = 7
                    elif quoteData['xaa_aa_quote_cavity_thickness_home'] == 'Meer dan 8 cm':
                        tickness_of_wall = 8
                    else:
                        tickness_of_wall = 6
                    for product in material_product_ids:
                        if tickness_of_wall == int(product.xaa_aa_tickness_of_wall):
                            cost_price = product.standard_price
                            sell_price = product.lst_price
                            material_name = product.name
                            material_id = product.id
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': material_id,
                        'name': material_name,
                        'product_uom_qty': quoteData['xaa_aa_quote_many_extension'] or 1,
                        })
                certificate_product_id = Product.search([
                    ('xaa_aa_product_type', '=', 'SKG IKOB Certification payment')],
                    limit=1)
                if certificate_product_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': certificate_product_id.id,
                        'product_uom_qty': quoteData['xaa_aa_quote_many_extension'] or 1,
                    })
                if quoteData['xaa_aa_qupte_do_crawl_space'] == 'ja':
                    ventilation_product_id = Product.search([
                        ('xaa_aa_product_type', '=', 'Ventilation grid')],limit=1)
                    if ventilation_product_id:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': ventilation_product_id.id,
                            'product_uom_qty': quoteData['xaa_aa_quote_ventilation_qty'] or 1,
                        })
                cavity_product_id = Product.search([
                    ('xaa_aa_product_type', '=', 'Cavity boundary')], limit=1)
                if cavity_product_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': cavity_product_id.id,
                        'product_uom_qty': quoteData['xaa_aa_quote_cavity_qty'] or 1,
                    })

                # extra_product_id = Product.search([
                #     ('xaa_aa_product_type', '=', 'Extra option iso')], limit=1)
                # if extra_product_id:
                #     SaleOrderLine.create({
                #         'order_id': quote.id,
                #         'product_id': extra_product_id.id,
                #         'product_uom_qty': 1,
                #         'discount': 100,
                #     })
                overhead_product = request.env.ref('formulier_quote_set_lines.overhead_product', False)
                if overhead_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': overhead_product.id,
                        'product_uom_qty': 1,
                        'purchase_price': overhead_total or overhead_product.standard_price,
                        'price_unit': overhead_sale_total or overhead_product.lst_price,
                        })
                task_product_id = Product.search([
                    ('name', 'ilike', 'Projectbegeleiding Isolatie')],
                    limit=1)
                if task_product_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': task_product_id.id,
                        'product_uom_qty': 1,
                    })
                formulier_id.xaa_aa_state = 'quotation'
                crm_stage_id = request.env.ref('crm.stage_lead3', False)
                if formulier_id.xaa_aa_lead_id and crm_stage_id:
                    lead = formulier_id.xaa_aa_lead_id
                    quote.xaa_aa_lead_category = lead.xaa_aa_lead_category and lead.xaa_aa_lead_category.id
                    quote.xaa_aa_lead_lead_source = lead.xaa_aa_lead_lead_source and lead.xaa_aa_lead_lead_source.id
                    if lead.stage_id.id != crm_stage_id.id:
                        lead.stage_id = crm_stage_id.id
                if quote_template_id:
                    quote.fill_calculations_value()
                email_act = quote.action_quotation_send()
                email_ctx = email_act.get('context', {})
                quote.with_context(**email_ctx).message_post_with_template(email_ctx.get('default_template_id'))
                return quote.preview_sale_order()
        return True

    @http.route(['/customer/iso/question/submit/<int:formulier_id>/<string:model_name>'],
        type='http', auth="public", methods=['POST'], website=True)
    def customer_iso_question_submit(self, formulier_id, model_name, **kwargs):
        """ Save ISO type PF fields value from website quote questionnier"""

        if formulier_id:
            values = {'xaa_aa_quote_home_free_install': kwargs.get('xaa_aa_quote_home_free_install'),
                    'xaa_aa_quote_iso_home_accessible': kwargs.get('xaa_aa_quote_iso_home_accessible'),
                    'xaa_aa_quote_iso_home_parking': kwargs.get('xaa_aa_quote_iso_home_parking'),
                    'xaa_aa_quote_iso_estimate_height_gutter': kwargs.get('xaa_aa_quote_iso_estimate_height_gutter'),
                    'xaa_aa_quote_iso_estimate_height_ridge': kwargs.get('xaa_aa_quote_iso_estimate_height_ridge'),
                    'xaa_aa_quote_iso_square_meter_quotation': kwargs.get('xaa_aa_quote_iso_square_meter_quotation'),
                    'xaa_aa_quote_iso_faced_covered_obstacles': kwargs.get('xaa_aa_quote_iso_faced_covered_obstacles'),
                    'xaa_aa_quote_iso_thickness_cavity': kwargs.get('xaa_aa_quote_iso_thickness_cavity'),
                    'xaa_aa_quote_iso_cavity_wall_insulation': kwargs.get('xaa_aa_quote_iso_cavity_wall_insulation'),
                    'xaa_aa_quote_iso_cavity_contamination': kwargs.get('xaa_aa_quote_iso_cavity_contamination'),
                    'xaa_aa_quote_iso_house_painted_faced': kwargs.get('xaa_aa_quote_iso_house_painted_faced'),
                    'xaa_aa_quote_iso_home_cutting_joint': kwargs.get('xaa_aa_quote_iso_home_cutting_joint'),
                    'xaa_aa_quote_iso_crawl_space_use': kwargs.get('xaa_aa_quote_iso_crawl_space_use'),
                    'xaa_aa_quote_iso_monumental_building': kwargs.get('xaa_aa_quote_iso_monumental_building'),
                    'xaa_aa_quote_iso_rental_owner_home': kwargs.get('xaa_aa_quote_iso_rental_owner_home'),
                    'xaa_aa_quote_iso_insulation_description': kwargs.get('xaa_aa_quote_iso_insulation_description'),
                    'xaa_aa_quote_iso_working_days': kwargs.get('xaa_aa_quote_iso_working_days'),
            }

            formulier_id = request.env['question.formulier'].sudo().browse(formulier_id)
            lead_id = formulier_id.xaa_aa_lead_id
            stage_id = request.env['crm.stage'].sudo().search([
                ('name','in',['Website offerte gemaakt (5)','Website offerte gemaakt (14)'])],limit=1)
            if stage_id and lead_id:
                if lead_id.stage_id.id != stage_id.id:
                    lead_id.stage_id = stage_id.id
            formulier_id.write(values)
            return json.dumps({'id': formulier_id.id})
        return False
