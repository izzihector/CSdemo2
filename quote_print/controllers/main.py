# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

import re

from odoo import http
from odoo.http import request
from odoo.addons.sale.controllers.portal import CustomerPortal


class customSaleQuote(CustomerPortal):

    @http.route(['/my/orders/<int:order_id>'], type='http', auth="public", website=True)
    def portal_order_page(self, order_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type='pdf', report_ref='quote_print.report_web_quotation_custom', download=download)
        result = super(customSaleQuote, self).portal_order_page(order_id, report_type=report_type, access_token=access_token, message=message, download=download, **kw)
        if access_token:
            order = request.env['sale.order'].sudo().search([('id', '=', order_id), ('access_token', '=', access_token)])
        else:
            order = request.env['sale.order'].search([('id', '=', order_id)])

        if report_type == 'pdf':
            return result
        if not order:
            return result

        if hasattr(result, 'render'):
            renderedResult = result.render()
        elif hasattr(result, 'replace'):
            renderedResult = result
        else:
            return result

        variables = re.findall(b'\${custom:.*?}', renderedResult)
        if not variables:
            return result

        object = order
        for variable in variables:
            value = eval(variable[9:-1])
            if isinstance(value, (int, float, list, tuple, dict)):
                try:
                    # There are uncertain possible data. So making generic and ignore issue.
                    try:
                        value = str(value).encode("utf-8").decode("utf-8")
                    except:
                        value = str(value).decode("utf-8")
                except:
                    print ('Invalid Data')
                    value = u''
            renderedResult = renderedResult.replace(variable, value.encode('utf-8'))
        return renderedResult

    @http.route("/online_quote/send_by_mail", type='json', auth="public", website=True)
    def send_by_mail(self, order_id, **post):
        ir_model_data = request.env['ir.model.data'].sudo()
        Mail_Message = request.env['mail.compose.message'].sudo()
        vals = dict()
        order = request.env['sale.order'].sudo().browse(int(order_id))
        try:
            if order.sale_order_template_id and order.sale_order_template_id.mail_template_id:
                template_id = order.sale_order_template_id.mail_template_id.id or False
            else:
                template_id = ir_model_data.get_object_reference('sale', 'email_template_edi_sale')[1]
        except ValueError:
            template_id = False
        vals.update({
            'model': 'sale.order',
            'res_id': order.ids[0],
            'template_id': template_id,
            'composition_mode': 'comment',
            'email_from': order.company_id.email,
        })
        mail_id = Mail_Message.create(vals)
        update_values = mail_id.onchange_template_id(template_id, vals['composition_mode'], order._name, vals.get('res_id'))['value']
        mail_id.write(update_values)
        if order and order.sale_order_template_id and order.sale_order_template_id.xaa_aa_pdf_attachment:
            res = request._cr.execute('''
                SELECT id
                FROM ir_attachment
                WHERE res_model = 'sale.order.template'
                  AND res_id = %s
                  AND res_field = 'xaa_aa_pdf_attachment'
                ''' % (order.sale_order_template_id.id))
            res = request._cr.fetchall()
            new_attachment_ids = []
            for attachment_id in mail_id.attachment_ids:
                new_attachment_ids.append(attachment_id.id)
            new_attachment_ids.append(res[0][0])
            mail_id.attachment_ids = [(6, 0, new_attachment_ids)]
        mail_id.action_send_mail()
        stage = request.env.ref('opportunity_from_quote.stage_lead6')
        if stage and order.opportunity_id:
            if order.opportunity_id.stage_id.id != stage.id:
                order.opportunity_id.stage_id = stage.id
        return True
