# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _
from random import choice
from string import digits
import base64
import urllib.request


class ProjectFormulier(models.Model):
    _name = "question.formulier"
    _inherit = ['mail.thread'] 
    _description = "Project Formulier for questions form"
    _order = "id desc"
    _rec_name = 'xaa_aa_name'

    def _default_random_pf_access(self):
        pf_access = "".join(choice(digits) for i in range(4))
        return pf_access

    xaa_aa_name = fields.Char('Name')
    active = fields.Boolean(default=True)
    xaa_aa_lead_id = fields.Many2one('crm.lead', string='Lead', readonly=True)
    xaa_aa_image = fields.Binary(tracking=True)
    xaa_aa_partner_id = fields.Many2one('res.partner', string="Customer")
    xaa_aa_created_by = fields.Many2one('res.users', string="Created By")
    xaa_aa_formulier_type = fields.Selection(related='xaa_aa_lead_id.xaa_aa_formulier_type', string="Question Type")
    xaa_aa_state = fields.Selection([('concept', 'Concept'),
                            ('opportunity', 'Opportunity'),
                            ('opportunity_output', 'Opportunity Output'),
                            ('quotation', 'Quotation'),
                            ('quotation_output', 'Quotation Output'),
                            ('task', 'Task'),
                            ('task_output', 'Task Output'),
                            ('done', 'Done'),],
                             string='status', default='concept', required=True, tracking=True)
    xaa_aa_street = fields.Char(tracking=True)
    xaa_aa_street2 = fields.Char(tracking=True)
    xaa_aa_zip = fields.Char(tracking=True)
    xaa_aa_city = fields.Char(tracking=True)
    xaa_aa_state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', tracking=True)
    xaa_aa_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', tracking=True)

    xaa_aa_phone = fields.Char(string='Phone', tracking=True)
    xaa_aa_mobile = fields.Char(string='Mobile', tracking=True)
    xaa_aa_trademark_id = fields.Many2one('company.trademark', string = 'Trademark',related='xaa_aa_lead_id.xaa_aa_trademark_id')
    xaa_aa_time = fields.Datetime('Time of day', tracking=True)
    xaa_aa_user_id = fields.Many2one('res.users', string="Salesperson", index=True, tracking=True, default=lambda self: self.env.user)
    xaa_aa_pf_access = fields.Char('Security Token', copy=False, default=_default_random_pf_access)

    xaa_aa_image_ids = fields.One2many('order.image', 'xaa_aa_formulier_id', tracking=True, string='Images')
    xaa_aa_sale_number = fields.Integer(compute='_compute_quotation', string="Number of Quotations")
    xaa_aa_order_ids = fields.One2many('sale.order', 'xaa_aa_formulier_id', string='Quotation')
    xaa_aa_lead_number = fields.Integer(compute='_compute_quotation', string="Number of Lead")
    xaa_aa_lead_ids = fields.One2many('crm.lead', 'xaa_aa_formulier_id', string='Opportunities')
    xaa_aa_task_number = fields.Integer(compute='_compute_quotation', string="Number of Task")
    xaa_aa_task_ids = fields.One2many('project.task', 'xaa_aa_formulier_id', string='Tasks')

    xaa_aa_date_opportunity = fields.Date(string='Meeting Date')
    xaa_aa_date_report = fields.Date(string='Report Date')

    xaa_aa_video_ids = fields.One2many('order.video', 'xaa_aa_formulier_id', tracking=True, string='Video')
    xaa_aa_document_ids = fields.One2many('order.document', 'xaa_aa_formulier_id', tracking=True, string="Document")

    def _init_column(self, column_name):
        """ Initialize the value of the given column for existing rows.
            Overridden here because we need to have different default values
            for PF Access token for every Formulier.
        """
        if column_name != 'xaa_aa_pf_access':
            super(ProjectFormulier, self)._init_column(column_name)
        else:
            query = 'SELECT id FROM "%s" WHERE "%s" is NULL' % (
                self._table, column_name)
            self.env.cr.execute(query)
            formulier_ids = self.env.cr.fetchall()

            for formulier_id in formulier_ids:
                query = 'UPDATE "%s" SET xaa_aa_pf_access = %s WHERE id = %s' % (
                    self._table, self._default_random_pf_access(), formulier_id[0])
                self.env.cr.execute(query)

    @api.onchange('xaa_aa_partner_id')
    def overview_image_set(self):
        ''' set streetview image in pf '''

        apikey = self.env['ir.config_parameter'].sudo().get_param('base_geolocalize.google_map_api_key')
        if apikey and self.xaa_aa_partner_id:
            self.xaa_aa_partner_id.geo_localize()
            if self.xaa_aa_partner_id.partner_latitude and self.xaa_aa_partner_id.partner_longitude:
                url = 'https://maps.googleapis.com/maps/api/streetview?size=1500x900&location='+str(self.xaa_aa_partner_id.partner_latitude)+','+str(self.xaa_aa_partner_id.partner_longitude)+'&heading=360&pitch=-0.76&key='+apikey
                html = urllib.request.urlopen(url).read()
                profile_image = base64.encodestring(html)
                self.xaa_aa_image = profile_image

    @api.model
    def create(self, vals):
        res = super(ProjectFormulier, self).create(vals)
        res.overview_image_set()
        return res

    def write(self,vals):
        res = super(ProjectFormulier, self).write(vals)
        if vals.get('xaa_aa_partner_id'):
            self.overview_image_set()
        return res

    @api.depends('xaa_aa_order_ids')
    def _compute_quotation(self):
        for formulier in self:
            s_nbr = 0
            for order in formulier.xaa_aa_order_ids:
                s_nbr += 1
            formulier.xaa_aa_lead_number = len(formulier.xaa_aa_lead_ids.ids) or 0
            formulier.xaa_aa_task_number = len(formulier.xaa_aa_task_ids.ids) or 0
            formulier.xaa_aa_sale_number = s_nbr

    def opportunity_stage(self):
        self.xaa_aa_state = 'opportunity'

    def quotation_stage(self):
        self.xaa_aa_state = 'quotation'

    def task_stage(self):
        self.xaa_aa_state = 'task'

    def goto_website_form(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/project-formulier/'+str(self.id)+'/'+str(self.xaa_aa_pf_access),
            'target': 'self',
        }

    def online_pf_dictionary(self):
        """ send all required values on online pf page"""

        products = self.env['product.product'].sudo().search([])
        countries = self.env['res.country'].search([])
        values = {'formulier_id': self,
                'products': products,
               }
        return values


