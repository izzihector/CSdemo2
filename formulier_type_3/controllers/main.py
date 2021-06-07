# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.project_formulier.controllers.main import ProjectFormulier

class ProjectFormulier(ProjectFormulier):

    @http.route(['/pv_questions_thanks'], type='http', auth="public", website=True)
    def pv_questions_thanks(self, **kw):
        return request.render('formulier_type_3.pv_questions_thanks', {})

    @http.route(['/project/formulier/submit/<int:xaa_aa_formulier_id>/<string:model_name>'], type='http',
                auth='public', methods=['POST'], website=True)
    def project_formulier_submit(self, xaa_aa_formulier_id, model_name, **kwargs):
        """ Project Formulier web form submit """

        if xaa_aa_formulier_id:
            if kwargs.get('xaa_aa_solar_type'):
                kwargs.update({'xaa_aa_solar_type': [[6,False,[int(i) for i in kwargs.get('xaa_aa_solar_type').split(',')]]]})
        return super(ProjectFormulier, self).project_formulier_submit(xaa_aa_formulier_id,model_name,**kwargs)

    @http.route(['/formulier/get_installation_time'], type='json', auth="user", methods=['POST'], website=True)
    def get_installation_time(self, solar_qty, **kw):
        hours = 0
        sale_conf = request.env['sale.line.config'].sudo().search([('xaa_aa_qty', '=', int(solar_qty))], limit=1)
        if sale_conf:
            hours = str(sale_conf.xaa_aa_qty_hours)+' Hours'
        return dict(
            hours=hours,
        )

    @http.route(['/formulier/quote_infos'], type='json', auth="user", methods=['POST'], website=True)
    def quote_infos(self, energy=0.0, quote_type=None, roof=None, xaa_aa_solar_type=None, product_id=0, **kw):
        Product = request.env['product.product'].sudo()
        energy_wat_piek = 0
        select_product = Product
        optimiser_products = Product
        solar_product_ids = Product
        flat_product_ids = Product
        slanted_product_ids = Product
        user = request.env.user
        if user.has_group('base.group_user'):
            domain = ['|',('xaa_aa_show_product_user','=','yes'),'|',
                ('xaa_aa_show_product_user','=',False),
                ('xaa_aa_product_portal_user','in', user.id)]
        else:
            domain = ['|',('xaa_aa_product_portal_user','in', user.id),('xaa_aa_show_product_user','=',False)]
        if xaa_aa_solar_type:
            solar_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',[int(sol) for sol in xaa_aa_solar_type])], order='xaa_aa_priority')
        converter_product_ids = Product.search(domain+[
            '&', ('xaa_aa_min_product_range', '<=', energy),
            ('xaa_aa_max_product_range', '>=', energy),
            ('xaa_aa_product_type', '=', 'Converter')], order='xaa_aa_priority')
        if str(roof) in ['Flat Roof', 'Mix Roof']:
            flat_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Flat Roof')], order='xaa_aa_priority')
        if str(roof) in ['Slanted Roof', 'Mix Roof']:
            slanted_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Slanted Roof')], order='xaa_aa_priority')
        if product_id:
            select_product = Product.browse(product_id)
            energy_wat_piek = select_product.xaa_aa_watt_piek
            if select_product.xaa_aa_product_type == 'Converter' and select_product.xaa_aa_product_brand:
                optimiser_products = Product.search(domain+[
                            ('xaa_aa_product_type', '=', 'Optimisers'),
                            ('xaa_aa_product_brand','=', select_product.xaa_aa_product_brand.id)],
                             order='xaa_aa_priority')
        return dict(
            converter_product_ids=[(cp.id, cp.name, cp.xaa_aa_wq_header_1, cp.xaa_aa_wq_header_2, cp.xaa_aa_wq_line1, cp.xaa_aa_wq_line2, cp.xaa_aa_wq_line3, cp.xaa_aa_wq_line4, cp.list_price) for cp in converter_product_ids],
            optimiser_products = [(op.id, op.name, op.xaa_aa_wq_header_1, op.xaa_aa_wq_header_2, op.xaa_aa_wq_line1, op.xaa_aa_wq_line2, op.xaa_aa_wq_line3, op.xaa_aa_wq_line4, op.list_price) for op in optimiser_products],
            flat_product_ids=[(frp.id, frp.name, frp.xaa_aa_wq_header_1, frp.xaa_aa_wq_header_2, frp.xaa_aa_wq_line1, frp.xaa_aa_wq_line2, frp.xaa_aa_wq_line3, frp.xaa_aa_wq_line4) for frp in flat_product_ids],
            slanted_product_ids=[(srp.id, srp.name, srp.xaa_aa_wq_header_1, srp.xaa_aa_wq_header_2, srp.xaa_aa_wq_line1, srp.xaa_aa_wq_line2, srp.xaa_aa_wq_line3, srp.xaa_aa_wq_line4) for srp in slanted_product_ids],
            energy_wat_piek=energy_wat_piek,
            select_product=[(sp.id, sp.name, sp.list_price) for sp in select_product],
            solar_product_ids=[(sp.id, sp.name, sp.xaa_aa_wq_header_1, sp.xaa_aa_wq_header_2, sp.xaa_aa_wq_line1, sp.xaa_aa_wq_line2, sp.xaa_aa_wq_line3, sp.xaa_aa_wq_line4, sp.xaa_aa_watt_piek, sp.list_price) for sp in solar_product_ids],
        )

    @http.route(['/formulier/pv/quote_create'], type='json', auth="user", methods=['POST'], website=True)
    def online_quote_create(self, quoteData, formulier_id, eval_quote,**kw):
        """ Create quote for PV type PF from online PF"""

        Product = request.env['product.product'].sudo()
        hours,hours_cost,hours_sales,overhead_total,overhead_sale_total=1,0,0,0,0
        commission_cost = 0
        range_amount = 0
        # if quoteData['xaa_aa_need_discount_2'] == 'ja':
        #     if quoteData['xaa_aa_amount_range']:
        #          get_amount = int(quoteData['xaa_aa_amount_range'])
        #          if get_amount > 0:
        #             range_amount = get_amount / 2

        if quoteData['xaa_aa_installation_time'] == '4 Hours':
            hours = 4
        elif quoteData['xaa_aa_installation_time'] == '8 Hours':
            hours = 8
        elif quoteData['xaa_aa_installation_time'] == '12 Hours':
            hours = 12
        elif quoteData['xaa_aa_installation_time'] == '16 Hours':
            hours = 16
        elif quoteData['xaa_aa_installation_time'] == '24 Hours':
            hours = 24
        elif quoteData['xaa_aa_installation_time'] == '30 Hours':
            hours = 30
        elif quoteData['xaa_aa_installation_time'] == '32 Hours':
            hours = 32
        elif quoteData['xaa_aa_installation_time'] == '36 Hours':
            hours = 36
        elif quoteData['xaa_aa_installation_time'] == '40 Hours':
            hours = 40
        if quoteData['solar_qty'] or hours:
            if hours:
                sale_conf = request.env['sale.line.config'].sudo().search([
                    ('xaa_aa_qty', '=', hours),
                    ('xaa_aa_formulier_type', '=', 'formulier_three')], limit=1)
            else:
                sale_conf = request.env['sale.line.config'].sudo().search([
                    ('xaa_aa_qty', '=', int(quoteData['solar_qty'])),
                    ('xaa_aa_formulier_type', '=', 'formulier_three')], limit=1)
            if sale_conf:
                hours_cost = sale_conf.xaa_aa_team_cost
                hours_sales = sale_conf.xaa_aa_team_sale
                overhead_total = sale_conf.xaa_aa_overhead_total
                overhead_sale_total = sale_conf.xaa_aa_sales_overhead_total
                commission_cost = sale_conf.xaa_aa_commission
        user = request.env.user
        if eval_quote:
            SaleOrder = request.env['sale.order.temp'].sudo()
            SaleOrderLine = request.env['sale.order.line.temp'].sudo()
        else:
            SaleOrder = request.env['sale.order'].sudo()
            SaleOrderLine = request.env['sale.order.line'].sudo()

        # domain for product search
        if user.has_group('base.group_user'):
            domain = ['|',('xaa_aa_show_product_user','=','yes'),'|',
                ('xaa_aa_show_product_user','=',False),
                ('xaa_aa_product_portal_user','in', user.id)]
        else:
            domain = ['|',('xaa_aa_product_portal_user','in', user.id),('xaa_aa_show_product_user','=',False)]

        if formulier_id and quoteData:
            formulier_id = request.env['question.formulier'].sudo().browse(int(formulier_id))
            if formulier_id.xaa_aa_partner_id:
                # product_id = request.env['product.product'].browse(int(product))
                quote = SaleOrder.create({
                        'partner_id': formulier_id.xaa_aa_partner_id.id,
                        'xaa_aa_formulier_id': formulier_id.id,
                        'opportunity_id': formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.id,
                        # 'lead_id': que_id.lead_id and que_id.lead_id.id,
                        'sale_order_template_id': quoteData['xaa_aa_quote_template_id'],
                        'xaa_aa_rendement': quoteData['xaa_aa_location_correction'] or 0,
                        'xaa_aa_show_only_total': True,
                        'global_discount': True,
                        'discount_type': 'fixed',
                    })
                quote.user_id = request.env.user.id
                quote.onchange_sale_order_template_id()
                quote.fill_drawing_images()
                vat_id = Product.search(domain+[
                    ('xaa_aa_product_type', '=', 'BTW teruggave')],
                    order='xaa_aa_priority', limit=1)
                if vat_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': vat_id.id,
                        'product_uom_qty': 1,
                        'discount': 100,
                    })
                if quoteData['xaa_aa_solar_product']:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_solar_product'],
                        'product_uom_qty': quoteData['solar_qty'],
                        # 'price_unit': quoteData['xaa_aa_panel_price'],
                    })
                if quoteData['xaa_aa_need_optimiser'] == 'ja' and quoteData['xaa_aa_optimiser_product']:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_optimiser_product'],
                        'product_uom_qty': quoteData['optimiser_qty'],
                        # 'price_unit': quoteData['xaa_aa_optimisers_price'],
                    })
                if quoteData['xaa_aa_need_converter'] == 'ja' and quoteData['xaa_aa_converter_product']:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_converter_product'],
                        'product_uom_qty': quoteData['converter_qty'],
                        # 'price_unit': quoteData['xaa_aa_converter_price'],
                    })
                if quoteData['xaa_aa_pf_select_roof'] in ['Flat Roof','Mix Roof'] and quoteData['xaa_aa_flat_roof_product']:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_flat_roof_product'],
                        'product_uom_qty': quoteData['flat_roof_qty'],
                    })
                if quoteData['xaa_aa_pf_select_roof'] in ['Slanted Roof','Mix Roof'] and quoteData['xaa_aa_slanted_roof_product']:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_slanted_roof_product'],
                        'product_uom_qty': quoteData['slanted_roof_qty'],
                    })
                stekkers_id = Product.search(domain+[
                    ('xaa_aa_product_type', '=', 'Stekkers')],
                    order='xaa_aa_priority', limit=1)
                if stekkers_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': stekkers_id.id,
                        'product_uom_qty': 1,
                    })
                # if quoteData['xaa_aa_need_discount_2'] == 'ja':
                #     product_id = Product.search([('name','=','Korting')], limit=1)
                #     if product_id:
                #         SaleOrderLine.create({
                #             'order_id': quote.id,
                #             'product_id': product_id.id,
                #             'price_unit': -int(quoteData['xaa_aa_amount_range']),
                #             'product_uom_qty': 1,
                #         })
                if quoteData['xaa_aa_need_discount'] == 'ja':
                    quote.acs_discount_amount = int(quoteData['xaa_aa_discount_qty'])
                    product_id = request.env.user.company_id.sale_discount_product_id
                    if product_id:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': product_id.id,
                            'price_unit': int(quoteData['xaa_aa_discount_qty']),
                            'purchase_price': 0,
                            'product_uom_qty': 1,
                            'discount': 0.0,
                            'sequence': 100,
                        })
                schouw_id = request.env.ref('project_formulier_quote.schouw_product',False)
                if quoteData['xaa_aa_need_schouw'] == 'ja' and schouw_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': schouw_id.sudo().id,
                        'product_uom_qty': 1,
                    })
                if quoteData['xaa_aa_installation_time']:
                    installation_product = Product.search([('name', 'ilike', 'Montage kosten zonnepanelen')], limit=1)
                    if installation_product:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': installation_product.id,
                            'product_uom_qty': 1,
                            'price_unit': hours_sales or installation_product.lst_price,
                            'purchase_price': hours_cost or installation_product.standard_price,
                        })
                # material_id = Product.search(domain+[
                # ('xaa_aa_product_type', '=', 'Overige Materialen')], order='xaa_aa_priority', limit=1)
                # if material_id:
                    # SaleOrderLine.create({
                        # 'order_id': quote.id,
                        # 'product_id': material_id.id,
                        # 'product_uom_qty': 1,
                    # })
                # if quoteData['xaa_aa_installation_time'] and quote.sale_order_template_id:
                #     if quote.sale_order_template_id.xaa_aa_task_product_id:
                #         SaleOrderLine.create({
                #             'order_id': quote.id,
                #             'product_id': quote.sale_order_template_id.xaa_aa_task_product_id.id,
                #             'product_uom_qty': hours,
                #         })
                if quoteData['xaa_aa_installation_time']:
                    task_product = Product.search([
                        ('name','ilike','Projectbegeleiding PV')], limit=1)
                    if task_product:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': task_product.id,
                            'product_uom_qty': hours,
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
                if quoteData['xaa_aa_pv_need_custm_extra_product'] in ['ja 1','ja 2', 'ja 3']:
                    custom_extra_product = Product.search([
                        ('xaa_aa_product_type', '=', 'Extra option iso')], limit=1)
                    if custom_extra_product:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': custom_extra_product.id,
                            'name': quoteData['xaa_aa_pv_extra_product_description'] or custom_extra_product.name,
                            'product_uom_qty': 1,
                            'price_unit': quoteData['xaa_aa_pv_extra_product_sale'] or custom_extra_product.lst_price,
                            'purchase_price': quoteData['xaa_aa_pv_extra_product_cost'] or custom_extra_product.standard_price,
                        })
                        if quoteData['xaa_aa_pv_need_custm_extra_product'] in ['ja 2', 'ja 3']:
                            SaleOrderLine.create({
                                'order_id': quote.id,
                                'product_id': custom_extra_product.id,
                                'name': quoteData['xaa_aa_pv_extra_product_description_two'] or custom_extra_product.name,
                                'product_uom_qty': 1,
                                'price_unit': quoteData['xaa_aa_pv_extra_product_sale_two'] or custom_extra_product.lst_price,
                                'purchase_price': quoteData['xaa_aa_pv_extra_product_cost_two'] or custom_extra_product.standard_price,
                            })
                        if quoteData['xaa_aa_pv_need_custm_extra_product'] == 'ja 3':
                            SaleOrderLine.create({
                                'order_id': quote.id,
                                'product_id': custom_extra_product.id,
                                'name': quoteData['xaa_aa_pv_extra_product_description_three'] or custom_extra_product.name,
                                'product_uom_qty': 1,
                                'price_unit': quoteData['xaa_aa_pv_extra_product_sale_three'] or custom_extra_product.lst_price,
                                'purchase_price': quoteData['xaa_aa_pv_extra_product_cost_three'] or custom_extra_product.standard_price,
                            })
                if quote.sale_order_template_id:
                    quote.fill_calculations_value()
                total_cost = 0
                # currency = quote.currency_id or quote.company_id.currency_id
                if quoteData['xaa_aa_discount_qty']:
                    commission_cost += int(quoteData['xaa_aa_discount_qty'])
                for line in quote.order_line:
                    total_cost += line.product_id.standard_price*line.product_uom_qty
                formulier_id.write({'xaa_aa_pv_cost_price_total': total_cost or quote.amount_untaxed})
                quote.xaa_aa_cost_price_total = total_cost or quote.amount_untaxed
                quote.xaa_aa_commission = commission_cost
                if eval_quote:
                    if not user.xaa_aa_show_score:
                        return ['{0:.2f}'.format(quote.amount_untaxed), '{0:.2f}'.format(commission_cost)]
                    else:
                        margin_per = '{0:.2f}'.format(quote.margin / 100)
                        return [margin_per+' %','€ '+ '{0:.2f}'.format(quote.amount_untaxed),'{0:.2f}'.format(commission_cost)]
                else:
                    quote.state = 'sent'
                    return quote.preview_sale_order()
        return True


    @http.route(['/order/snippet/pv_dynamic_value'], type='json', auth="public", website=True, csrf=False)
    def pv_dynamic_value(self, sale_id):
        order = request.env['sale.order'].sudo().browse(sale_id)
        data = {}
        if order and order.xaa_aa_formulier_id:
            formulier_id = order.xaa_aa_formulier_id
            data.update({'formulier_id': formulier_id.id,
                        'xaa_aa_photo_roof_1': formulier_id.xaa_aa_photo_roof_1 or False,
                        'xaa_aa_photo_roof_2': formulier_id.xaa_aa_photo_roof_2 or False,
                        'xaa_aa_inverter_in_operation': formulier_id.xaa_aa_inverter_in_operation or False,
                        'xaa_aa_cupboard_opened': formulier_id.xaa_aa_cupboard_opened or False,
                        'xaa_aa_inverter_serial_number': formulier_id.xaa_aa_inverter_serial_number or False,
                        'xaa_aa_optimizers_serial_number': formulier_id.xaa_aa_optimizers_serial_number or False,
                        })
            return data
        else:
            data.update({'formulier_id': False,})
            return data
