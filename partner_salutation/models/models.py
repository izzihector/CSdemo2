# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import api, fields, models, _ 


class PartnerSalutation(models.Model):
    _inherit = 'res.partner'

    xaa_aa_firstname = fields.Char("First name")
    xaa_aa_lastname = fields.Char("Last name")
    xaa_aa_informal_salutation = fields.Selection([
        ('hello','Hello'),
        ('best','Best')
    ], string='Informal Salutation')
    xaa_aa_formal_salutation = fields.Selection([
        ('dear','Dear')
    ], string='Formal Salutation')
    xaa_aa_formal_partner_salutation = fields.Char(string='Formal Partner Salutation')
    xaa_aa_informal_partner_salutation = fields.Char(string='Informal Partner Salutation')

    @api.onchange('xaa_aa_informal_salutation', 'xaa_aa_firstname')
    def _onchange_partner_salutation(self):
        ''' Set  Informal Partner Salutation based on first name and informal salutation type'''
        if self.xaa_aa_firstname and self.xaa_aa_informal_salutation:
            xaa_aa_informal_salutation = dict(self._fields['xaa_aa_informal_salutation'].selection).get(self.xaa_aa_informal_salutation)
            self.xaa_aa_informal_partner_salutation = _(xaa_aa_informal_salutation)+ ' ' + self.xaa_aa_firstname
        else:
            self.xaa_aa_informal_partner_salutation = False

    @api.onchange('xaa_aa_formal_salutation', 'title', 'xaa_aa_lastname')
    def _onchange_par_formal_salutation(self):
        ''' Set Formal Partner Salutation based on title, lastname and formal salutaion type'''
        if self.xaa_aa_lastname and self.xaa_aa_formal_salutation:
            nameContent = []
            xaa_aa_formal_salutation = dict(self._fields['xaa_aa_formal_salutation'].selection).get(self.xaa_aa_formal_salutation)
            nameContent.append(_(xaa_aa_formal_salutation))
            nameContent.append(self.title and self.title.name or '')
            nameContent.append(self.xaa_aa_lastname or '')
            title = ' '.join([x for x in nameContent if x])
            self.xaa_aa_formal_partner_salutation = title
        else:
            self.xaa_aa_formal_partner_salutation = False


