# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class FormulierPortal(CustomerPortal):
    """ list out all project formulier record on my account """

    def _prepare_portal_layout_values(self):
        values = super(FormulierPortal, self)._prepare_portal_layout_values()
        user = request.env.user
        admin_user = request.env['res.users'].sudo().browse(2)
        if admin_user.id == user.id:
            domain = []
        else:
            domain = [('xaa_aa_created_by','=',user.id)]
        values['project_formulier_count'] = request.env['question.formulier'].search_count(domain)
        return values

    @http.route(['/my/formulier'], type='http', auth="user", website=True)
    def portal_my_formulier(self, page=1, date_begin=None, date_end=None, sortby=None,filterby=None, **kw):
        values = self._prepare_portal_layout_values()
        user = request.env.user
        ProjectFormulier = request.env['question.formulier']
        admin_user = request.env['res.users'].sudo().browse(2)

        if admin_user.id == user.id:
            domain = []
        else:
            domain = [('xaa_aa_created_by','=',user.id)]

        formulier_count = request.env['question.formulier'].search_count(domain)
        pager = portal_pager(
            url="/my/formulier",
            url_args={'date_begin': date_begin, 'date_end': date_end},
            total=formulier_count,
            page=page,
            step=self._items_per_page
        )
        # search the purchase orders to display, according to the pager data
        records = ProjectFormulier.search(
            domain,
            limit=self._items_per_page,
            offset=pager['offset']
        )
        request.session['my_formulier_history'] = records.ids[:100]

        values.update({
            'date': date_begin,
            'formuliers': records,
            'page_name': 'Project Formulier',
            'pager': pager,
            'default_url': '/my/formulier',
        })
        return request.render("project_formulier.portal_my_project_formulier", values)
