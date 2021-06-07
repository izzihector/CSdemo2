# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

import os
import re
import base64
import tempfile
from contextlib import closing
from PyPDF2 import PdfFileWriter, PdfFileReader
from logging import getLogger

from odoo import api, fields, models
from odoo.addons.quote_print.caretutils import listutils
from datetime import datetime, timedelta
from odoo.exceptions import UserError

_logger = getLogger(__name__)

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    xaa_aa_website_desc_footer = fields.Html('Template Footer', translate=True)
    xaa_aa_website_desc_footer_bellow = fields.Html('Template Footer Below', translate=True)
    xaa_aa_show_only_total = fields.Boolean('Show Only Total', default=True)
    xaa_aa_cover_image = fields.Binary("Cover Image", store=True)
    xaa_aa_close_image = fields.Binary('Closing Image')


    @api.depends('order_line.margin', 'amount_untaxed')
    def _compute_margin(self):
        if not all(self._ids):
            for order in self:
                order.margin = sum(order.order_line.mapped('margin'))
                total_margin_per = 0
                for line in order.order_line:
                    total_margin_per += line.purchase_price * line.product_uom_qty
                if total_margin_per and order.margin:
                    order.margin_percent = order.margin/total_margin_per
                else:
                    order.margin_percent = 1
        else:
            self.env["sale.order.line"].flush(['margin'])
            # On batch records recomputation (e.g. at install), compute the margins
            # with a single read_group query for better performance.
            # This isn't done in an onchange environment because (part of) the data
            # may not be stored in database (new records or unsaved modifications).
            grouped_order_lines_data = self.env['sale.order.line'].read_group(
                [
                    ('order_id', 'in', self.ids),
                ], ['margin', 'order_id'], ['order_id'])
            mapped_data = {m['order_id'][0]: m['margin'] for m in grouped_order_lines_data}
            for order in self:
                order.margin = mapped_data.get(order.id, 0.0)
                total_margin_per = 0
                for line in order.order_line:
                    total_margin_per += line.purchase_price * line.product_uom_qty
                if total_margin_per and order.margin:
                    order.margin_percent = order.margin/total_margin_per
                else:
                    order.margin_percent = 1

    def action_quotation_send(self):
        # TODO: Dhaval
        ''' this method use to set email template which is set in Quotation Template  '''
        if not self.sale_order_template_id:
            raise UserError('Please add Quotation Template!!!.')
        res = super(SaleOrderInherit, self).action_quotation_send()
        if self.sale_order_template_id and self.sale_order_template_id.mail_template_id:
            res['context']['default_template_id'] = self.sale_order_template_id.mail_template_id.id or False
        if self.state == 'sale':
            confirmed_mail = self.env.ref('sale.mail_template_sale_confirmation', False)
            if confirmed_mail:
                res['context']['default_template_id'] = confirmed_mail.id
        task_product = self.env['sale.order.line'].search([
            ('order_id','=',self.id),('product_id.categ_id.name','ilike','Projectbegeleiding')])
        if not task_product.ids:
            raise UserError('Please add Projectbegeleiding product!!!.')
        return res

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id(self):

        if not self.sale_order_template_id:
            self.require_signature = self._get_default_require_signature()
            self.require_payment = self._get_default_require_payment()
            return

        template = self.sale_order_template_id.with_context(lang=self.partner_id.lang)

        # --- first, process the list of products from the template
        if not self.order_line:
            order_lines = [(5, 0, 0)]
            for line in template.sale_order_template_line_ids:
                data = self._compute_line_data_for_template_change(line)

                if line.product_id:
                    price = line.product_id.lst_price
                    discount = 0

                    if self.pricelist_id:
                        pricelist_price = self.pricelist_id.with_context(uom=line.product_uom_id.id).get_product_price(line.product_id, 1, False)

                        if self.pricelist_id.discount_policy == 'without_discount' and price:
                            discount = max(0, (price - pricelist_price) * 100 / price)
                        else:
                            price = pricelist_price

                    data.update({
                        'price_unit': price,
                        'discount': discount,
                        'product_uom_qty': line.product_uom_qty,
                        'product_id': line.product_id.id,
                        'product_uom': line.product_uom_id.id,
                        'customer_lead': self._get_customer_lead(line.product_id.product_tmpl_id),
                    })

                order_lines.append((0, 0, data))

            self.order_line = order_lines
            self.order_line._compute_tax_id()

        # then, process the list of optional products from the template
        if not self.sale_order_option_ids:
            option_lines = [(5, 0, 0)]
            for option in template.sale_order_template_option_ids:
                data = self._compute_option_data_for_template_change(option)
                option_lines.append((0, 0, data))

            self.sale_order_option_ids = option_lines

        if template.number_of_days > 0:
            self.validity_date = fields.Date.context_today(self) + timedelta(template.number_of_days)

        self.require_signature = template.require_signature
        self.require_payment = template.require_payment

        if template.note:
            self.note = template.note
        self.website_description = template.website_description
        self.xaa_aa_website_desc_footer = template.xaa_aa_website_desc_footer
        self.xaa_aa_website_desc_footer_bellow = template.xaa_aa_website_desc_footer_bellow
        self.xaa_aa_cover_image = template.xaa_aa_cover_image
        self.xaa_aa_close_image = template.xaa_aa_close_image

    def get_quote_print_pdf(self):
        return self.env.ref('quote_print.report_web_quotation_custom').report_action(self)


class mailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.onchange('template_id')
    def onchange_template_id_wrapper(self):
        """owrwrite this mehod to display SO template's pdf attachment in mail
           compose message wizard and send that attachment with mail."""
        result = super(mailComposeMessage, self).onchange_template_id_wrapper()
        if self.env.context.get('active_model') and self.env.context.get('active_model') == 'sale.order':
            order = self.env['sale.order'].browse(self.env.context['active_id'])
            if order and order.sale_order_template_id and order.sale_order_template_id.xaa_aa_pdf_attachment:
                res = self._cr.execute('''
                    SELECT id
                    FROM ir_attachment
                    WHERE res_model = 'sale.order.template'
                      AND res_id = %s
                      AND res_field = 'xaa_aa_pdf_attachment'
                    ''' % (order.sale_order_template_id.id))
                res = self._cr.fetchall()
                for attachment in res:
                    if attachment:
                        att_rec = self.env['ir.attachment'].browse(attachment[0])
                        if att_rec:
                            if att_rec.name.find('.')==-1:
                                att_rec.write({'name': att_rec.name + '.pdf'})
                            if not att_rec.store_fname:
                                att_rec.write({'store_fname': order.sale_order_template_id.xaa_aa_file_name_pdf})
                new_attachment_ids = []
                for attachment_id in self.attachment_ids:
                    new_attachment_ids.append(attachment_id.id)
                new_attachment_ids.append(res[0][0])
                self.attachment_ids = [(6, 0, new_attachment_ids)]
        return result


