    # -*- coding: utf-8 -*-

import datetime
from odoo import api, fields, models, _

class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_three', 'intake PV')])

class ProjectFormulier(models.Model):
    """ Add all questions for PV online PF and PV website quote of PF"""

    _inherit = "question.formulier"

    @api.depends('xaa_aa_location_calculation', 'xaa_aa_solar_watt_piek', 'xaa_aa_solar_product')
    def compute_energy_wat_piek(self):
        for rec in self:
            if rec.xaa_aa_location_calculation and rec.xaa_aa_solar_watt_piek:
                cal = rec.xaa_aa_location_calculation / rec.xaa_aa_solar_watt_piek
                solar_qty = 1
                if (isinstance(cal, float)):
                    solar_qty = int(cal) + 1
                else:
                    solar_qty = cal
                rec.xaa_aa_energy_wat_piek = rec.xaa_aa_solar_watt_piek * solar_qty

    @api.depends('xaa_aa_location_correction', 'xaa_aa_energy_use')
    def compute_location(self):
        for rec in self:
            if rec.xaa_aa_location_correction and rec.xaa_aa_energy_use:
                rec.xaa_aa_location_calculation = rec.xaa_aa_energy_use / rec.xaa_aa_location_correction

    @api.depends('xaa_aa_solar_product')
    def get_energy_wat_piek(self):
        for rec in self:
            rec.xaa_aa_solar_watt_piek = rec.xaa_aa_solar_product.xaa_aa_watt_piek


    # Ontwerpvragen -> Design questions
    xaa_aa_roof_surface = fields.Selection([
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('meer dan 4', 'meer dan 4'),],
        string='How many roof surfaces', default='1', tracking=True)

    # Woning -> Home
    xaa_aa_is_permit_required = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Is a permit required', default='nee', tracking=True)
    xaa_aa_construction_year = fields.Integer(string='Year of construction of the house',
        tracking=True)
    xaa_aa_any_roof_problem = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee'),],
        string='Have you ever had any leaks or other problems with your roof?',
        default='nee', tracking=True)
    xaa_aa_is_buy_rent_property = fields.Selection([
        ('koop', 'koop'), ('huur', 'huur'),],
        string='Is it a rent or buy property?', default='koop', tracking=True)

    # Aansluiten omvormer -> Connecting the inverter
    xaa_aa_string_1 = fields.Integer(string='String 1 (Note: onchange 6 panels or more in 1 string)',
        tracking=True)
    xaa_aa_string_2 = fields.Integer(string='String 2 (Note: onchange 6 panels or more in 1 string)',
        tracking=True)

    # Bereikbaarheid van de woning en het dak -> Accessibility of the home and the roof
    xaa_aa_is_free_space_scaffolding = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee'),],
        string='Is there a free space for scaffolding?', tracking=True)
    xaa_aa_is_provision_required = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee'),],
        string='Is a special provision required (telehandler / lift / aerial platform)',
        default='nee', tracking=True)
    xaa_aa_condition_scaffolding_place = fields.Selection([
        ('Gras', 'Gras'),
        ('Tuin', 'Tuin'),
        ('Zand', 'Zand'),
        ('Straat', 'Straat'),
        ('Geen steiger te plaatsen', 'Geen steiger te plaatsen'),
        ('Geen steiger nodig', 'Geen steiger nodig'),],
        string='What is the condition of the surface on which the scaffolding is placed?',
        tracking=True, default='Tuin')
    xaa_aa_accessibility_rear = fields.Selection([
        ('Brandgang', 'Brandgang'),
        ('Door de garage', 'Door de garage'),
        ('Vrije rondgang', 'Vrije rondgang'),
        ('Door de woning', 'Door de woning'),
        ('N.V.T.', 'N.V.T.'),],
        string='What is the accessibility of the rear',
        tracking=True, default='N.V.T.')
    xaa_aa_use_public_road = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Use must be made of the public road for the erection of scaffolding or facilities',
        default='nee', tracking=True)
    xaa_aa_access_roof_neighbors = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja er is toestemming', 'Ja er is toestemming'),
        ('Ja maar er is nog geen toestemming', 'Ja maar er is nog geen toestemming'),],
        string='Access to the roof / territory of the neighbors is required',
        tracking=True)
    xaa_aa_distance_bus_to_roof = fields.Selection([
        ('0-10', '0-10'),
        ('10-25', '10-25'),
        ('25-50', '25-50'),
        ('50-100', '50-100'),
        ('100-250', '100-250'),
        ('250-500', '250-500'),
        ('500+', '500+'),],
        string='Walking distance from bus to roof access',
        tracking=True)
    xaa_aa_direct_installation_scaffolding = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),
        ('Ja, zie foto/video', 'Ja, zie foto/video'),
        ('Ja, klant zorgt voor oplossing', 'Ja, klant zorgt voor oplossing'),],
        string='Is there an extension / obstacle present that hinders the direct installation of scaffolding or roof lift?',
        default='nee', tracking=True)

    # Dak -> Roof
    xaa_aa_dak_type_of_roof = fields.Selection([
        ('Schuin', 'Schuin'),
        ('Plat', 'Plat'),
        ('Schuin / Dak', 'Schuin / Dak'),
        ('Zadeldak', 'Zadeldak'),],
        string='What type (s) of roof is it?', tracking=True)
    xaa_aa_condition_of_roof = fields.Selection([
        ('goed', 'goed'),
        ('matig', 'matig'),
        ('slecht', 'slecht'),
        ('onbekend', 'onbekend'),],
        string='What is the condition of the roof?',
        default='goed', tracking=True)
    xaa_aa_asbestos_incorporated_roof = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),
        ('ja klant op de hoogte van de gevogen','ja klant op de hoogte van de gevogen'),
        ('ja klant niet op de hoogte van de gevogen','ja klant niet op de hoogte van de gevogen')],
        string='Is asbestos incorporated in the roof? And is the customer aware of the consequences?',
        default='nee', tracking=True)
    xaa_aa_height_of_gutter = fields.Selection([
        ('0-2.5 m1', '0-2.5 m1'),
        ('2.5-4 m1', '2.5-4 m1'),
        ('4-6 m1', '4-6 m1'),
        ('6-8 m1', '6-8 m1'),
        ('8-10 m1', '8-10 m1'),
        ('10+', '10+'),],
        string='What is the height of the gutter?',
        default='8-10 m1', tracking=True)

    # Schuin Dak -> Slanted roof
    xaa_aa_slope = fields.Selection([
        ('0-20 graden', '0-20 graden'),
        ('20-30 graden', '20-30 graden'),
        ('30-40 graden', '30-40 graden'),
        ('40-50 graden', '40-50 graden'),
        ('50-60 graden', '50-60 graden'),
        ('60-70 graden', '60-70 graden'),
        ('70+ graden', '70+ graden')],
        string='What is the slope?', tracking=True)
    xaa_aa_schuin_type_of_roof = fields.Selection([
        ('Pannen', 'Pannen'),
        ('Bitumen', 'Bitumen'),
        ('Golfplaten', 'Golfplaten'),
        ('Staal', 'Staal'),
        ('Leien ', 'Leien '),
        ('Zink', 'Zink'),
        ('Overige', 'Overige'),
        ('ASBEST', 'ASBEST'),],
        string='What type (s) of roofing is it?',
        default='Pannen', tracking=True)
    xaa_aa_are_pans_screwed_or_hooked = fields.Selection([
        ('geschroefd', 'geschroefd'),
        ('gehaakt', 'gehaakt'),
        ('beide', 'beide'),
        ('anders', 'anders')],
        string='Are the pans screwed or hooked?',
        default='geschroefd', tracking=True)

    # Plat Dak -> Flat roof
    xaa_aa_gravel_on_roof = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Is there gravel on the roof?',
        default='nee', tracking=True)
    xaa_aa_plat_type_roof = fields.Selection([
        ('Bitumen', 'Bitumen'),
        ('EPDM', 'EPDM'),
        ('PVC', 'PVC'),
        ('Overige', 'Overige'),],
        string='What type (s) of roofing is it?',
        default='Bitumen', tracking=True)
    xaa_aa_roof_terminal_cabling = fields.Selection([
        ('ja', 'ja'),
        ('Nee aanleggen ECNL', 'Nee aanleggen ECNL'),
        ('nee', 'nee'),
        ('Nee klant draagt hier zorg voor', 'Nee klant draagt hier zorg voor'),],
        string='Is there a roof terminal for the string cabling',
        default='nee', tracking=True)

    # Meterkast -> Fuse box
    xaa_aa_main_switch = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),],
        string='Is there a main switch?',
        default='ja', tracking=True)
    xaa_aa_is_space_install_earth_leakage = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),],
        string='Is there a free space to install the earth leakage circuit breaker?',
        default='ja', tracking=True)

    # Omvormer -> Inverter
    xaa_aa_location_of_inverter = fields.Text(string='Location of the inverter')
    xaa_aa_is_space_inverter_cooling = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),],
        string='Is there sufficient free space around the inverter for cooling / ventilation purposes?',
        default='ja', tracking=True)
    xaa_aa_is_sturdy_rear_wall = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),],
        string='Is a sturdy rear wall available?',
        default='ja', tracking=True)
    xaa_aa_washing_machine_use = fields.Selection([
        ('ja', 'ja'),
        ('nee', 'nee'),],
        string='Can a washing machine connection be used?',
        default='nee', tracking=True)

    # Bekabeling -> Cabling
    xaa_aa_empty_pipe_use = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Can an empty pipe be used?',
        default='nee', tracking=True)
    xaa_aa_description_inverter = fields.Text(string='Description cable route panels -> inverter')
    xaa_aa_description_cable_inverter = fields.Text(string='Description cable inverter -> meter box')
    xaa_aa_description_utp_cable = fields.Text(default='NVT',
        string='Description UTP cable converter -> meter box')
    xaa_aa_want_mount_cable_himself = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Does the customer want to mount a cable himself?',
        default='nee', tracking=True)
    xaa_aa_diameter_of_cable = fields.Selection([
        ('3*2.5mm2', '3*2.5mm2'),
        ('5*2.5mm2', '5*2.5mm2'),
        ('3*4mm2', '3*4mm2'),
        ('5*4mm2', '5*4mm2'),
        ('5*6mm2', '5*6mm2'),
        ('5*10mm2', '5*10mm2'),],
        string='When using an existing cable what is the diameter of the cable?')
    xaa_aa_internet_connection_wired = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='The internet connection can be wired',tracking=True)

    # Overige -> Others
    xaa_aa_is_entrepreneurship = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Is there any entrepreneurship?',
        default='nee', tracking=True)
    xaa_aa_name_on_bill = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Does the name (incl. Initials) on the energy bill / contract match the name on the quote?',
        default='ja', tracking=True)
    xaa_aa_vat_exemption_rules = fields.Selection([
        ('ja', 'ja'),('nee', 'nee'),],
        string='Do you fall under VAT exemption rules?',
        default='nee', tracking=True)
    xaa_aa_preservation_product = fields.Selection([
        ('Nee', 'Nee'),
        ('Ja niet geinteresseerd', 'Ja niet geinteresseerd'),
        ('Ja geinteresseerd', 'Ja geinteresseerd'),
        ('Ja offerte', 'Ja offerte')],
        string='Do you need other preservation products?',
        default='Nee',tracking=True)
    xaa_aa_agreements_with_client = fields.Text(string='Other special agreements with client')
    xaa_aa_note = fields.Text(string='Note', tracking=True)

    xaa_aa_scaffolding_site = fields.Binary(string='Scaffolding site',
        tracking=True, attachment=True)
    xaa_aa_roof_2 = fields.Binary(string='Roof 2',
        tracking=True, attachment=True)
    xaa_aa_roof_3 = fields.Binary(string='Roof 3',
        tracking=True, attachment=True)
    xaa_aa_meter_cupboard_1 = fields.Binary(string='Meter cupboard 1',
        tracking=True, attachment=True)
    xaa_aa_meter_cupboard_2 = fields.Binary(string='Meter cupboard 2',
        tracking=True, attachment=True)
    xaa_aa_place_inverter_comes = fields.Binary(string='Place where the inverter comes',
        tracking=True, attachment=True)
    xaa_aa_cable_gradient_panels_inverter = fields.Binary(string='Cable gradient panels -> inverter',
        tracking=True, attachment=True)
    xaa_aa_cable_converter_converter_meter = fields.Binary(string='Cable converter converter -> meter box',
        tracking=True, attachment=True)
    xaa_aa_roof_plan = fields.Binary(string='Something special: Roof plan',
        tracking=True, attachment=True)
    xaa_aa_drawing_field_hand = fields.Binary(string='A drawing field where you with your hand',
        tracking=True, attachment=True)
    xaa_aa_parking_spot_three = fields.Binary(string='Parking spot',
        tracking=True, attachment=True)
    xaa_aa_house_three = fields.Binary(string='House / Property',
        tracking=True, attachment=True)
    xaa_aa_access_three = fields.Binary(string='Access',
        tracking=True, attachment=True)
    xaa_aa_roof1_three = fields.Binary(string='Roof 1',
        tracking=True, attachment=True)
    xaa_aa_obstacles_three = fields.Binary(string='Obstacles',
        tracking=True, attachment=True)

    #Question for Task
    # Algemeen -> General
    xaa_aa_system_vendor_name = fields.Char(string='Vendor name of the system',
        tracking=True)
    xaa_aa_email_address = fields.Char(string='E-mail address',
        tracking=True)
    xaa_aa_commencement_work_date = fields.Date(string='Date of commencement of work',
        tracking=True, default=datetime.date.today())
    xaa_aa_delivery_date = fields.Date(string='Delivery date',
        tracking=True, default=datetime.date.today())
    xaa_aa_mechanic_name_1 = fields.Char(string='Mechanic Name 1',
        tracking=True)
    xaa_aa_mechanic_name_2 = fields.Char(string='Mechanic Name 2',
        tracking=True)
    xaa_aa_mechanic_name_3 = fields.Char(string='Mechanic Name 3',
        tracking=True)

    # Dakwerk -> Roofing
    xaa_aa_any_damage_detected_start = fields.Selection([
        ('ja', 'ja'),('nee', 'nee')],
        string='Have any damage already been detected at the start of the work?',
        default='ja', tracking=True)
    xaa_aa_solar_panels_installed = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Have the solar panels been installed in accordance with the roof plan?',
        default='ja', tracking=True)
    xaa_aa_extra_solar_panels_installed = fields.Selection([
        ('Yes, enter the amount for other', 'Yes, enter the amount for other'), ('nee', 'nee')],
        string='Have additional solar panels been installed?',
        default='nee', tracking=True)
    xaa_aa_waterline_installed = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Have all plugs from the waterline been installed?',
        default='ja', tracking=True)
    xaa_aa_cables_separated = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Are the plus and minus cables separated?',
        default='ja', tracking=True)
    xaa_aa_pans_pushed = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Have all pans been pushed back?',
        default='ja', tracking=True)
    xaa_aa_is_representatives_inspection = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Is the inspection by the representatives correct?',
        default='ja', tracking=True)
    xaa_aa_is_roof_plan_fit = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Does the roof plan fit?',
        default='ja', tracking=True)
    xaa_aa_what_panel_installed = fields.Char(string='What panels have been installed?',
        tracking=True)

    # Elektrisch -> Electric
    xaa_aa_cabling_length = fields.Integer(string='Length of the used string cabling?')
    xaa_aa_cable_thickness = fields.Selection([
        ('4mm2', '4mm2'),
        ('6mm2', '6mm2'),
        ('10mm2', '10mm2')],
        string='Applied cable thickness of string cabling?',
        default='4mm2', tracking=True)
    xaa_aa_inverter_length = fields.Integer(string='Length of the inverter wiring used -> meter box?')
    xaa_aa_inverter_cable_thickness = fields.Selection([
        ('3x2,5mm2', '3x2,5mm2'),
        ('5x2,5mm2', '5x2,5mm2'),
        ('3x4mm2', '3x4mm2'),
        ('5x4mm2', '5x4mm2'),
        ('5x6mm2', '5x6mm2'),
        ('5x10mm2', '5x10mm2')],
        string='Applied cable thickness of the inverter -> meter box?',
        default='3x2,5mm2', tracking=True)
    xaa_aa_is_earthing_total_length = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Has the earthing been checked for correct installation?')
    xaa_aa_earthing_total_length = fields.Integer(string='What is the earth cable length?')
    xaa_aa_is_utp_total_length = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')], 
        string='Is the UTP cable connected correctly?')
    xaa_aa_utp_total_length = fields.Integer(string='What is the length of the UTP cable used?')
    xaa_aa_measured_voltage = fields.Integer(string='Measured string voltage - Value')
    xaa_aa_measured_panels_voltage = fields.Integer(string='Measured String Voltage - Panels')
    xaa_aa_measured_optimizers_voltage = fields.Integer(string='Measured string voltage - Number of optimizers')
    xaa_aa_internet_via = fields.Selection([
        ('UTP', 'UTP'),
        ('WiFi', 'WiFi'),
        ('Socket boxes', 'Socket boxes'),
        ('Customer arranges itself', 'Customer arranges itself'),
        ('No internet i.o.m. customer agreement', 'No internet i.o.m. customer agreement')],
        string='Internet connection established via?',
        default='UTP', tracking=True)
    xaa_aa_is_home_installation_ok = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Is the home installation still OK after installing the earth leakage circuit breaker?',
        tracking=True)

    # Overige -> Others
    xaa_aa_extra_panels = fields.Integer(
        string='How many panels have been installed extra?')
    xaa_aa_installation_damages = fields.Text(
        string='What damages have been detected or made during the installation process?')
    xaa_aa_other_remarks = fields.Text(string='Other remarks')

    # Afsluiting in te vullen door de de klant -> Closure to be completed by the customer
    xaa_aa_is_engineers_work_safely = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Did our engineers work safely with scaffolding or fall protection?',
        default='ja', tracking=True)
    xaa_aa_is_workplace_clean = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Has the workplace been left clean?',
        default='ja', tracking=True)
    xaa_aa_is_sufficient_explanation = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Have you received sufficient explanation during installation?',
        default='ja', tracking=True)
    xaa_aa_setting_explanation = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Did you have an explanation when setting up the monitoring app?',
        tracking=True)
    xaa_aa_any_comments = fields.Text(string='Do you have any comments for us?')
    xaa_aa_use_home_photos = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Can we use photos of your home as a reference on the internet?',
        tracking=True)
    xaa_aa_other_interested_customers = fields.Text(
        string='Do you have other customers who are also interested in our services?')
    xaa_aa_receive_order = fields.Char(
        string='order you receive a whopping € 100 application premium.')
    xaa_aa_other_discussed = fields.Text(string='Other discussed matters')

    # Welke foto's moeten worden genomen -> Which photos must be taken
    xaa_aa_cables_together_1 = fields.Binary(string='Are the plus and minus cables together 1',
        tracking=True, attachment=True)
    xaa_aa_cables_together_2 = fields.Binary(string='Are the plus and minus cables together 2',
        tracking=True, attachment=True)
    xaa_aa_cables_together_3 = fields.Binary(string='Are the plus and minus cables together 3',
        tracking=True, attachment=True)
    xaa_aa_pans_pushed_back = fields.Binary(string='All pans pushed back',
        tracking=True, attachment=True)
    xaa_aa_photo_roof_1 = fields.Binary(string='Overview photo roof 1',
        tracking=True, attachment=True)
    xaa_aa_photo_roof_2 = fields.Binary(string='Overview photo roof 2',
        tracking=True, attachment=True)
    xaa_aa_photo_roof_3 = fields.Binary(string='Overview photo roof 3',
        tracking=True, attachment=True)
    xaa_aa_outlet_inverter_roof = fields.Binary(string='Photo roof outlet inverter -> roof',
        tracking=True, attachment=True)
    xaa_aa_work_switch = fields.Binary(string='Photo opened work switch',
        tracking=True, attachment=True)
    xaa_aa_photo_placement_inverter = fields.Binary(string='Overview photo placement inverter + work switch',
        tracking=True, attachment=True)
    xaa_aa_inverter_in_operation = fields.Binary(string='Photo display inverter in operation',
        tracking=True, attachment=True)
    xaa_aa_inverter_internet = fields.Binary(string='Photo display inverter internet',
        tracking=True, attachment=True)
    xaa_aa_cupboard_opened = fields.Binary(string='Photo meter cupboard opened with automatic',
        tracking=True, attachment=True)
    xaa_aa_cupboard_closed = fields.Binary(string='Meter cupboard closed',
        tracking=True, attachment=True)
    xaa_aa_inverter_serial_number = fields.Binary(string='Photo serial number inverter',
        tracking=True, attachment=True)
    xaa_aa_optimizers_serial_number = fields.Binary(string='Photo serial numbers optimizers (Readable!)',
        tracking=True, attachment=True)

    #Questions for solar quote
    xaa_aa_energy_use = fields.Float(string='How much energy You use ?',
        tracking=True, default=1)
    xaa_aa_location_correction = fields.Integer(string="Location Correction",
        default=1)
    xaa_aa_location_calculation = fields.Float(string='Location Calculations',
        compute=compute_location, store=True)
    xaa_aa_solar_type = fields.Many2many('solar.type', string="Solar type")
    xaa_aa_solar_product = fields.Many2one('product.product',
        string='Which solar panel do you want?', tracking=True)
    xaa_aa_solar_watt_piek = fields.Float(string='Solar Energy Watt Piek',
        compute=get_energy_wat_piek, store=True)
    xaa_aa_energy_wat_piek = fields.Float(string='Energy Wat Piek Calclulation',
        compute=compute_energy_wat_piek, tracking=True, store=True)
    xaa_aa_need_converter = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do You need Converter ?',tracking=True)
    xaa_aa_converter_product = fields.Many2one('product.product',
        string='Which converter do you want ?', tracking=True)
    xaa_aa_pf_select_roof = fields.Selection([
        ('Flat Roof', 'Flat Roof'),
        ('Slanted Roof', 'Slanted Roof'),
        ('Mix Roof', 'Mix Roof')],
        string='Is it a flat roof or a slanted roof ?')
    xaa_aa_flat_roof_product = fields.Many2one('product.product',
        string='Which Flat roof system You want ?',
        tracking=True)
    xaa_aa_slanted_roof_product = fields.Many2one('product.product',
        string='Which Slanted roof system You want ?',
        tracking=True)
    xaa_aa_installation_time = fields.Selection([
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
    xaa_aa_stekkers_product = fields.Many2one('product.product',
        string='Which stekkers You want ?',
        tracking=True)
    xaa_aa_remain_material = fields.Many2one('product.product',
        string='Which Overige Materialen You want ?',
        tracking=True)
    xaa_aa_vat_refund_product = fields.Many2one('product.product',
        string='Which btw teruggave You want ?',
        tracking=True)
    xaa_aa_need_optimiser = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do You need product Optimisers ?',
        tracking=True)
    xaa_aa_optimiser_product = fields.Many2one('product.product',
        string='Which optimizer do you want ?',
        tracking=True)
    xaa_aa_need_discount_2 = fields.Selection([
        ('ja', 'ja'), ('nee', 'nee')],
        string='Do You need Discount 2 ?',
        tracking=True,)
    xaa_aa_amount_range = fields.Integer(string='Extra marge')
    xaa_aa_pv_need_custm_extra_product = fields.Selection([
        ('ja 1', 'ja 1'),
        ('ja 2', 'ja 2'),
        ('ja 3', 'ja 3'),
        ('nee', 'nee')],
        string="Do you need extra product ?",
        tracking=True)
    xaa_aa_pv_extra_product_description = fields.Char('Extra product 1: give description')
    xaa_aa_pv_extra_product_cost = fields.Float('Cost price')
    xaa_aa_pv_extra_product_sale = fields.Float('Sale price')
    xaa_aa_pv_extra_product_description_two = fields.Char('Extra product 2: give description')
    xaa_aa_pv_extra_product_cost_two = fields.Float('Cost price')
    xaa_aa_pv_extra_product_sale_two = fields.Float('Sale price')
    xaa_aa_pv_extra_product_description_three = fields.Char('Extra product 3: give description')
    xaa_aa_pv_extra_product_cost_three = fields.Float('Cost price')
    xaa_aa_pv_extra_product_sale_three = fields.Float('Sale price')

    xaa_aa_converter_price = fields.Float(string="Converter Price", default=1)
    xaa_aa_panel_price = fields.Float(string="Panel Price", default=1)
    xaa_aa_optimisers_price = fields.Float(string="Optimisers Price", default=1)
    xaa_aa_pv_cost_price_total = fields.Float(string="Cost price")

    # website quote for PV
    xaa_aa_details_are_correct = fields.Boolean(string='My details are correct', default=True)
    xaa_aa_energy_consumption = fields.Float(string='What is your energy consumption?')
    xaa_aa_count_people_in_house = fields.Integer(string='How many people live in your house?')

    xaa_aa_solar_pannel_product_id = fields.Many2one('product.product', 'What type of house do you live in?')
    xaa_aa_type_of_house_id = fields.Many2one('house.info', 'What type of house do you live in?')
    xaa_aa_type_of_roof_ids = fields.Many2one('roof.info', 'What kind of roof does your home have?')
    xaa_aa_how_roof_covered = fields.Selection([
        ('Dakpannen', 'Dakpannen'),
        ('Golfplaat', 'Golfplaat'),
        ('Riet', 'Riet')],
        string='How is your roof covered?',
        default="Dakpannen", tracking=True)
    xaa_aa_how_flat_roof_covered = fields.Selection([
        ('bitumen (dakleer) EDPM', 'bitumen (dakleer) EDPM'),
        ('PVC', 'PVC'),
        ('Groen dak', 'Groen dak')],
        string='How is your Flat roof covered?',
        default="bitumen (dakleer) EDPM", tracking=True)
    xaa_aa_location_of_roof = fields.Selection([
        ('Noord', 'Noord'),
        ('Oost', 'Oost'),
        ('Zuid', 'Zuid'),
        ('West', 'West'),
        ('Zuidoost', 'Zuidoost'),
        ('Zuidwest', 'Zuidwest'),
        ('Noordoost', 'Noordoost'),
        ('Noordwest', 'Noordwest'),
        ('Meerdere dakdelen', 'Meerdere dakdelen')],
        string='What is the location of your roof?',
        tracking=True)
    xaa_aa_obstacles_on_roof = fields.Selection([
        ('ja', 'ja'), ('nee','nee')],
        string='How is your roof covered?',
        tracking=True)
    xaa_aa_shadow_cast_solar_panels = fields.Selection([
        ('ja', 'ja'), ('nee','nee')],
        string='Do this shadow cast on your future solar panels?',
        tracking=True)

    xaa_aa_tree = fields.Boolean(string='Tree')
    xaa_aa_another_building = fields.Boolean(string='Another building')
    xaa_aa_obstacle_dormer = fields.Boolean(string='Dormer')
    xaa_aa_obstacle_chimney_or_air_inlet = fields.Boolean(string='chimney / air inlet')
    xaa_aa_obstacle_otherwise_namely = fields.Boolean(string='otherwise, namely')
    xaa_aa_explain_otherwise_namely = fields.Char(string='Explain')
    xaa_aa_percentage_correction = fields.Float(string="Percentage correction")
    xaa_aa_calculated_energy = fields.Float(string="Calculated energy")
    xaa_aa_calculated_panel_qty = fields.Float(string="Calculated panels")
    xaa_aa_choosen_panel_qty = fields.Integer(string="Choosen panels ")
    xaa_aa_energy_production = fields.Float(string="Energy production")


    # Quote stage questions
    # Bereikbaarheid / Accessibility
    xaa_aa_quote_scaffolding = fields.Selection(
        [('ja', 'ja'),
        ('nee', 'nee')],
        string='Is there a free space for scaffolding?',
        default='ja', tracking=True)
    xaa_aa_quote_place_scaffolding = fields.Selection(
        [('tuin', 'tuin'),
        ('grind', 'grind'),
        ('tegels', 'tegels'),
        ('anders, namelijk', 'anders, namelijk'),],
        string='What is at the place where we place the scaffolding?',
        default='tuin', tracking=True)
    xaa_aa_quote_place_scaffolding_text = fields.Char(string='Other place scaffolding')
    xaa_aa_quote_home_accessible = fields.Selection(
        [('goed', 'goed'),
        ('redelijk', 'redelijk'),
        ('slecht', 'slecht'),],
        string='Is your home easily accessible?',
        default='goed', tracking=True)
    xaa_aa_quote_home_parking = fields.Selection(
        [('goed', 'goed'),
        ('redelijk', 'redelijk'),
        ('slecht', 'slecht'),],
        string='How is the parking at your home?',
        default='goed', tracking=True)

    # Dak
    xaa_aa_quote_type_of_roof = fields.Selection(
        [('schuin', 'schuin'),
        ('plat', 'plat'),
        ('beide', 'beide'),
        ('anders, namelijk', 'anders, namelijk'),],
        string='What type of roof do you have?',
        default='schuin', tracking=True)
    xaa_aa_quote_type_of_roof_text = fields.Char(string='Other type of roof')
    xaa_aa_quote_schuin_roof_covered = fields.Selection(
        [('pannen', 'pannen'),
        ('golfplaten', 'golfplaten'),
        ('metaal', 'metaal'),
        ('bitumen', 'bitumen'),
        ('riet', 'riet'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='How is your pitched roof covered?',
        default='pannen', tracking=True)
    xaa_aa_quote_plat_roof_covered = fields.Selection(
        [('bitumen', 'bitumen'),
        ('kunststof', 'kunststof'),
        ('grind', 'grind'),
        ('sedum', 'sedum'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='How is your flat roof covered?',
        default='bitumen', tracking=True)
    xaa_aa_quote_condition_roof = fields.Selection(
        [('Het dak is goed', 'Het dak is goed'),
        ('Het dak is niet goed, maar ik laat hier iemand naar kijken', 'Het dak is niet goed, maar ik laat hier iemand naar kijken'),
        ('Ik heb een nieuwbouwwoning', 'Ik heb een nieuwbouwwoning'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='What is the condition of your roof?',
        default='Het dak is goed', tracking=True)
    xaa_aa_quote_edge_relevant_roof = fields.Selection(
        [('2,5 t/m 5 meter', '2,5 t/m 5 meter'),
        ('5 t/m 8 meter', '5 t/m 8 meter'),
        ('Hoger dan 8 meter', 'Hoger dan 8 meter'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='How high do you estimate the height from the ground to the edge of the relevant roof?',
        default='5 t/m 8 meter', tracking=True)
    xaa_aa_quote_incorporated_roof = fields.Selection(
        [('ja', 'ja'),
        ('nee', 'nee'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='Is asbestos incorporated in the roof?',
        default='nee', tracking=True)
    xaa_aa_quote_slope_roof = fields.Selection(
        [('0 - 10', '0 - 10'),
        ('10 - 45', '10 - 45'),
        ('boven 45', 'boven 45'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='What is the slope of the roof?',
        default='10 - 45', tracking=True)

    # step 3
    #Het plaatsen van de omvormer & bekabeling/Positioning the inverter and cabling
    xaa_aa_quote_description = fields.Text(string="Where do you want to mount your solar panels?")
    xaa_aa_quote_inverter_hang = fields.Selection(
        [('Ja, ik weet alleen niet zeker of dit technisch gezien kan.', 'Ja, ik weet alleen niet zeker of dit technisch gezien kan.'),
        ('Ja, ik heb dit uitgezocht en ben (vrijwel) zeker van een correcte, en eenvoudige montageplaats.','Ja, ik heb dit uitgezocht en ben (vrijwel) zeker van een correcte, en eenvoudige montageplaats.'),
        ('Ja, Ik heb dit uitgezocht en ben (vrijwel) zeker van een correcte, maar moeilijk te bereiken montageplaats: hiervoor moeten diverse ruimtes gepasseerd worden.', 'Ja, Ik heb dit uitgezocht en ben (vrijwel) zeker van een correcte, maar moeilijk te bereiken montageplaats: hiervoor moeten diverse ruimtes gepasseerd worden.'),
        ('Ja, ik heb zelfs een loze leiding waar rechtstreeks een kabel door kan naar de meterkast.','Ja, ik heb zelfs een loze leiding waar rechtstreeks een kabel door kan naar de meterkast.'),
        ('Nee, ik zou hierover graag extra advies krijgen.','Nee, ik zou hierover graag extra advies krijgen.'),],
        string='Do you have a good place in mind where the inverter can hang?',
        default='Ja, ik weet alleen niet zeker of dit technisch gezien kan.',
        tracking=True)
    xaa_aa_quote_meter_cupboard = fields.Selection(
        [('ja', 'ja'),
        ('Nee, maar er is een goed Wi-Fi ontvangst op de plek waar de omvormer komt te hangen.', 'Nee, maar er is een goed Wi-Fi ontvangst op de plek waar de omvormer komt te hangen.'),
        ('Nee, maar ik hoef de omvormer niet uit te lezen met mijn telefoon, tablet en- of computer.', 'Nee, maar ik hoef de omvormer niet uit te lezen met mijn telefoon, tablet en- of computer.'),],
        string='Is the router/internet port in the meter cupboard?',
        default='ja', tracking=True)
    xaa_aa_quote_lay_cable_description = fields.Text(string="How would you like to have the cables laid?")

    # step 5
    # Kop: Afsluitende vragen
    xaa_aa_quote_building_permit_required = fields.Selection(
        [('ja', 'ja'),
        ('nee', 'nee'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='Do you have a monument and / or building where a permit is required to do work on the outside of your home?',
        default="nee",tracking=True)
    xaa_aa_quote_occupied_home = fields.Selection(
        [('koop', 'koop'),
        ('huur', 'huur'),
        ('de woning moet nog aangekocht worden', 'de woning moet nog aangekocht worden'),],
        string='Do you have a rental or owner-occupied home?',
        default='koop',tracking=True)
    xaa_aa_quote_entrepreneur = fields.Selection(
        [('nee', 'nee'),
        ('Ik ben ondernemer maar mijn partner niet.', 'Ik ben ondernemer maar mijn partner niet.'),
        ('ja', 'ja'),
        ('Ik weet het niet', 'Ik weet het niet'),],
        string='Are you an entrepreneur?',
        default='nee',tracking=True)
    xaa_aa_quote_solar_panel_description = fields.Text(string="Do you have any important additions?")

    # step 6
    # foto’s van uw woning / photos of your home
    xaa_aa_quote_overview_roof_photo = fields.Binary(
        string='Overview photo of the roof (important)', attachment=True)
    xaa_aa_quote_location_inverter_photo = fields.Binary(
        string='Photo of the preferred location of the inverter (important)', attachment=True)
    xaa_aa_quote_meter_cupboard_photo = fields.Binary(
        string='Photograph of your meter cupboard (important)', attachment=True)
    xaa_aa_quote_placement_panels_photo = fields.Binary(
        string='Photograph or drawing of the desired placement of solar panels', attachment=True)
    xaa_aa_quote_where_cabling_photo = fields.Binary(
        string='Photo of where the cabling can go', attachment=True)
    xaa_aa_quote_extra_photo = fields.Binary(
        string='Extra photos', attachment=True)
    xaa_aa_quote_extra_photo_one = fields.Binary(
        string='Previously received quotation', attachment=True)

    # step 7
    xaa_aa_quote_final_approval = fields.Selection([
        ('Ik word graag gebeld om de offerte door te nemen van de spouwmuurisolatie en de woning wellicht binnen 5 werkdagen te hebben geisoleerd.', 'Ik word graag gebeld om de offerte door te nemen van de spouwmuurisolatie en de woning wellicht binnen 5 werkdagen te hebben geisoleerd.'),
        ('Ik word graag gebeld voor meer informatie over de spouwmuurisolatie.', 'Ik word graag gebeld voor meer informatie over de spouwmuurisolatie.'),
        ('Ik neem binnen twee weken telefonisch contact op.', 'Ik neem binnen twee weken telefonisch contact op.'),
        ('Ik neem deze offerte mee in mijn vergelijking en neem binnen twee weken contact op.','Ik neem deze offerte mee in mijn vergelijking en neem binnen twee weken contact op.'),
        ('Anders, namelijk','Anders, namelijk')],
        default='Ik word graag gebeld om de offerte door te nemen van de spouwmuurisolatie en de woning wellicht binnen 5 werkdagen te hebben geisoleerd.',
        string='What can we do for you now?')
    xaa_aa_quote_final_approval_text = fields.Char(string='Final approval description')
    xaa_aa_quote_final_approval_date = fields.Datetime(string="At what time would you like to be called about this?")

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
        if self.xaa_aa_formulier_type == 'formulier_three':
            Product = self.env['product.product'].sudo()
            solar_type_ids = self.env['solar.type'].sudo().search([])
            solar_product_ids = Product.search(domain+[
                ('xaa_aa_product_type', '=', 'Solar Panel'),
                ('xaa_aa_solar_type','in',self.xaa_aa_solar_type.ids)], order='xaa_aa_priority')
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
                        'solar_product_ids': solar_product_ids,
                        'converter_product_ids': converter_product_ids,
                        'flat_product_ids': flat_product_ids,
                        'slanted_product_ids': slanted_product_ids,
                        'optimiser_products': optimiser_products,
                        'iso_extra_product': iso_extra_product,
                        })
        return values
