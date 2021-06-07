# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

import xlwt
import base64
from io import BytesIO
from datetime import datetime
from xlsxwriter.workbook import Workbook

from odoo import models, fields


class AccountInvoiceReport(models.TransientModel):

    _name = "account.invoice.wizard"
    _description = "Account Invoice Wizard"

    xaa_aa_invoice_ids = fields.Many2many('account.move', string='Invoice')

    def invoice_export_excel(self):
        tax_obj = self.env['account.tax']
        result = []
        if self.xaa_aa_invoice_ids:
            finalperiod = ''
            Omschrijving = ''
            for invoice in self.xaa_aa_invoice_ids:
                result_line = []
                partner = invoice.partner_id and invoice.partner_id.name or ''
                invoicenumber = invoice.name or ''
                dateinvoice = invoice.invoice_date.strftime("%m/%d/%Y, %H:%M:%S") or ''
                Omschrijving = partner + ' ' + invoicenumber + ' ' + dateinvoice
                if invoice.invoice_date:
                    finalperiod = '%02d' % invoice.invoice_date.month
                for line in invoice.invoice_line_ids:
                    taxes = []
                    line_account_name = line.account_id.xaa_aa_ac_code or ''
                    lineacc = line_account_name
                    if line.tax_ids:
                        for tax in line.tax_ids:
                            tax_id = tax_obj.search([('name','=',tax.name),('type_tax_use','=',tax.type_tax_use)])
                            if tax_id:
                                taxes.append(tax_id.id)
                    result_line.append({
                       'journal_id': invoice.journal_id and invoice.journal_id.xaa_aa_ac_code or '',
                       'period': finalperiod or '',
                       'description': line.name or '',
                       'price_subtotal': line.price_subtotal or '',
                       'account_id': lineacc or 10300,
                       'currency_id': invoice.currency_id and invoice.currency_id.name or '',
                       'invoice_line_tax_id': taxes,
                       'move_type': invoice.move_type,
                    })
                result.append({
                   'Omschrijving': Omschrijving or '',
                   'journal_id': invoice.journal_id and invoice.journal_id.xaa_aa_ac_code or '',
                   'partner_id': invoice.partner_id and invoice.partner_id.ref or '',
                   'invoice_number': invoice.name or '',
                   'period': finalperiod or '',
                   'invoice_date': invoice.invoice_date.strftime("%Y-%m-%d") or False,
                   'invoice_date_due': invoice.invoice_date_due.strftime("%Y-%m-%d") or False,
                   'amount_untaxed': invoice.amount_untaxed or '',
                   'amount_total': invoice.amount_total,
                   'amount_residual': invoice.amount_residual,
                   'currency_id': invoice.currency_id and invoice.currency_id.name or '',
                   'invoice_line_ids':result_line,
                   'move_type':invoice.move_type,
                })
                invoice.write({'xaa_aa_export_date':datetime.today(),'xaa_aa_export':True})

        # Create an new Excel file and add a worksheet.
        filename = 'account_export_report.xls'
        workbook = xlwt.Workbook()
        style = xlwt.XFStyle()
        tall_style = xlwt.easyxf('font:height 720;') # 36pt

        # Create a font to use with the style
        font = xlwt.Font()
        font.name = 'Times New Roman'
        font.bold = True
        font.height = 250
        style.font = font
        worksheet = workbook.add_sheet('Sheet 1')

        zero_col = worksheet.col(5)
        zero_col.width = 236 * 60
        worksheet.write(0, 0, 'Header of regel', style)
        worksheet.write(0, 1, 'Dagboek', style)
        worksheet.write(0, 2, 'sub_nr', style)
        worksheet.write(0, 3, 'fact_nr', style)
        worksheet.write(0, 4, 'Periode', style)
        worksheet.write(0, 5, 'Omschrijving', style)
        worksheet.write(0, 6, 'Factuurdatum', style)
        worksheet.write(0, 7, 'Vervaldatum', style)
        worksheet.write(0, 8, 'Grootboek', style)
        worksheet.write(0, 9, 'Bedrag', style)
        worksheet.write(0, 10, 'Valuta code', style)
        worksheet.write(0, 11, 'BTW-code', style)

        row_2 = 1
        header = 0
        for val in result:
            worksheet.write(row_2, 0, header)
            worksheet.write(row_2, 1, val['journal_id'])
            worksheet.write(row_2, 2, val['partner_id'])
            worksheet.write(row_2, 3, val['invoice_number'])
            worksheet.write(row_2, 4, val['period'])
            worksheet.write(row_2, 5, val['Omschrijving'])
            worksheet.write(row_2, 6, val['invoice_date'])
            worksheet.write(row_2, 7, val['invoice_date_due'])
            if val['amount_total'] > val['amount_residual'] or val['move_type'] == 'out_refund':
                worksheet.write(row_2, 9, val['amount_untaxed']*-1)
            else:
                worksheet.write(row_2, 9, val['amount_untaxed'])
            worksheet.write(row_2, 10,val['currency_id'])
            if val['invoice_line_ids']:
                lineheader = 1
                for valline in val['invoice_line_ids']:
                    worksheet.write(row_2+1, 0, lineheader)
                    worksheet.write(row_2+1, 1, valline['journal_id'])
                    worksheet.write(row_2+1, 2, val['partner_id'])
                    worksheet.write(row_2+1, 3, val['invoice_number'])
                    worksheet.write(row_2+1, 4, valline['period'])
                    worksheet.write(row_2+1, 5, valline['description'])
                    worksheet.write(row_2+1, 6, val['invoice_date'])
                    worksheet.write(row_2+1, 7, val['invoice_date_due'])
                    worksheet.write(row_2+1, 8, valline['account_id'])
                    if val['amount_total'] > val['amount_residual'] or val['move_type'] == 'out_refund':
                        worksheet.write(row_2+1, 9, valline['price_subtotal']*-1)
                    else:
                        worksheet.write(row_2+1, 9, valline['price_subtotal'])
                    worksheet.write(row_2+1, 10, valline['currency_id'])
                    if valline['invoice_line_tax_id']:
                        taxname = ''
                        for tax in tax_obj.browse(valline['invoice_line_tax_id']):
                            if tax.amount == 21.000:
                                taxname = taxname + '1' + ','
                            elif tax.amount == 6.000:
                                taxname = taxname + '2' + ','
                            elif tax.amount == 9.000:
                                taxname = taxname + '2' + ','
                            elif tax.amount == 0.000:
                                taxname = '9'
                        worksheet.write(row_2+1, 11, taxname.rstrip(","))
                    else:
                        worksheet.write(row_2+1, 11, '9')
                    lineheader += 1
                    row_2+=1
            row_2+=1

        fp = BytesIO()
        workbook.save(fp)
        export_id = self.env['invoice.excel'].create({'xaa_aa_excel_file': base64.encodestring(fp.getvalue()), 'xaa_aa_file_name': filename})
        fp.close()

        return {
            'view_mode': 'form',
            'res_id': export_id.id,
            'res_model': 'invoice.excel',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
        return True


class invoice_excel(models.TransientModel):
    _name= "invoice.excel"
    _description = "Invoice Excel Report"

    xaa_aa_excel_file = fields.Binary('Excel Report for Invoice')
    xaa_aa_file_name = fields.Char('Excel File', size=64)
