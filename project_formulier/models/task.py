# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    xaa_aa_formulier_id = fields.Many2one('question.formulier', string='Project Formulier')

    @api.model
    def create(self,vals):
        res = super(ProjectTask, self).create(vals)
        order_id = res.sale_order_id
        if order_id.xaa_aa_formulier_id:
            res.xaa_aa_formulier_id = order_id.xaa_aa_formulier_id.id
        return res

    def write(self,vals):
        res = super(ProjectTask, self).write(vals)
        if vals.get('sale_order_id'):
            sale_order_id = self.sale_order_id
            if sale_order_id.xaa_aa_formulier_id:
                self.xaa_aa_formulier_id = sale_order_id.xaa_aa_formulier_id.id
        return res
