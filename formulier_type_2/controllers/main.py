# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.project_formulier.controllers.main import ProjectFormulier

class ProjectFormulier(ProjectFormulier):

    @http.route(['/iso_questions_thanks'], type='http', auth="public", website=True)
    def iso_questions_thanks(self, **kw):
        return request.render('formulier_type_2.iso_questions_thanks', {})

    @http.route(['/formulier/iso_quote_infos'],
                type='json', auth="user", methods=['POST'], website=True)
    def iso_quote_infos(self, product_id=0, cavity_thickness=None, spacing=None, **kw):
        """send related and selected product on online PF"""

        Product = request.env['product.product'].sudo()
        selected_product = Product
        isolation_product = Product
        user = request.env.user
        if user.has_group('base.group_user'):
            domain = ['|',('xaa_aa_show_product_user','=','yes'),'|',
                ('xaa_aa_show_product_user','=',False),
                ('xaa_aa_product_portal_user','in', user.id)]
        else:
            domain = ['|',('xaa_aa_product_portal_user','in', user.id),('xaa_aa_show_product_user','=',False)]
        if product_id:
            selected_product = Product.browse(product_id)
        if cavity_thickness:
            isolation_product = Product.search(domain+[('xaa_aa_product_type','=','I am Isolation'),('xaa_aa_tickness_of_wall', '=', cavity_thickness)])
        if spacing:
            if spacing == 'Meer dan 45 cm':
                isolation_product = Product.search(domain+[
                    ('xaa_aa_product_type', 'in', ['ISO floor material 1', 'ISO floor material 2'])], order='xaa_aa_priority')
            else:
                isolation_product = Product.search(domain+[
                    ('xaa_aa_product_type', '=', 'ISO floor material 1')], order='xaa_aa_priority')
        return dict(
            selected_product = [(sp.id, sp.name, sp.list_price) for sp in selected_product],
            isolation_product = [(ip.id, ip.name, ip.xaa_aa_wq_header_1, ip.xaa_aa_wq_header_2, ip.xaa_aa_wq_line1, ip.xaa_aa_wq_line2, ip.xaa_aa_wq_line3, ip.xaa_aa_wq_line4, ip.xaa_aa_watt_piek, ip.list_price) for ip in isolation_product],
        )

    @http.route(['/formulier/iso/quote_create'],
                type='json',auth="user", methods=['POST'], website=True)
    def online_iso_quote_create(self, quoteData, formulier_id, eval_quote,**kw):
        """ Create Quote for ISO type PF from online PF"""

        user = request.env.user
        hours,hours_cost,hours_sales,overhead_total,overhead_sale_total=1,0,0,0,0
        commission_cost = 0

        if quoteData['xaa_aa_iso_installation_time']:
            if quoteData['xaa_aa_iso_installation_time'] == '4 Hours':
                hours = 4
            elif quoteData['xaa_aa_iso_installation_time'] == '8 Hours':
                hours = 8
            elif quoteData['xaa_aa_iso_installation_time'] == '12 Hours':
                hours = 12
            elif quoteData['xaa_aa_iso_installation_time'] == '16 Hours':
                hours = 16
            elif quoteData['xaa_aa_iso_installation_time'] == '24 Hours':
                hours = 24
            elif quoteData['xaa_aa_iso_installation_time'] == '30 Hours':
                hours = 30
            elif quoteData['xaa_aa_iso_installation_time'] == '32 Hours':
                hours = 32
            elif quoteData['xaa_aa_iso_installation_time'] == '36 Hours':
                hours = 36
            elif quoteData['xaa_aa_iso_installation_time'] == '40 Hours':
                hours = 40

        if quoteData['isolation_qty'] or hours:
            if hours:
                sale_conf = request.env['sale.line.config'].sudo().search([
                    ('xaa_aa_qty', '=', hours),
                    ('xaa_aa_formulier_type', '=', 'formulier_two')], limit=1)
            else:
                sale_conf = request.env['sale.line.config'].sudo().search([
                    ('xaa_aa_qty', '=', int(quoteData['isolation_qty'])),
                    ('xaa_aa_formulier_type', '=', 'formulier_two')], limit=1)

            if sale_conf:
                hours_cost = sale_conf.xaa_aa_team_cost
                hours_sales = sale_conf.xaa_aa_team_sale
                overhead_total = sale_conf.xaa_aa_overhead_total
                overhead_sale_total = sale_conf.xaa_aa_sales_overhead_total
                commission_cost = sale_conf.xaa_aa_commission

        if eval_quote:
            SaleOrder = request.env['sale.order.temp'].sudo()
            SaleOrderLine = request.env['sale.order.line.temp'].sudo()
        else:
            SaleOrder = request.env['sale.order'].sudo()
            SaleOrderLine = request.env['sale.order.line'].sudo()
        if formulier_id and quoteData:
            formulier_id = request.env['question.formulier'].sudo().browse(int(formulier_id))
            Product = request.env['product.product'].sudo()
            if formulier_id.xaa_aa_partner_id:
                quote = SaleOrder.create({
                        'partner_id': formulier_id.xaa_aa_partner_id.id,
                        'xaa_aa_formulier_id': formulier_id.id,
                        'opportunity_id': formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.id or False,
                        'xaa_aa_show_only_total': True,
                        'sale_order_template_id': quoteData['xaa_aa_quote_template_id'] or False,
                    })
                quote.user_id = request.env.user.id
                quote.onchange_sale_order_template_id()
                quote.fill_drawing_images()

                if quoteData['xaa_aa_isolation_product']:
                    if quoteData['xaa_aa_kind_of_isolate'] == 'Floor':
                        service_product = Product.search([
                            ('name', 'ilike', 'Aanbrengen vloerisolatie')],
                            limit=1)
                    else:
                        service_product = Product.search([
                            ('name', 'ilike', 'Aanbrengen spouwmuurisolatie')],
                            limit=1)
                    if service_product:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': service_product.id,
                            'product_uom_qty': 1,
                            'purchase_price': hours_cost or service_product.standard_price,
                            'price_unit': hours_sales or service_product.lst_price,
                            # 'price_unit': quoteData['xaa_aa_service_price'],
                        })
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_isolation_product'],
                        'product_uom_qty': quoteData['isolation_qty'] or 1,
                        # 'price_unit': quoteData['xaa_aa_material_price'],
                    })
                certificate_product = Product.search([
                    ('xaa_aa_product_type', '=', 'SKG IKOB Certification payment')],limit=1)
                if certificate_product:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': certificate_product.id,
                        'product_uom_qty': quoteData['isolation_qty'] or 1,
                    })
                if quoteData['xaa_aa_need_ventilation_grid'] == 'ja' and quoteData['xaa_aa_ventilation_product'] and quoteData['xaa_aa_kind_of_isolate'] == 'Cavity':
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_ventilation_product'],
                        'product_uom_qty': quoteData['ventilation_qty'],
                        # 'price_unit': quoteData['xaa_aa_ventilation_price'],
                    })
                if quoteData['xaa_aa_need_cavity_boundary'] == 'ja' and quoteData['xaa_aa_cavity_boundary_product'] and quoteData['xaa_aa_kind_of_isolate'] != 'Floor':
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': quoteData['xaa_aa_cavity_boundary_product'],
                        'product_uom_qty': quoteData['cavity_boundary_qty'],
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
                if quoteData['xaa_aa_need_custm_extra_product'] in ['ja 1','ja 2', 'ja 3'] and quoteData['xaa_aa_kind_of_isolate'] != 'Floor':
                    custom_extra_product = Product.search([
                        ('xaa_aa_product_type', '=', 'Extra option iso')], limit=1)
                    if custom_extra_product:
                        SaleOrderLine.create({
                            'order_id': quote.id,
                            'product_id': custom_extra_product.id,
                            'name': quoteData['xaa_aa_extra_product_description'] or custom_extra_product.name,
                            'product_uom_qty': 1,
                            'price_unit': quoteData['xaa_aa_extra_product_sale'] or custom_extra_product.lst_price,
                            'purchase_price': quoteData['xaa_aa_extra_product_cost'] or custom_extra_product.standard_price,
                        })
                        if quoteData['xaa_aa_need_custm_extra_product'] in ['ja 2', 'ja 3']:
                            SaleOrderLine.create({
                                'order_id': quote.id,
                                'product_id': custom_extra_product.id,
                                'name': quoteData['xaa_aa_extra_product_description_two'] or custom_extra_product.name,
                                'product_uom_qty': 1,
                                'price_unit': quoteData['xaa_aa_extra_product_sale_two'] or custom_extra_product.lst_price,
                                'purchase_price': quoteData['xaa_aa_extra_product_cost_two'] or custom_extra_product.standard_price,
                            })
                        if quoteData['xaa_aa_need_custm_extra_product'] == 'ja 3':
                            SaleOrderLine.create({
                                'order_id': quote.id,
                                'product_id': custom_extra_product.id,
                                'name': quoteData['xaa_aa_extra_product_description_three'] or custom_extra_product.name,
                                'product_uom_qty': 1,
                                'price_unit': quoteData['xaa_aa_extra_product_sale_three'] or custom_extra_product.lst_price,
                                'purchase_price': quoteData['xaa_aa_extra_product_cost_three'] or custom_extra_product.standard_price,
                            })
                schouw_id = request.env.ref('project_formulier_quote.schouw_product',False)
                if quoteData['xaa_aa_need_schouw'] == 'ja' and schouw_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': schouw_id.sudo().id,
                        'product_uom_qty': 1,
                        'discount': 100,
                    })
                if quoteData['xaa_aa_need_discount'] == 'ja':
                    quote.acs_discount_amount = int(quoteData['xaa_aa_discount_qty'])
                    product_id = Product.search([
                        ('name', 'ilike', 'Isolatie toevoeging')],limit=1)
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
                task_product_id = Product.search([
                    ('name', 'ilike', 'Projectbegeleiding Isolatie')],limit=1)
                if task_product_id:
                    SaleOrderLine.create({
                        'order_id': quote.id,
                        'product_id': task_product_id.id,
                        'product_uom_qty': hours,
                    })
                if quote.sale_order_template_id:
                    quote.fill_calculations_value()
                total_cost = 0
                # currency = quote.currency_id or quote.company_id.currency_id
                if quoteData['xaa_aa_discount_qty']:
                    commission_cost += int(quoteData['xaa_aa_discount_qty'])
                for line in quote.order_line:
                    total_cost += line.product_id.standard_price*line.product_uom_qty
                formulier_id.write({'xaa_aa_cost_price_total': total_cost or quote.amount_untaxed})
                quote.xaa_aa_cost_price_total = total_cost or quote.amount_untaxed
                quote.xaa_aa_commission = commission_cost
                if eval_quote:
                    if not user.xaa_aa_show_score:
                        return ['{0:.2f}'.format(quote.amount_untaxed),'{0:.2f}'.format(commission_cost)]
                    else:
                        margin_per = '{0:.2f}'.format(quote.margin / 100)
                        return [margin_per+' %','€ '+ '{0:.2f}'.format(quote.amount_untaxed),'{0:.2f}'.format(commission_cost)]
                else:
                    quote.state = 'sent'
                    return quote.preview_sale_order()
        return True
