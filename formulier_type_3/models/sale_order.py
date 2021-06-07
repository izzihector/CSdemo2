# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    xaa_aa_agreements_with_client = fields.Text(
        related="xaa_aa_formulier_id.xaa_aa_agreements_with_client",
        string='Other special agreements with client')

    @api.model
    def fill_drawing_images(self):
        """ auto update snippet value and custom code value"""

        res = super(SaleOrder, self).fill_drawing_images()
        footer = ""
        description = ""
        imgDict = {}
        formulier_id = self.xaa_aa_formulier_id
        if self.website_description:
            description = self.website_description.encode('utf-8')
        if self.xaa_aa_website_desc_footer:
            footer = self.xaa_aa_website_desc_footer.encode('utf-8')

        if formulier_id and (description or footer):
            if formulier_id.xaa_aa_image:
                bannerKey = '<img src="/formulier_type_3/static/src/images/blank_image.jpg" class="img img-fluid" alt="Project Formulier" id="level_measurement_img" loading="lazy">' 
                imgDict.update({bannerKey:
                    '<img class="img img-fluid" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_image' + ' ' + 'alt="Project Formulier" id="level_measurement_img" loading="lazy">'})

            if formulier_id.xaa_aa_formulier_type == 'formulier_three':
                if formulier_id.xaa_aa_photo_roof_1:
                    imgDict.update({'<img class="img img-fluid" src="/formulier_type_3/static/src/images/blank_image.jpg" alt="Overview Photo Roof 1 Image" id="photo_roof_1_img_id" loading="lazy">':
                                    '<img class="img img-fluid center-block" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_photo_roof_1' + ' ' + ' alt="Overview Photo Roof 1 Image" id="photo_roof_1_img_id"/>'})
                if formulier_id.xaa_aa_photo_roof_2:
                    imgDict.update({'<img class="img img-fluid" src="/formulier_type_3/static/src/images/blank_image.jpg" alt="Overview Photo Roof 2 Image" id="photo_roof_2_img_id" loading="lazy">':
                                    '<img class="img img-fluid center-block" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_photo_roof_2' + ' ' + ' alt="Overview Photo Roof 2 Image" id="photo_roof_2_img_id"/>'})
                if formulier_id.xaa_aa_inverter_in_operation:
                    imgDict.update({'<img class="img img-fluid" src="/formulier_type_3/static/src/images/blank_image.jpg" alt="Inverter In Operation Image" id="Inverter_in_operation_id" loading="lazy">':
                                    '<img class="img img-fluid center-block" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_inverter_in_operation' + ' ' + ' alt="Inverter In Operation Image" id="Inverter_in_operation_id"/>'})
                if formulier_id.xaa_aa_cupboard_opened:
                    imgDict.update({'<img class="img img-fluid" src="/formulier_type_3/static/src/images/blank_image.jpg" alt="Cupboard Opened Image" id="cupboard_opened_id" loading="lazy">':
                                    '<img class="img img-fluid center-block" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_cupboard_opened' + ' ' + ' alt="Cupboard Opened Image" id="cupboard_opened_id"/>'})
                if formulier_id.xaa_aa_inverter_serial_number:
                    imgDict.update({'<img class="img img-fluid" src="/formulier_type_3/static/src/images/blank_image.jpg" alt="Inverter Serial No Image" id="inverter_serial_number_id" loading="lazy">':
                                    '<img class="img img-fluid center-block" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_inverter_serial_number' + ' ' + ' alt="Inverter Serial No Image" id="inverter_serial_number_id"/>'})
                if formulier_id.xaa_aa_optimizers_serial_number:
                    imgDict.update({'<img class="img img-fluid" src="/formulier_type_3/static/src/images/blank_image.jpg" alt="Photo serial numbers optimizers Image" id="optimizers_serial_number_id" loading="lazy">':
                                    '<img class="img img-fluid center-block" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_optimizers_serial_number' + ' ' + ' alt="Photo serial numbers optimizers Image" id="optimizers_serial_number_id"/>'})

            if description:
                for key, val in imgDict.items():
                    description = description.replace(
                        key.encode('utf-8'), val.encode('utf-8'))
                self.website_description = description
            if footer:
                for key, val in imgDict.items():
                    footer = footer.replace(
                        key.encode('utf-8'), val.encode('utf-8'))
                self.xaa_aa_website_desc_footer = footer
        return self.website_description


    def add_formulier_lines(self):
        if self.xaa_aa_formulier_type == 'formulier_three':
            panel_line = False
            for line in self.order_line:
                if line.product_id.categ_id.name in ['Solar Panel','Zonnepanelen']:
                    panel_line = line
            if panel_line:
                hours=False
                sale_conf = self.env['sale.line.config'].search([
                    ('xaa_aa_formulier_type','=','formulier_three'),
                    ('xaa_aa_qty','=',panel_line.product_uom_qty)],limit=1)
                if sale_conf:
                    hours = sale_conf.xaa_aa_qty_hours
                ctx = {
                    'default_xaa_aa_sale_id': self.ids[0],
                    'default_xaa_aa_qty_hours': hours,
                    'default_xaa_aa_formulier_type': 'formulier_three',
                    'default_xaa_aa_product_qty': panel_line.product_uom_qty,
                }
                view_id = self.env.ref('formulier_quote_set_lines.view_sale_line_form', False)
                if view_id:
                    return {
                        'type': 'ir.actions.act_window',
                        'view_mode': 'form',
                        'res_model': 'sale.line.config.wizard',
                        'views': [(view_id.id, 'form')],
                        'view_id': view_id.id,
                        'target': 'new',
                        'context': ctx,
                    }
        else:
            return super(SaleOrder, self).add_formulier_lines()


class ProjectTask(models.Model):
    _inherit = "project.task"

    xaa_aa_agreements_with_client = fields.Text(
        related="xaa_aa_formulier_id.xaa_aa_agreements_with_client",
        string='Other special agreements with client')