class SaleQuoteTemplateInh(models.Model):
    _inherit = 'sale.order.template'

    xaa_aa_website_desc_footer = fields.Html('Template Footer', translate=True)
    xaa_aa_website_desc_footer_bellow = fields.Html('Template Footer Below', translate=True)
    xaa_aa_cover_image = fields.Binary("Cover Image", attachment=True)
    xaa_aa_file_name_cover = fields.Char('File Name')
    xaa_aa_cover_image_pdf = fields.Binary("Cover Image Pdf", attachment=True)
    xaa_aa_report_layout = fields.Selection([
         ('address_only', 'First Page Address Only'),
         ('no_extra_space', 'Start Content From First Page')],
         string='Report Layout')
    xaa_aa_file_name_cover_pdf = fields.Char('Pdf File Name')
    xaa_aa_cover_height = fields.Integer(string="Cover Image Height", default=1031)
    xaa_aa_isfooteradrsimg_first_page = fields.Boolean(
        string="Remove Footer",
        help="Show footer address image on first\
        page when rest pages don't have footer")
    xaa_aa_close_image = fields.Binary('Closing Image', attachment=True)
    xaa_aa_close_height = fields.Integer(string="Closing Image Height", default=1031)
    xaa_aa_file_name_close = fields.Char('Close File Name')
    xaa_aa_close_image_pdf = fields.Binary("Close Image Pdf", attachment=True)
    xaa_aa_file_name_close_pdf = fields.Char('Pdf File name')
    xaa_aa_header_image = fields.Binary("Header Image")
    xaa_aa_file_name_header = fields.Char('Header File name')
    xaa_aa_footer_image = fields.Binary("Footer Image")
    xaa_aa_file_name_footer = fields.Char('Footer File Name')
    xaa_aa_pdf_attachment = fields.Binary('PDF Attachment', attachment=True)
    xaa_aa_file_name_pdf = fields.Char('PDF File Name')
    xaa_aa_hide_pricing_tab = fields.Boolean(string='Hide Pricing Tab')

    @api.model
    def create(self, values):
        result = super(SaleQuoteTemplateInh, self).create(values)
        if result.xaa_aa_cover_image:
            result.generate_pdf()
        if result.xaa_aa_close_image:
            result.generate_pdf()
        return result

    def write(self, values):
        result = super(SaleQuoteTemplateInh, self).write(values)
        if self.xaa_aa_cover_image and values.get('xaa_aa_cover_height'):
            self.generate_pdf()
        if values.get('xaa_aa_cover_image'):
            self.generate_pdf()

        if self.xaa_aa_close_image and values.get('xaa_aa_close_height'):
            self.generate_pdf()
        if values.get('xaa_aa_close_image'):
            self.generate_pdf()
        return result

    def generate_pdf(self):
        if not self.xaa_aa_cover_image:
            self.xaa_aa_cover_image_pdf = None
            self.xaa_aa_file_name_cover_pdf = None
        else:
            #pdf = self.env['ir.actions.report'].sudo()._get_report_from_name('quote_print.report_quote_cover')
            #pdf_bin, _ = pdf.with_context(snailmail_layout=True).render_qweb_pdf(self.id)
            reportAct = self.env.ref('quote_print.report_web_quote_cover')
            if reportAct:
                pdf_bin, _ = reportAct._render_qweb_pdf(docids=self.id)
                self.xaa_aa_cover_image_pdf = base64.b64encode(pdf_bin)
                self.xaa_aa_file_name_cover_pdf = (self.xaa_aa_file_name_cover.split('.')[0] or 'cover') + '.pdf'
        if not self.xaa_aa_close_image:
            self.xaa_aa_close_image_pdf = None
            self.xaa_aa_file_name_close_pdf = None
        else:
            # closePdf = self.env['ir.actions.report'].sudo()._get_report_from_name('quote_print.report_quote_close')
            # closePdf_bin, _ = closePdf.with_context(snailmail_layout=True).render_qweb_pdf(self.id)
            reportCloseAct = self.env.ref('quote_print.report_web_quote_close')
            if reportCloseAct:
                closepdf_bin, _ = reportCloseAct._render_qweb_pdf(docids=self.id)
                self.xaa_aa_close_image_pdf = base64.b64encode(closepdf_bin)
                self.xaa_aa_file_name_close_pdf = (self.xaa_aa_file_name_close.split('.')[0] or 'close') + '.pdf'


