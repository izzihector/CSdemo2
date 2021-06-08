    # -*- coding: utf-8 -*-

import datetime
from odoo import api, fields, models, _

class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_four', 'PV projectform')])

class ProjectFormulier(models.Model):
    """ Add all questions for PV online PF and PV website quote of PF"""

    _inherit = "question.formulier"


    # Ontwerpvragen -> Design questions
    xaa_aa_roof_type_one = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type.')
    xaa_aa_roof_type_two = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_roof_type_three = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_roof_type_four = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_roof_type_five = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_roof_type_six = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_roof_type_seven = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_roof_type_eight = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),],
        string='Roof type')
    xaa_aa_covering_type_one = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_two = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_three = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_four = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_five = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_six = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_seven = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_covering_type_eight = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet'),
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('Anders,Zie op', 'Anders,Zie op'),],
        string='Covering type')
    xaa_aa_orientaion_type_one = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_two = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_three = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_four = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_five = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_six = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_seven = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_orientaion_type_eight = fields.Selection([
        ('Zuid', 'Zuid'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Oost', 'Oost'),
        ('West', 'West'),
        ('Noordwest', 'Noordwest'),
        ('Noord', 'Noord'),],
        string='Orientaion type')
    xaa_aa_inclination_angle_one = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_two = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_three = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_four = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_five = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_six = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_seven = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_inclination_angle_eight = fields.Float(
        'Inclination Angle(Degrees)')
    xaa_aa_roof_tiles_one = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_two = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_three = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_four = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_five = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_six = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_seven = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_roof_tiles_eight = fields.Selection([
        ('Gehaakt', 'Gehaakt'),
        ('Geschroefd', 'Geschroefd'),
        ('Geen idee', 'Geen idee'),],
        string='Roof tiles type')
    xaa_aa_visual_estimate_panels_one = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_two = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_three = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_four = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_five = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_six = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_seven = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_visual_estimate_panels_eight = fields.Integer(
        'Visual Estimate Maximum Panels 1100*1800m')
    xaa_aa_schadow_one = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_two = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_three = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_four = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_five = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_six = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_seven = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_schadow_eight = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja, paal', 'Ja, paal'),
        ('Ja, boom', 'Ja, boom'),
        ('Ja, dakkapel', 'Ja, dakkapel'),],
        string='Schadow')
    xaa_aa_remark_one = fields.Char('Remarks')
    xaa_aa_remark_two = fields.Char('Remarks')
    xaa_aa_remark_three = fields.Char('Remarks')
    xaa_aa_remark_four = fields.Char('Remarks')
    xaa_aa_remark_five = fields.Char('Remarks')
    xaa_aa_remark_six = fields.Char('Remarks')
    xaa_aa_remark_seven = fields.Char('Remarks')
    xaa_aa_remark_eight = fields.Char('Remarks')
    xaa_aa_roof_surface_remark = fields.Text('Remarks regarding the roof surfaces:')

    annual_consumption = fields.Float('What is the annual consumption:')
    total_yield_chosen_panels = fields.Float('Total yield for the chosen panels:')
    annual_consumption_percentage = fields.Float('(%)of your annual consumption')

    xaa_aa_solar_color_one = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_one = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_one = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_two = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_two = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_two = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_three = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_three = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_three = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_four = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_four = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_four = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_five = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_five = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_five = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_six = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_six = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_six = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_seven = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_seven = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_seven = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_solar_color_eight = fields.Many2one('solar.type', string="What color panel is desired:")
    xaa_aa_solar_product_eight = fields.Many2one('product.product', string='Choose the panels:')
    xaa_aa_mounting_sys_eight = fields.Many2one('product.product', string='Mounting System:')
    xaa_aa_no_of_panels_one = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_one = fields.Integer('Panel inclination')
    xaa_aa_no_of_panels_two = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_two = fields.Integer('Panel inclination')

    xaa_aa_no_of_panels_three = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_three = fields.Integer('Panel inclination')
    xaa_aa_no_of_panels_four = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_four = fields.Integer('Panel inclination')
    xaa_aa_no_of_panels_five = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_five = fields.Integer('Panel inclination')
    xaa_aa_no_of_panels_six = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_six = fields.Integer('Panel inclination')
    xaa_aa_no_of_panels_seven = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_seven = fields.Integer('Panel inclination')
    xaa_aa_no_of_panels_eight = fields.Integer('Choose the number of panels:')
    xaa_aa_panel_inclination_eight = fields.Integer('Panel inclination')

    # INVERTER AND OTHER DETAILS
    xaa_aa_inverter_type = fields.Selection([
        ('Omvormer - string', 'Omvormer - string'),
        ('Omvormer - optimizers', 'Omvormer - optimizers'),
        ('Micro omvormer', 'Micro omvormer'),],
        string='Choose inverter type:')
    xaa_aa_gateway = fields.Selection([
        ('Envoy-S Standard', 'Envoy-S Standard'),
        ('Envoy-S Metered', 'Envoy-S Metered'),],
        string='Choose gateway:')
    xaa_aa_inverter_icw_optimizer = fields.Many2one(
        'product.product', string='Choose inverter i.c.w optimizers:')
    xaa_aa_optimizer = fields.Selection([
        ('SolarEdge P401 (1 piece per panel)', 'SolarEdge P401 (1 piece per panel)'),
        ('SolarEdge P850 (1 piece per 2 panel)', 'SolarEdge P850 (1 piece per 2 panel)'),],
        string='Choose optimizers:')
    xaa_aa_inverter = fields.Selection([
        ('Goodwe', 'Goodwe'),
        ('Growatt', 'Growatt'),
        ('Fronius', 'Fronius'),],
        string='Choose inverter:')
    xaa_aa_model = fields.Selection([],string='Choose model:')
    xaa_aa_standard_extraproduct = fields.Selection([
        ('Niet van toepassing', 'Niet van toepassing'),
        ('Dakdoorvoer', 'Dakdoorvoer'),
        ('Ventilatiepan', 'Ventilatiepan'),],
        string='Select, standard, extra product(s):')
    xaa_aa_extra_onetime_product_needed = fields.Selection([
        ('Niet van toepassing', 'Niet van toepassing'),
        ('Ja', 'Ja'),],
        string='Extra "one time" product(s) needed:')
    xaa_aa_adjustment = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja', 'Ja'),],
        string='Adjustment:')
    xaa_aa_adjustment_detail = fields.Char('Adjustment detail:')
    xaa_aa_technical_recording_needed = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja', 'Ja'),],
        string='Technical recording needed:')
    xaa_aa_installation_time = fields.Integer('Required installation time:')
    xaa_aa_template = fields.Selection([
        ('Layout op eigen naam', 'Layout op eigen naam'),
        ('Layout op naam van installteur', 'Layout op naam van installteur'),],
        string='Choose your template:')




    def online_pf_dictionary(self):
        """ online PF possible values"""

        values = super(ProjectFormulier, self).online_pf_dictionary()
        if values.get('internal_user') and values.get('internal_user') == True:
            domain = ['|',('xaa_aa_show_product_user','=','yes'),'|',
                ('xaa_aa_show_product_user','=',False),
                ('xaa_aa_product_portal_user','in', values.get('user').id)]
        else:
            domain = ['|',('xaa_aa_product_portal_user','in', values.get('user').id),
                ('xaa_aa_show_product_user','=',False)]
        if self.xaa_aa_formulier_type == 'formulier_four':
            Product = self.env['product.product'].sudo()
            solar_type_ids = self.env['solar.type'].sudo().search([])
            solar_product_one_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_one.ids)], order='xaa_aa_priority')
            solar_product_two_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_two.ids)], order='xaa_aa_priority')
            solar_product_three_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_three.ids)], order='xaa_aa_priority')
            solar_product_four_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_four.ids)], order='xaa_aa_priority')
            solar_product_five_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_five.ids)], order='xaa_aa_priority')
            solar_product_six_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_six.ids)], order='xaa_aa_priority')
            solar_product_seven_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_seven.ids)], order='xaa_aa_priority')
            solar_product_eight_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_color_eight.ids)], order='xaa_aa_priority')
            converter_product_ids = Product.search(domain+[
                '&', ('xaa_aa_min_product_range', '<=', self.xaa_aa_energy_wat_piek),
                ('xaa_aa_max_product_range', '>=', self.xaa_aa_energy_wat_piek),
                ('xaa_aa_product_type', '=', 'Converter')], order='xaa_aa_priority')
            flat_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Flat Roof')], order='xaa_aa_priority')
            slanted_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Slanted Roof')], order='xaa_aa_priority')
            optimiser_products = self.xaa_aa_optimiser_product
            iso_extra_product = Product.search([
                ('xaa_aa_product_type', '=', 'Extra option iso')], limit=1)
            values.update({'solar_type_ids': solar_type_ids,
                        'solar_product_one_ids': solar_product_one_ids,
                        'solar_product_two_ids': solar_product_two_ids,
                        'solar_product_three_ids': solar_product_three_ids,
                        'solar_product_four_ids': solar_product_four_ids,
                        'solar_product_five_ids': solar_product_five_ids,
                        'solar_product_six_ids': solar_product_six_ids,
                        'solar_product_seven_ids': solar_product_seven_ids,
                        'solar_product_eight_ids': solar_product_eight_ids,
                        'converter_product_ids': converter_product_ids,
                        'flat_product_ids': flat_product_ids,
                        'slanted_product_ids': slanted_product_ids,
                        'optimiser_products': optimiser_products,
                        'iso_extra_product': iso_extra_product,
                        })
        return values
