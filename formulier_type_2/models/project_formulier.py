# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_two', 'intake ISO')])

class ProjectFormulier(models.Model):
    """ Add all questions for ISO online PF and ISO website quote of PF"""

    _inherit = "question.formulier"


    # Gevel
    xaa_aa_wall_number_m2 = fields.Integer(string='Wall Number of m2', tracking=True)
    xaa_aa_wall_material= fields.Selection([
        ('PUR', 'PUR'),
        ('Foam', 'Foam'),
        ('Parels', 'Parels'),
        ('Wol', 'Wol'),
        ('anders', 'anders'),
        ('nvt', 'nvt'),],
        string='Wall Material', default='Wol', tracking=True)
    xaa_aa_hole_diameter = fields.Selection([
        ('18 CM', '18 CM'),
        ('16 CM', '16 CM'),
        ('14 CM', '14 CM'),
        ('12 CM', '12 CM'),
        ('22 CM', '22 CM'),
        ('nvt', 'nvt'),],
        string='Hole Diameter', default='18 CM', tracking=True)
    xaa_aa_gutter_height = fields.Selection([
        ('0-2.5 m1', '0-2.5 m1'),
        ('2.5-4 m1', '2.5-4 m1'),
        ('4-6 m1', '4-6 m1'),
        ('6-8 m1', '6-8 m1'),
        ('8-10 m1', '8-10 m1'),
        ('10+', '10+'),
        ('nvt', 'nvt'),],
        string='Gutter height', tracking=True)
    xaa_aa_cam_height = fields.Selection([
        ('0-4 m1', '0-4 m1'),
        ('4-6 m1', '4-6 m1'),
        ('6-7 m1', '6-7 m1'),
        ('7-8 m1', '7-8 m1'),
        ('8-9 m1', '8-9 m1'),
        ('10-12 m1', '10-12 m1'),
        ('12+', '12+'),
        ('nvt', 'nvt'),],
        string='Cam height', tracking=True)
    xaa_aa_platform = fields.Selection([
        ('ja', 'ja'),('nee', 'nee')],
        string="Platform", tracking=True)
    xaa_aa_scaffolding = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string="Scaffolding", tracking=True)
    xaa_aa_joint_color = fields.Selection([
        ('wit', 'wit'),
        ('licht grijs', 'licht grijs'),
        ('grijs','grijs'),
        ('donkergrijs', 'donkergrijs'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string="Joint Color", default='wit', tracking=True)
    xaa_aa_painted_facade = fields.Selection([
        ('nee', 'nee'),
        ('ja, besproken', 'ja, besproken'),
        ('ja, niet besproken','ja, niet besproken'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string="Painted facade", default='nee', tracking=True)
    xaa_aa_condition_add = fields.Selection([
        ('goed', 'goed'),
        ('normaal', 'normaal'),
        ('slecht','slecht'),
        ('heel slecht','heel slecht'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string="Condition Add", default='goed', tracking=True)
    xaa_aa_cavity_width = fields.Selection([
        ('geen', 'geen'),
        ('3 CM', '3 CM'),
        ('4 CM','4 CM'),
        ('5 CM','5 CM'),
        ('6 CM','6 CM'),
        ('7 CM','7 CM'),
        ('8 CM','8 CM'),
        ('9 CM','9 CM'),
        ('10 CM','10 CM'),
        ('11 CM','11 CM'),
        ('12 CM','12 CM'),
        ('13 CM','13 CM'),
        ('14 CM','14 CM'),
        ('15 CM','15 CM'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string='Cavity width', default='6 CM', tracking=True)
    xaa_aa_cavity_inspection = fields.Selection([
        ('geen', 'geen'),
        ('1 gat', '1 gat'),
        ('2 gaten','2 gaten'),
        ('3 gaten','3 gaten'),
        ('4 gaten','4 gaten'),
        ('5 gaten','5 gaten'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string="Cavity inspection", default='1 gat', tracking=True)
    xaa_aa_plant_growth = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string="Plant growth", default='nee', tracking=True)
    xaa_aa_housing_separation = fields.Selection([
        ('geen', 'geen'),
        ('1 borstel', '1 borstel'),
        ('2 borstel', '2 borstel'),
        ('3 borstel', '3 borstel'),
        ('4 borstel', '4 borstel'),
        ('5 borstel', '5 borstel'),
        ('6 borstel', '6 borstel'),
        ('7 borstel', '7 borstel'),
        ('8 borstel', '8 borstel'),
        ('9 borstel', '9 borstel'),
        ('10 borstel', '10 borstel'),
        ('11 borstel', '11 borstel'),
        ('12 borstel', '12 borstel'),
        ('13 borstel', '13 borstel'),
        ('14 borstel', '14 borstel'),
        ('15 borstel', '15 borstel'),
        ('16 borstel', '16 borstel'),
        ('17 borstel', '17 borstel'),
        ('18 borstel', '18 borstel'),
        ('19 borstel', '19 borstel'),
        ('20 borstel', '20 borstel'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string='Housing separation', default='geen', tracking=True)

    # vloer
    xaa_aa_floor_number_m2 = fields.Integer(string='Floor Number of m2', tracking=True)
    xaa_aa_floor_material= fields.Selection([
        ('PUR', 'PUR'),
        ('Bodemparels', 'Bodemparels'),
        ('Anders', 'Anders'),
        ('NVT', 'NVT'),],
        string='Floor Material', default='PUR', tracking=True)
    xaa_aa_floor_ventilation = fields.Selection([
        ('geen', 'geen'),
        ('1 rooster', '1 rooster'),
        ('2 rooster', '2 rooster'),
        ('3 rooster', '3 rooster'),
        ('4 rooster', '4 rooster'),
        ('5 rooster', '5 rooster'),
        ('6 rooster', '6 rooster'),
        ('7 rooster', '7 rooster'),
        ('8 rooster', '8 rooster'),
        ('9 rooster', '9 rooster'),
        ('10 rooster', '10 rooster'),
        ('11 rooster', '11 rooster'),
        ('12 rooster', '12 rooster'),
        ('13 rooster', '13 rooster'),
        ('14 rooster', '14 rooster'),
        ('15 rooster', '15 rooster'),
        ('16 rooster', '16 rooster'),
        ('17 rooster', '17 rooster'),
        ('18 rooster', '18 rooster'),
        ('19 rooster', '19 rooster'),
        ('20 rooster', '20 rooster'),
        ('anders', 'anders'),
        ('nvt', 'nvt')],
        string='Floor Ventilation', default='geen', tracking=True)
    xaa_aa_crawl_space_available = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Crawl space available', tracking=True)
    xaa_aa_crawl_space_accessible = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Crawl space accessible', tracking=True)
    xaa_aa_crawl_space_isolated = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        default='nee', string='Crawl space isolated', tracking=True)

    # Dak
    xaa_aa_roof_number_m2 = fields.Integer(string='Roof Number of m2', tracking=True)
    xaa_aa_roof_material= fields.Selection([
        ('PUR', 'PUR'),
        ('Isovlas incl witte afwerking', 'Isovlas incl witte afwerking'),
        ('PIR plaat', 'PIR plaat'),
        ('Rockwool', 'Rockwool'),
        ('Knauf timberframe', 'Knauf timberframe'),
        ('Anders', 'Anders'),
        ('NVT', 'NVT'),],
        string='Roof Material', default='PUR', tracking=True)
    xaa_aa_accessible = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Accessible', tracking=True)

    xaa_aa_house = fields.Binary(string='House / Property',
        tracking=True, attachment=True)
    xaa_aa_access = fields.Binary(string='Access',
        tracking=True, attachment=True)
    xaa_aa_parking_spot = fields.Binary(string='Parking spot',
        tracking=True, attachment=True)
    xaa_aa_obstacles = fields.Binary(string='Obstacles',
        tracking=True, attachment=True)
    xaa_aa_wall1 = fields.Binary(string='Wall 1',
        tracking=True, attachment=True)
    xaa_aa_wall2 = fields.Binary(string='Wall 2',
        tracking=True, attachment=True)
    xaa_aa_floor1 = fields.Binary(string='Floor 1',
        tracking=True, attachment=True)
    xaa_aa_roof1 = fields.Binary(string='Roof 1',
        tracking=True, attachment=True)

    # Questions for ISO quote
    xaa_aa_kind_of_isolate = fields.Selection([
        ('Cavity', 'Cavity'),
        ('Floor', 'Floor')],
        string='What kind of isolation is it about ?')
    xaa_aa_iso_type = fields.Selection([
        ('Hout', 'Hout'),
        ('Beton', 'Beton')],
        string='Type')
    xaa_aa_m2_count = fields.Integer(string="Number of m2")
    xaa_aa_spacing = fields.Selection([
        ('Minder 45 cm', 'Minder 45 cm'),
        ('Meer dan 45 cm', 'Meer dan 45 cm')],
        string='Spacing')
    xaa_aa_tickness_of_wall = fields.Selection([
        ('4', '4'),('5', '5'),('6', '6'),('7', '7'),
        ('8', '8'),('9', '9'),('10', '10'),('11', '11'),
        ('12', '12'),],
        string='Tickness of wall', tracking=True)
    xaa_aa_isolation_product = fields.Many2one('product.product',
        string='What kind of material ?')
    xaa_aa_need_certificate = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do you need certificate ?', tracking=True, default="ja")
    xaa_aa_need_ventilation_grid = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do you need ventilation grid ?', tracking=True)
    xaa_aa_ventilation_product = fields.Many2one('product.product',
        string='Ventilation grid')
    xaa_aa_need_cavity_boundary = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee')],
        string='Do you need Cavity boundary ?', tracking=True)
    xaa_aa_cavity_boundary_product = fields.Many2one('product.product',
        string='Cavity boundary')
    xaa_aa_iso_installation_time = fields.Selection([
        ('4 Hours', '4 Hours'),
        ('8 Hours', '8 Hours'),
        ('12 Hours', '12 Hours'),
        ('16 Hours', '16 Hours'),
        ('24 Hours', '24 Hours'),
        ('30 Hours', '30 Hours'),
        ('32 Hours', '32 Hours'),
        ('36 Hours', '36 Hours'),
        ('40 Hours', '40 Hours')],
        string='How many time needed for installation ?', default='8 Hours')
    xaa_aa_extra_support = fields.Selection([
        ('Platform', 'Platform'),
        ('Manitour', 'Manitour'),
        ('Scaffolding', 'Scaffolding')],
        string='Extra support')
    xaa_aa_need_extra_product = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee')],
        string='Add inspection', tracking=True, default="ja")

    xaa_aa_need_custm_extra_product = fields.Selection([
        ('ja 1', 'ja 1'),
        ('ja 2', 'ja 2'),
        ('ja 3', 'ja 3'),
        ('nee', 'nee')],
        string='Do you need extra product ?', tracking=True)
    xaa_aa_extra_product_description = fields.Char(string='Extra product 1: give description')
    xaa_aa_extra_product_cost = fields.Float(string='Cost price')
    xaa_aa_extra_product_sale = fields.Float(string='Sale price')
    xaa_aa_extra_product_description_two = fields.Char(string='Extra product 2: give description')
    xaa_aa_extra_product_cost_two = fields.Float(string='Cost price')
    xaa_aa_extra_product_sale_two = fields.Float(string='Sale price')
    xaa_aa_extra_product_description_three = fields.Char(string='Extra product 3: give description')
    xaa_aa_extra_product_cost_three = fields.Float(string='Cost price')
    xaa_aa_extra_product_sale_three = fields.Float(string='Sale price')
    xaa_aa_service_price = fields.Float(string='Service Price')
    xaa_aa_material_price = fields.Float(string='Material Price')
    xaa_aa_ventilation_price = fields.Float(string='Price ventilation grid per piece')


    # iso website quote
    xaa_aa_quote_construction_year = fields.Selection([
        ('voor 1935', 'voor 1935'),
        ('tussen 1935 en 1975', 'tussen 1935 en 1975'),
        ('na 1975', 'na 1975'),
        ('Ik weet het niet', 'Ik weet het niet')],
        string='What is the year of construction of your home?',
        tracking=True, default='tussen 1935 en 1975')
    xaa_aa_quote_house_insulated = fields.Selection([
        ('Knauf Supafil minerals inblaaswol(aanbevolen)', 'Knauf Supafil minerals inblaaswol(aanbevolen)'),
        ('HR++ Grijze EPS Parels', 'HR++ Grijze EPS Parels'),
        ('Energie Foam wit isolatieschuim', 'Energie Foam wit isolatieschuim')],
        string='How do you want your house to be insulated?',
        tracking=True,
        default='Knauf Supafil minerals inblaaswol(aanbevolen)')
    xaa_aa_quote_cavity_thickness_home = fields.Selection([
        ('Minder dan 5 cm', 'Minder dan 5 cm'),
        ('5 tot 6 cm', '5 tot 6 cm'),
        ('6 tot 8 cm', '6 tot 8 cm'),
        ('Meer dan 8 cm', 'Meer dan 8 cm'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='What is the cavity thickness of your home?',
        tracking=True, default='5 tot 6 cm')
    xaa_aa_quote_type_of_house_id = fields.Many2one('house.info',
        string='What type of house do you live in?')
    xaa_aa_quote_need_insulated = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Does your home have an extension that needs to be insulated?',
        tracking=True, default='nee')
    xaa_aa_quote_many_extension = fields.Integer(string='Number of M2 to be insulated')
    xaa_aa_qupte_do_crawl_space = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do you have crawl space?', tracking=True, default='ja')


    # ISO Quote stage questions
    xaa_aa_quote_home_free_install = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Is each side of your home free to install a ladder?',
        tracking=True, default="ja")
    xaa_aa_quote_iso_home_accessible = fields.Selection([
        ('goed', 'goed'),
        ('redelijk', 'redelijk'),
        ('slecht', 'slecht')],
        string='How accessible is your home?',
        tracking=True, default='goed')
    xaa_aa_quote_iso_home_parking = fields.Selection([
        ('goed', 'goed'),
        ('redelijk', 'redelijk'),
        ('slecht', 'slecht')],
        string='How is the parking at your home?',
        tracking=True, default='goed')
    xaa_aa_quote_iso_estimate_height_gutter = fields.Selection([
        ('1 tot 3 meter', '1 tot 3 meter'),
        ('3 tot 6 meter', '3 tot 6 meter'),
        ('hoger dan 7 meter', 'hoger dan 7 meter'),
        ('Ik weet het niet', 'Ik weet het niet')],
        string='How high do you estimate the height from the ground to the gutter?',
        tracking=True, default='3 tot 6 meter')
    xaa_aa_quote_iso_estimate_height_ridge = fields.Selection([
        ('lager dan 5 meter', 'lager dan 5 meter'),
        ('5 tot 9 meter', '5 tot 9 meter'),
        ('hoger dan 9 meter', 'hoger dan 9 meter'),
        ('Ik weet het niet', 'Ik weet het niet')],
        string='How high do you estimate the height from the ground to the ridge of your home?',
        tracking=True, default='5 tot 9 meter')
    xaa_aa_quote_iso_square_meter_quotation = fields.Selection([
        ('Ja, ik weet dat dit klopt.', 'Ja, ik weet dat dit klopt.'),
        ('Nee, dit klopt niet; ik heb een schatting gegeven.', 'Nee, dit klopt niet; ik heb een schatting gegeven.'),
        ('Ik weet niet of dit klopt, neem contact met me op.', 'Ik weet niet of dit klopt, neem contact met me op.'),],
        string='Is the number of square meters on the quotation correct?',
        tracking=True, default='Ja, ik weet dat dit klopt.')
    xaa_aa_quote_iso_faced_covered_obstacles = fields.Selection([
        ('nee', 'nee'),
        ('ja', 'ja'),
        ('Ja, maar ik ben bereid deze voor de tijd te verwijderen.', 'Ja, maar ik ben bereid deze voor de tijd te verwijderen.'),],
        string='Is your facade covered with vegetation or similar obstacles?',
        tracking=True, default='nee')
    xaa_aa_quote_iso_thickness_cavity = fields.Selection([
        ('minder dan 5 cm', 'minder dan 5 cm'),
        ('5 tot 6 cm', '5 tot 6 cm'),
        ('6 tot 9 cm', '6 tot 9 cm'),
        ('9+', '9+'),],
        string="What is the width / thickness of the cavity?",
        tracking=True, default="5 tot 6 cm")
    xaa_aa_quote_iso_cavity_wall_insulation = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee')],
        string="Has your house already been checked for suitability for cavity wall insulation?",
        tracking=True, default="nee")
    xaa_aa_quote_iso_cavity_contamination = fields.Selection([
        ('nee', 'nee'),
        ('ja', 'ja')],
        string="Is there internal cavity contamination?",
        tracking=True, default="nee")
    xaa_aa_quote_iso_house_painted_faced = fields.Selection([
        ('nee', 'nee'),
        ('ja', 'ja'),
        ('Ja, maar ik weet zeker dat deze dampdoorlatend is.', 'Ja, maar ik weet zeker dat deze dampdoorlatend is.')],
        string="Does the house have a painted facade?",
        tracking=True, default="nee")
    xaa_aa_quote_iso_home_cutting_joint = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee')],
        string='Does your home have a cutting joint?',
        tracking=True, default='nee')
    xaa_aa_quote_iso_crawl_space_use = fields.Selection([
        ('Ja, en deze is goed te gebruiken', 'Ja, en deze is goed te gebruiken'),
        ('Nee, de woning heeft geen kruipruimte', 'Nee, de woning heeft geen kruipruimte'),
        ('Ja, maar deze niet goed/eenvoudig te gebruiken','Ja, maar deze niet goed/eenvoudig te gebruiken')],
        string="Does your home have a crawl space and is it good to use?",
        tracking=True)
    xaa_aa_quote_iso_monumental_building = fields.Selection([
        ('nee', 'nee'),
        ('ja', 'ja')],
        string='Do you have a monumental building, or a building where a permit is required to carry out these activities?',
        tracking=True, default='nee')
    xaa_aa_quote_iso_rental_owner_home = fields.Selection([
        ('koop', 'koop'),
        ('huur', 'huur'),
        ('De woning moet nog worden aangekocht', 'De woning moet nog worden aangekocht')],
        string='Do you have a rental or owner-occupied home?',
        tracking=True, default='koop')
    xaa_aa_quote_iso_insulation_description = fields.Text(string='Perhaps there are other things you think are important that we need to know to properly perform insulation. You can indicate these matters in the field below.')

    xaa_aa_quote_iso_overview_photo = fields.Binary(string='Overview photo (important)', attachment=True)
    xaa_aa_quote_iso_faced_photo = fields.Binary(string='Photo facade', attachment=True)
    xaa_aa_quote_iso_rear_faced_photo = fields.Binary(string='Rear facade', attachment=True)
    xaa_aa_quote_iso_side_wall_photo = fields.Binary(string='Side wall 1', attachment=True)
    xaa_aa_quote_iso_side_wall_two_photo = fields.Binary(string='Side wall 1', attachment=True)
    xaa_aa_quote_attachment_photo = fields.Binary(string='Attachment', attachment=True)
    xaa_aa_quote_extra_photo_one = fields.Binary(string='Additional photo', attachment=True)
    xaa_aa_quote_extra_photo_two = fields.Binary(string='Additional photo', attachment=True)
    xaa_aa_quote_iso_working_days = fields.Selection([
        ('Ja, ik ben tevreden over de offerte en wil graag door Energiecontrol gebeld worden over dit aanbod.', 'Ja, ik ben tevreden over de offerte en wil graag door Energiecontrol gebeld worden over dit aanbod.'),
        ('Nee, ik neem graag zelf contact met jullie op.', 'Nee, ik neem graag zelf contact met jullie op.'),
        ('Nee, ik zou graag nog andere offertes willen vergelijken.','Nee, ik zou graag nog andere offertes willen vergelijken.'),
        ('Nee, ik zou graag nog meer informatie van Energiecontrol willen ontvangen, en word graag door jullie gebeld.', 'Nee, ik zou graag nog meer informatie van Energiecontrol willen ontvangen, en word graag door jullie gebeld.')],
        string='so that you have your solar panels on the roof within five working days?',
        tracking=True, default='Ja, ik ben tevreden over de offerte en wil graag door Energiecontrol gebeld worden over dit aanbod.')


    def online_pf_dictionary(self):
        """ online PF possible values"""

        values = super(ProjectFormulier, self).online_pf_dictionary()
        if self.xaa_aa_formulier_type == 'formulier_two':
            if values.get('internal_user') and values.get('internal_user') == True:
                domain = ['|',('xaa_aa_show_product_user','=','yes'),'|',
                    ('xaa_aa_show_product_user','=',False),
                    ('xaa_aa_product_portal_user','in', values.get('user').id)]
            else:
                domain = ['|',('xaa_aa_product_portal_user','in', values.get('user').id),
                    ('xaa_aa_show_product_user','=',False)]
            Product = self.env['product.product'].sudo()
            if self.xaa_aa_kind_of_isolate and self.xaa_aa_kind_of_isolate == 'Floor':
                if self.xaa_aa_spacing and self.xaa_aa_spacing == 'Meer dan 45 cm':
                    isolation_product_ids = Product.search(domain+[
                        ('xaa_aa_product_type', 'in', ['ISO floor material 1', 'ISO floor material 2'])], order='xaa_aa_priority')
                else:
                    isolation_product_ids = Product.search(domain+[
                        ('xaa_aa_product_type', '=', 'ISO floor material 1')], order='xaa_aa_priority')
            else:
                if self.xaa_aa_tickness_of_wall:
                    isolation_product_ids = Product.search(domain+[
                        ('xaa_aa_product_type', '=', 'I am Isolation'),('xaa_aa_tickness_of_wall', '=', self.xaa_aa_tickness_of_wall)], order='xaa_aa_priority')
                else:
                    isolation_product_ids = Product.search(domain+[
                        ('xaa_aa_product_type', '=', 'I am Isolation')], order='xaa_aa_priority')
            ventilation_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Ventilation grid')], order='xaa_aa_priority')
            cavityboundary_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Cavity boundary')], order='xaa_aa_priority')
            iso_extra_product = Product.search([
                ('xaa_aa_product_type', '=', 'Extra option iso')], limit=1)
            iso_service_product = Product.search([
                        ('name', 'ilike', 'Aanbrengen spouwmuurisolatie')],
                         limit=1)
            values.update({'isolation_product_ids': isolation_product_ids,
                            'ventilation_product_ids': ventilation_product_ids,
                            'cavityboundary_product_ids': cavityboundary_product_ids,
                            'iso_extra_product': iso_extra_product,
                            'iso_service_product': iso_service_product,
                            })
        return values