class PFImage(models.Model):
    _name = 'order.image'
    _description = 'Images for PF'

    xaa_aa_name = fields.Char('Name')
    xaa_aa_image = fields.Binary('Image', attachment=True)
    xaa_aa_file_type = fields.Char('File Type')
    xaa_aa_is_task = fields.Boolean('Is for Task')
    xaa_aa_formulier_id = fields.Many2one('question.formulier', 'Related Form', copy=True, readonly=True)


class PFVideo(models.Model):
    _name = 'order.video'
    _description = 'Videos for PF'

    xaa_aa_name = fields.Char('Name')
    xaa_aa_video = fields.Binary('Video', attachment=True)
    xaa_aa_file_type = fields.Char('File Type')
    xaa_aa_is_task = fields.Boolean('Is for Task')
    xaa_aa_formulier_id = fields.Many2one('question.formulier', 'Related Form', copy=True, readonly=True)


class PFDocument(models.Model):
    _name = 'order.document'
    _description = 'Documents for PF'

    xaa_aa_name = fields.Char('Name')
    xaa_aa_file = fields.Binary('File', attachment=True)
    xaa_aa_file_type = fields.Char('File Type')
    xaa_aa_formulier_id = fields.Many2one('question.formulier', 'Related Form', copy=True, readonly=True)