class IrActionsReportInh(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def _render_qweb_html(self, docids, data=None):
        html = super(IrActionsReportInh, self)._render_qweb_html(docids, data=data)
        if (self.model != 'sale.order' and
            self.report_name != 'quote_print.report_web_quotation_custom'):
            return html

        variables = re.findall(b'\${custom:.*?}', html[0])
        if not variables:
            return html
        lst = list(html)
        for i, variChunk in enumerate(listutils.chunks(variables, len(variables) / len(docids))):
            docId = docids[i]
            object = self.env['sale.order'].browse(docId)
            for variable in variChunk:
                value = eval(variable[9:-1])
                if isinstance(value, (int, float, list, tuple, dict)):
                    try:
                        # There are uncertain possible data. So making generic and ignore issue.
                        try:
                            value = str(value).encode("utf-8").decode("utf-8")
                        except:
                            value = str(value).decode("utf-8")
                    except:
                        value = u''
                lst[0] = lst[0].replace(variable, value.encode('utf-8'), 1)
        return tuple(lst)

    def _merge_pdf(self, documents):
        """Merge PDF files into one."""
        writer = PdfFileWriter()
        streams = []
        try:
            for document in documents:
                pdfreport = open(document, 'rb')
                streams.append(pdfreport)
                reader = PdfFileReader(pdfreport)
                for page in range(0, reader.getNumPages()):
                    writer.addPage(reader.getPage(page))

            merged_file_fd, merged_file_path = tempfile.mkstemp(
                suffix='.pdf', prefix='report.merged.tmp.')
            with closing(os.fdopen(merged_file_fd, 'wb')) as merged_file:
                writer.write(merged_file)
        finally:
            for stream in streams:
                try:
                    stream.close()
                except Exception:
                    pass
        return merged_file_path

    def _render_qweb_pdf(self, docids, data=None):
        """This method generates and returns pdf version with background of a report.
        """
        temporary_files = []
        pdf = super(IrActionsReportInh, self)._render_qweb_pdf(docids, data=data)
        if (self.model != 'sale.order' and
            self.report_name != 'quote_print.custom_web_quote_print'):
            return pdf
        soId = docids[0] if isinstance(docids, list) else docids
        so = self.env['sale.order'].browse(soId)
        if not so.sale_order_template_id:
            return pdf
        if so.sale_order_template_id.xaa_aa_isfooteradrsimg_first_page:
            self.paperformat_id.sudo().write({'margin_bottom': 23})
        else:
            self.paperformat_id.sudo().write({'margin_bottom': 48})

        cover_image = so.sale_order_template_id.xaa_aa_cover_image
        cover_image_pdf = so.sale_order_template_id.xaa_aa_cover_image_pdf
        if (cover_image and cover_image_pdf and (not so.sale_order_template_id.xaa_aa_report_layout 
            or so.sale_order_template_id.xaa_aa_report_layout in ['address_only','no_extra_space'])):

            writer = PdfFileWriter()
            streams = []
            try:
                report_fd, report_path = tempfile.mkstemp(
                    suffix='.pdf', prefix='report.tmp.')
                temporary_files.append(report_path)
                with closing(os.fdopen(report_fd, 'wb')) as repo:
                    repo.write(pdf[0])
            finally:
                for stream in streams:
                    try:
                        stream.close()
                    except Exception:
                        pass

            cover_image_pdf = base64.decodebytes(cover_image_pdf)
            cover_fd, cover_path = tempfile.mkstemp(
                suffix='.pdf', prefix='report.tmp.')
            temporary_files.append(cover_path)
            with closing(os.fdopen(cover_fd, 'wb')) as repo:
                repo.write(cover_image_pdf)

            mergeFile = self._merge_pdf([cover_path, report_path])
            with open(mergeFile, 'rb') as pdfdocument:
                pdf = pdfdocument.read(), 'pdf'

        close_image = so.sale_order_template_id.xaa_aa_close_image
        close_image_pdf = so.sale_order_template_id.xaa_aa_close_image_pdf
        if close_image and close_image_pdf:
            writer = PdfFileWriter()
            streams = []
            try:
                report_fd, report_path = tempfile.mkstemp(
                    suffix='.pdf', prefix='report.tmp.')
                temporary_files.append(report_path)
                with closing(os.fdopen(report_fd, 'wb')) as repo:
                    repo.write(pdf[0])
            finally:
                for stream in streams:
                    try:
                        stream.close()
                    except Exception:
                        pass

            close_image_pdf = base64.decodebytes(close_image_pdf)
            close_fd, close_path = tempfile.mkstemp(
                suffix='.pdf', prefix='report.tmp.')
            temporary_files.append(close_path)
            with closing(os.fdopen(close_fd, 'wb')) as repo:
                repo.write(close_image_pdf)

            mergeFile = self._merge_pdf([report_path, close_path])
            with open(mergeFile, 'rb') as pdfdocument:
                pdf = pdfdocument.read(), 'pdf'

            # Manual cleanup of the temporary files
        for temporary_file in temporary_files:
            try:
                os.unlink(temporary_file)
            except (OSError, IOError):
                _logger.error('Error when trying to remove file %s' % temporary_file)

        return pdf

    @api.model
    def _run_wkhtmltopdf(
            self,
            bodies,
            header=None,
            footer=None,
            landscape=False,
            specific_paperformat_args=None,
            set_viewport_size=False):

        if self.report_name == 'quote_print.custom_web_quote_print':
            set_viewport_size = True
        res = super(IrActionsReportInh, self)\
            ._run_wkhtmltopdf(
                bodies,
                header,
                footer,
                landscape,
                specific_paperformat_args=specific_paperformat_args,
                set_viewport_size=set_viewport_size
            )
        return res


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends('price_subtotal', 'product_uom_qty', 'purchase_price')
    def _compute_margin(self):
        for line in self:
            line.margin = line.price_subtotal - (line.purchase_price * line.product_uom_qty)
            cost_total = line.purchase_price * line.product_uom_qty
            if cost_total:
                line.margin_percent = line.margin/cost_total
            else:
                line.margin_percent = 1