class CrmSalutation(models.Model):
    _inherit = 'crm.lead'

    xaa_aa_firstname = fields.Char("First name")
    xaa_aa_lastname = fields.Char("Last name")
    xaa_aa_informal_salutation = fields.Selection([
        ('hello','Hello'),
        ('best','Best')
    ], string='Informal Salutation')
    xaa_aa_formal_salutation = fields.Selection([
        ('dear','Dear')
    ], string='Formal Salutation')
    xaa_aa_formal_salutation_result = fields.Char(string='Formal Partner Salutation')
    xaa_aa_informal_salutation_result = fields.Char(string='Informal Partner Salutation')

    phone = fields.Char(
        'Mobile', tracking=50,
        compute='_compute_phone', inverse='_inverse_phone', readonly=False, store=True)
    mobile = fields.Char('Phone', compute='_compute_partner_id_values', readonly=False, store=True)

    @api.onchange('xaa_aa_informal_salutation','xaa_aa_firstname')
    def _onchange_informal_salutation(self):
        ''' Set Contact name on Lead Based on Partners firstname and informal salutaion type'''
        ''' Set Informal Partner Salutation Based on first name and Informal Salutation type'''
        contactName = []
        if self.xaa_aa_firstname and self.xaa_aa_informal_salutation:
            xaa_aa_informal_salutation = dict(self._fields['xaa_aa_informal_salutation'].selection).get(self.xaa_aa_informal_salutation)
            self.xaa_aa_informal_salutation_result = _(xaa_aa_informal_salutation)+ ' ' + self.xaa_aa_firstname
        else:
            self.xaa_aa_informal_salutation_result = False
        contactName.append(self.xaa_aa_firstname)
        contactName.append(self.xaa_aa_lastname)
        fullname = ' '.join([x for x in contactName if x])
        if fullname:
            self.contact_name = fullname

    @api.onchange('xaa_aa_formal_salutation', 'title', 'xaa_aa_lastname')
    def _onchange_par_formal_salutation(self):
        ''' Set Contact name on Lead Based on Partners firstname and lastname'''
        ''' Set Formal Partner Salutation Based on last name and formal Salutation type'''
        contactName = []
        if self.xaa_aa_lastname and self.xaa_aa_formal_salutation:
            nameContent = []
            xaa_aa_formal_salutation = dict(self._fields['xaa_aa_formal_salutation'].selection).get(self.xaa_aa_formal_salutation)
            nameContent.append(_(xaa_aa_formal_salutation))
            nameContent.append(self.title and self.title.name)
            nameContent.append(self.xaa_aa_lastname or '')
            titles = ' '.join([x for x in nameContent if x])
            self.xaa_aa_formal_salutation_result = titles
        else:
            self.xaa_aa_formal_salutation_result = False
        contactName.append(self.xaa_aa_firstname)
        contactName.append(self.xaa_aa_lastname)
        fullname = ' '.join([x for x in contactName if x])
        if fullname:
            self.contact_name = fullname

    @api.onchange('partner_id')
    def _onchange_crmpartner_salutation(self):
        self.xaa_aa_formal_salutation_result = self.partner_id.xaa_aa_formal_partner_salutation
        self.xaa_aa_informal_salutation_result = self.partner_id.xaa_aa_informal_partner_salutation
        self.xaa_aa_firstname = self.partner_id.xaa_aa_firstname
        self.xaa_aa_lastname = self.partner_id.xaa_aa_lastname
        self.xaa_aa_formal_salutation = self.partner_id.xaa_aa_formal_salutation
        self.xaa_aa_informal_salutation = self.partner_id.xaa_aa_informal_salutation

    def fillsalutation(self, partner):
        ''' Set Partners firstname , lastname , formal and informal type and formal and informal salutaion
        result based on Leads'''
        partner.xaa_aa_firstname = self.xaa_aa_firstname
        partner.xaa_aa_lastname = self.xaa_aa_lastname
        partner.xaa_aa_formal_salutation = self.xaa_aa_formal_salutation
        partner.xaa_aa_informal_salutation = self.xaa_aa_informal_salutation
        partner.xaa_aa_formal_partner_salutation = self.xaa_aa_formal_salutation_result
        partner.xaa_aa_informal_partner_salutation = self.xaa_aa_informal_salutation_result
        partner.title = self.title

    def write(self, vals):
        ''' Set values of firstname , lastname , formal and informal type and formal and informal salutaion
        result  on Partners When Lead convert to opportunity.'''
        if vals.get('xaa_aa_firstname') and vals.get('xaa_aa_informal_salutation'):
            xaa_aa_informal_salutation = dict(self._fields['xaa_aa_informal_salutation'].selection).get(vals.get('xaa_aa_informal_salutation'))
            vals.update({'xaa_aa_informal_salutation_result': _(xaa_aa_informal_salutation)+ ' ' + vals.get('xaa_aa_firstname')})
        if vals.get('xaa_aa_lastname') and vals.get('xaa_aa_formal_salutation'):
            if vals.get('title'):
                title_id = self.env['res.partner.title'].browse(vals.get('title'))
                title = title_id.name or ''
            else:
                title = self.title.name or ''
            xaa_aa_formal_salutation = dict(self._fields['xaa_aa_formal_salutation'].selection).get(vals.get('xaa_aa_formal_salutation'))
            vals.update({'xaa_aa_formal_salutation_result': _(xaa_aa_formal_salutation)+ ' ' +_(title)+' '+vals.get('xaa_aa_lastname')})
        if vals.get('type') == 'opportunity':
            if self.partner_id:
                self.fillsalutation(self.partner_id)
            if vals.get('partner_id'):
                self.fillsalutation(self.env['res.partner'].browse(vals.get('partner_id')))
        return super(CrmSalutation, self).write(vals)

    @api.model
    def create(self, vals):
        res = super(CrmSalutation, self).create(vals)
        if res.contact_name and not (res.xaa_aa_firstname and res.xaa_aa_lastname):
            name = res.contact_name.split(' ',1)
            if len(name)>=2:
                res.xaa_aa_firstname = name[0]
                res.xaa_aa_lastname = name[1]
            if len(name) == 1:
                res.xaa_aa_firstname = name[0]
        return res

    @api.onchange('contact_name')
    def _onchange_contact_name(self):
        if self.contact_name:
            name = self.contact_name.split(' ',1)
            if len(name)>=2:
                self.xaa_aa_firstname = name[0]
                self.xaa_aa_lastname = name[1]
            if len(name) == 1:
                self.xaa_aa_firstname = name[0]

class SaleOrderSalutation(models.Model):
    _inherit = 'sale.order'

    xaa_aa_sale_order_partner_result = fields.Char(string='Partner Salutation')
    xaa_aa_salutation_type = fields.Selection([
        ('formal', 'Formal'),
        ('informal', 'Informal')
    ], default='formal', string='Salutation Type')

    @api.onchange('partner_id', 'xaa_aa_salutation_type')
    def _onchange_saleorder_salutation(self):
        ''' Set Partner Salutation Result and type On SO Based On Partner.'''
        if self.xaa_aa_salutation_type == 'formal':
            self.xaa_aa_sale_order_partner_result = self.partner_id.xaa_aa_formal_partner_salutation
        elif self.xaa_aa_salutation_type == 'informal':
            self.xaa_aa_sale_order_partner_result = self.partner_id.xaa_aa_informal_partner_salutation
        else:
            self.xaa_aa_sale_order_partner_result = False