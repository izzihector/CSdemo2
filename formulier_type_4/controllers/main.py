# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.project_formulier.controllers.main import ProjectFormulier

class ProjectFormulier(ProjectFormulier):

    @http.route(['/formulier/pv_quote_infos'], type='json', auth="public", methods=['POST'], website=True)
    def pv_quote_infos(self, solar_color=None, **kw):
        """ Send Required data to Quote PV tab"""

        productObj = request.env['product.product'].sudo()
        solar_products = productObj
        if solar_color:
            solar_products = productObj.search([
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',[int(solar_color)])])
        return dict(
            solar_products=[(sp.id, sp.name, sp.list_price) for sp in solar_products],
        )