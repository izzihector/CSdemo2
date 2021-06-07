# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class FormulierQuote(http.Controller):

    @http.route(['/formulier/quote/<int:xaa_aa_formulier_id>/<string:xaa_aa_pf_access>'],
                type='http', auth="public", website=True)
    def customer_formulier_quote(self, xaa_aa_formulier_id, xaa_aa_pf_access, **kw):
        """ Project Formulier Quote view on web form """

        formulier_id = request.env['question.formulier'].sudo().search([
                                                ('id','=',xaa_aa_formulier_id),
                                                ('xaa_aa_pf_access','=',xaa_aa_pf_access),
                                                ])
        if formulier_id and formulier_id.xaa_aa_partner_id:
            if formulier_id.xaa_aa_state in ['quotation','quotation_output']:
                return request.render('project_formulier_quote.customer_quotation_question_template',
                                    {'formulier_id': formulier_id})
            values = formulier_id.sudo().online_pf_dictionary()
            return request.render('project_formulier_quote.customer_quote_formulier', values)
        else:
            return request.redirect('/my')

    @http.route(['/stop/all/<int:xaa_aa_formulier_id>'],
                type='http', auth="public", website=True)
    def stop_all_formulier(self, xaa_aa_formulier_id, **kw):
        """ Project Formulier archive and opportunity add in lost stage """

        xaa_aa_formulier_id = request.env['question.formulier'].sudo().browse(int(xaa_aa_formulier_id))
        xaa_aa_formulier_id.active = False
        xaa_aa_formulier_id.xaa_aa_lead_id.sudo().action_set_lost()
        return request.render('project_formulier_quote.close_lead_template', {})

    @http.route(['/formulier/update_formulier'], type='json', auth="public", methods=['POST'], website=True)
    def update_formulier(self, quoteData, formulier_id,**kw):
        """ update some fields of PF"""

        if formulier_id:
            formulier_id = request.env['question.formulier'].sudo().browse(int(formulier_id))
            formulier_id.write(quoteData)
        return True

