# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _, tools
import re

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    xaa_aa_formulier_id = fields.Many2one(related='order_id.xaa_aa_formulier_id',
        string='Project Formulier')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_default_formulier(self):
        opportunity_id = self.env.context.get('default_opportunity_id') or False
        if opportunity_id:
            lead_id = self.env['crm.lead'].browse(opportunity_id)
            return lead_id.xaa_aa_formulier_id.id

    xaa_aa_formulier_id = fields.Many2one('question.formulier',
        default=_get_default_formulier, string='Project Formulier')
    xaa_aa_soort = fields.Selection(string='Soort', selection=[('aanbouw', 'aanbouw'),
        ('hoek', 'hoek'), ('gevel', 'kopgevel'), ('groot deel', 'groot deel')],
        default='aanbouw')

    @api.onchange('opportunity_id')
    def onchange_opportunity(self):
        if self.opportunity_id:
            self.user_id = self.opportunity_id.user_id and self.opportunity_id.user_id.id or False

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if res.sale_order_template_id:
            res.fill_drawing_images()
        oppo = res.opportunity_id
        if oppo:
            res.user_id = oppo.user_id.id or self.env.user.id
            if oppo.xaa_aa_formulier_id:
                res.xaa_aa_formulier_id = oppo.xaa_aa_formulier_id.id
                res.xaa_aa_formulier_id.xaa_aa_date_report = res.create_date.date()
                res.xaa_aa_formulier_id.xaa_aa_state = 'task'
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if vals.get('sale_order_template_id'):
            self.fill_drawing_images()
        if vals.get('opportunity_id'):
            oppo = self.opportunity_id
            if oppo:
                self.user_id = oppo.user_id.id or self.env.user.id
                if oppo.xaa_aa_formulier_id:
                    self.xaa_aa_formulier_id = oppo.xaa_aa_formulier_id.id
                    self.xaa_aa_formulier_id.xaa_aa_state = 'task'
        return res

    @api.model
    def fill_drawing_images(self):
        imgDict = {}
        footer = ""
        description = ""
        f_variables = ""
        c_variables = ""
        o_variables = ""
        if self.website_description:
            description = self.website_description.encode('utf-8')
        if self.xaa_aa_website_desc_footer:
            footer = self.xaa_aa_website_desc_footer.encode('utf-8')

        # custom object replacement for sale order,project formulier fields value 
        if description:
            c_variables = re.findall(b'\${custom:.*?}', description)
            if self.xaa_aa_formulier_id:
                f_variables = re.findall(b'\${formulier:.*?}', description)
            if self.opportunity_id:
                o_variables = re.findall(b'\${opportunity:.*?}', description)
        if footer:
            c_variables.extend(re.findall(b'\${custom:.*?}', footer))
            if self.xaa_aa_formulier_id:
                f_variables.extend(re.findall(b'\${formulier:.*?}', footer))
            if self.opportunity_id:
                o_variables.extend(re.findall(b'\${opportunity:.*?}', footer))

        if c_variables:
            for custom in list(set(c_variables)):
                custom_object = custom.decode('utf-8')
                field = custom_object.split('}')[0][16:]
                if field in self._fields:
                    value = self.read([field])
                    if value[0].get(field):
                        if field == 'amount_total':
                            imgDict.update(
                                {custom_object: str("{:.2f}".format(value[0].get(field)))})
                        elif type(value[0].get(field)) is tuple:
                            imgDict.update(
                                {custom_object: str(value[0].get(field)[1])})
                        else:
                            imgDict.update(
                                {custom_object: str(value[0].get(field))})
                    else:
                        imgDict.update({custom_object: ''})

        if o_variables:
            for oppo in list(set(o_variables)):
                oppo_object = oppo.decode('utf-8')
                field = oppo_object.split('}')[0][21:]
                if field == 'salutation':
                    salutation = 'Geachte '
                    if self.opportunity_id.title:
                        salutation = salutation + self.opportunity_id.title.name
                    else:
                        salutation = salutation + 'heer/mevrouw'
                    imgDict.update(
                                {oppo_object: salutation})
                if field in self.opportunity_id._fields:
                    value = self.opportunity_id.read([field])
                    if value[0].get(field):
                        if type(value[0].get(field)) is tuple:
                            imgDict.update(
                                {oppo_object: str(value[0].get(field)[1])})
                        else:
                            imgDict.update(
                                {oppo_object: str(value[0].get(field))})
                    else:
                        imgDict.update({oppo_object: ''})
        if f_variables:
            for custom in  list(set(f_variables)):
                custom_object = custom.decode('utf-8')
                field = custom_object.split('}')[0][19:]
                if field in self.xaa_aa_formulier_id._fields:
                    value = self.xaa_aa_formulier_id.read([field])
                    if value[0].get(field):
                        if type(value[0].get(field)) is tuple:
                            imgDict.update(
                                {custom_object: str(value[0].get(field)[1])})
                        else:
                            imgDict.update(
                                {custom_object: str(value[0].get(field))})
                    else:
                         imgDict.update({custom_object: ''})
            dutch_date = {'January': 'januari', 'February': 'februari',
                'March': 'maart', 'May': 'mei', 'June': 'juni', 'July': 'juli',
                'August': 'augustus', 'October': 'oktober', 'Monday': 'maandag',
                'Tuesday': 'dinsdag', 'Wednesday': 'woensdag', 'Thursday': 'donderdag',
                'Friday': 'vrijdag', 'Saturday': 'zaterdag', 'Sunday': 'zondag'}
            if self.xaa_aa_formulier_id.xaa_aa_lead_id and self.xaa_aa_formulier_id.xaa_aa_lead_id.xaa_aa_soort:
                imgDict.update({'${formulier:object.soort}': str(
                    self.xaa_aa_formulier_id.xaa_aa_lead_id.xaa_aa_soort)})
            else:
                imgDict.update({'${formulier:object.soort}': ''})
            if self.xaa_aa_formulier_id.xaa_aa_lead_id and self.xaa_aa_formulier_id.xaa_aa_lead_id.user_id:
                imgDict.update({'${formulier:object.salesman}': str(
                    self.xaa_aa_formulier_id.xaa_aa_lead_id.user_id.name)})
            else:
                imgDict.update({'${formulier:object.salesman}': ''})
            if self.xaa_aa_formulier_id.xaa_aa_date_opportunity:
                date_string = self.xaa_aa_formulier_id.xaa_aa_date_opportunity.strftime('%A %d %B')
                if self._context.get('lang') == 'nl_NL':
                    for i, j in dutch_date.items():
                        date_string = date_string.replace(i,j)
                imgDict.update({'${formulier:object.date_opportunity}': date_string})
            else:
                imgDict.update({'${formulier:object.date_opportunity}': ''})

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


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    xaa_aa_template_video_ids = fields.One2many('order.video', 'xaa_aa_order_template_id', string='Video')


class OrderTemplateVideo(models.Model):
    """ new model for add videos in sale order template"""

    _inherit = 'order.video'

    xaa_aa_order_template_id = fields.Many2one('sale.order.template', 'Related Template', copy=True, readonly=True)
