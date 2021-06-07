# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _


class ProjectFormulierInh(models.Model):
    _inherit = "question.formulier"

    def _default_line_ids(self):
        pr_lines = []
        foundation_img_ids = self.env['foundation.image'].search([])
        for foundation_id in foundation_img_ids:
            pr_lines.append((0, 0, {
                'xaa_aa_name': foundation_id.xaa_aa_name,
                'xaa_aa_image': foundation_id.xaa_aa_image,
            }))
        return pr_lines

    xaa_aa_house_info = fields.Text(string='Description of the House',
                            tracking=True,
                            default='Het betreft hier een aanbouw van gebouw uit 2000 welke aan linker zijde weg zakt')
    xaa_aa_goal_owner = fields.Text(string='Wish Owner',
                            tracking=True,
                            default='De wens van u is het stabiliseren van de fundering en indien mogelijk het liften hiervan')
    xaa_aa_analysis_settlement = fields.Text(
                            string='Our Analysis',
                            tracking=True,
                            default='Uit onze prik acties en Waterpasmetingen concluderen wij dat de draagkracht van de grond niet overal het zelfde is en dat het gebouw plaatselijk een grotere zetting heeft. Piekbelastingen door verbouw werkzaamheden. Verkeerstrillingen kunnen de situatie hebben verergerd.')
    xaa_aa_faced_construction = fields.Selection([
                            ('Spouwmuur', 'Spouwmuur'),
                            ('Steensmuur', 'Steensmuur'),
                            ('Halfsteensmuur met klamp', 'Halfsteensmuur met klamp')],
                            tracking=True,
                            string='Façade Construction', default='Spouwmuur')
    xaa_aa_area = fields.Selection([
                            ('Noord', 'Noord'),
                            ('Midden', 'Midden'),
                            ('Zuid', 'Zuid')],
                            string='Area', tracking=True)
    xaa_aa_floor_construction = fields.Selection([
                            ('zie tekening', 'zie tekening'),
                            ('Beton ; plaat op zand - Vrij tussen muren',
                            'Beton ; plaat op zand - Vrij tussen muren'),
                            ('Beton ; plaat op zand – verbonden aan muren',
                             'Beton ; plaat op zand – verbonden aan muren'),
                            ('Hout; vloerbalken oplegging – zijgevel',
                             'Hout; vloerbalken oplegging – zijgevel'),
                            ('Hout; vloerbalken oplegging – achtergevel',
                             'Hout; vloerbalken oplegging – achtergevel'),
                            ('Hout; vloerbalken oplegging – zie tekening',
                             'Hout; vloerbalken oplegging – zie tekening'),
                            ('Broodjes; balken oplegging – zijgevel',
                             'Broodjes; balken oplegging – zijgevel'),
                            ('Broodjes; balken oplegging – achtergevel',
                             'Broodjes; balken oplegging – achtergevel'),
                            ('Broodjes; balken oplegging - zie tekening', 'Broodjes; balken oplegging - zie tekening')],
                            string='Floor Construction bgg', tracking=True)
    xaa_aa_floor_construction_verd = fields.Selection([
                            ('zie tekening', 'zie tekening'),
                            ('Niet van toepassing', 'Niet van toepassing'),
                            ('Beton; kanaalplaat oplegging – zijgevel',
                             'Beton; kanaalplaat oplegging – zijgevel'),
                            ('Beton; kanaalplaat oplegging – achtergevel',
                             'Beton; kanaalplaat oplegging – achtergevel'),
                            ('Beton; kanaalplaat oplegging - zie tekening',
                             'Beton; kanaalplaat oplegging - zie tekening'),
                            ('Hout; vloerbalken oplegging – zijgevel',
                             'Hout; vloerbalken oplegging – zijgevel'),
                            ('Hout; vloerbalken oplegging – achtergevel',
                             'Hout; vloerbalken oplegging – achtergevel'),
                            ('Hout; vloerbalken oplegging – zie tekening', 'Hout; vloerbalken oplegging – zie tekening')],
                            string='Floor Construction 1* verdieping',
                            tracking=True)
    xaa_aa_floor_construction_verd_2 = fields.Selection([
                            ('zie tekening', 'zie tekening'),
                            ('Niet van toepassing', 'Niet van toepassing'),
                            ('Beton; kanaalplaat oplegging – zijgevel',
                            'Beton; kanaalplaat oplegging – zijgevel'),
                            ('Beton; kanaalplaat oplegging – achtergevel',
                            'Beton; kanaalplaat oplegging – achtergevel'),
                            ('Beton; kanaalplaat oplegging - zie tekening',
                            'Beton; kanaalplaat oplegging - zie tekening'),
                            ('Hout; vloerbalken oplegging – zijgevel',
                            'Hout; vloerbalken oplegging – zijgevel'),
                            ('Hout; vloerbalken oplegging – achtergevel',
                            'Hout; vloerbalken oplegging – achtergevel'),
                            ('Hout; vloerbalken oplegging – zie tekening', 'Hout; vloerbalken oplegging – zie tekening')],
                            string='Floor Construction 2* verdieping',
                            tracking=True)
    xaa_aa_leads = fields.Selection([
                            ('zie tekening', 'zie tekening'),
                            ('Niet van toepassing', 'Niet van toepassing'),
                            ('Beton; kanaalplaat oplegging – zijgevel',
                             'Beton; kanaalplaat oplegging – zijgevel'),
                            ('Beton; kanaalplaat oplegging – achtergevel',
                             'Beton; kanaalplaat oplegging – achtergevel'),
                            ('Beton; kanaalplaat oplegging - zie tekening',
                             'Beton; kanaalplaat oplegging - zie tekening'),
                            ('Hout; vloerbalken oplegging – zijgevel',
                             'Hout; vloerbalken oplegging – zijgevel'),
                            ('Hout; vloerbalken oplegging – achtergevel',
                             'Hout; vloerbalken oplegging – achtergevel'),
                            ('Hout; vloerbalken oplegging – zie tekening', 'Hout; vloerbalken oplegging – zie tekening')],
                            string='Leads', tracking=True)
    xaa_aa_dakbouw = fields.Selection([
                            ('Zie tekening', 'Zie tekening'),
                            ('Houten kapcontructie', 'Houten kapcontructie'),
                            ('Platdak Hout','Platdak Hout'),
                            ('Platdak Beton', 'Platdak Beton'),],
                           string='Dakopbouw', tracking=True)
    xaa_aa_roof_covering = fields.Selection([
                            ('dakpan', 'dakpan'),
                            ('bitumen', 'bitumen'),
                            ('glas', 'glas'),
                            ('riet', 'riet')],
                            string='Roof covering', tracking=True)
    xaa_aa_foundation_construction_ids = fields.One2many('foundation.image.selection',
                            'xaa_aa_formulier_id',
                            string="Foundation Construction",
                            default=_default_line_ids)
    xaa_aa_inspection_foundation_depth = fields.Text(string='Inspection well Foundation depth Groundwater',
                            tracking=True,
                            default='Fundering diepte cm onder Maaiveld \n Geen Grondwater op cm onder Maaiveld')
    xaa_aa_location_pipping_ground = fields.Text(string='Location of piping in the Ground (Info Residents)',
                            tracking=True,
                            default='Op cm afstand evenwijdig aan Achtergevel / Langs Gevel')
    xaa_aa_possible_settings = fields.Text(string='Possible cause of Setting',
                            tracking=True,
                            default='Weinig Draagkrachtige Grond met prikstok geconstateerd \n Piekbelasting door verbouw werkzaamheden')
    xaa_aa_action_resident = fields.Text(string='Action Resident',
                            tracking=True,
                            default='Gaat zelf Tuin opnieuw Aanleggen \n Will zelf Graafwerkzaamheden doen.')
    xaa_aa_action_total_wall = fields.Text(string='Action Total Wall',
                            tracking=True,
                            default='Stabiliseren / liften van Uitbouw \n Scheurherstel Buitengevel / binnen, Werkhoogte +/- mtr')
    xaa_aa_level_measurement_result = fields.Char(string='Level Measurement Result on Supplied Construction Plan',
                            tracking=True)
    xaa_aa_notes_calculation = fields.Text(string='Notes Engineering / Calculation',
                            tracking=True,
                            default='Werkzaamheden met .. man uitvoeren In werk controleren; …(wapening/fund. Afmeting) Palen ongeveer .. cm in dragende zandlaag aanbrengen Let op fundering diepte; niet te diep/laagdikte .. mtr Verwachte draaimoment; 3 kNm')

    xaa_aa_aantal_schroefpalen = fields.Integer(string='Aantal Schroefpalen')
    xaa_aa_sondering_diepte = fields.Integer(string='Depth bearing base layer t.o. reference in meters')
    xaa_aa_gkosten_funderingsherstel = fields.Integer(string='Gkosten Funderingsherstel')
    xaa_aa_gkosten_scheurherstel = fields.Integer(string='Gkosten Scheurherstel')
    xaa_aa_schroefpaaldiameter = fields.Selection([('360', '360'),('260', '260')],
                            string='Diameter Schroefpalen',tracking=True)

    xaa_aa_parkeren = fields.Text(string='Parkeren')
    xaa_aa_toegang = fields.Text(string='Toegang')
    xaa_aa_tuin = fields.Text(string='Tuin')
    xaa_aa_bomen = fields.Text(string='Bomen')
    xaa_aa_kraan = fields.Text(string='Kraan')
    xaa_aa_grondwerk = fields.Text(string='Grondwerk')
    xaa_aa_aanvullend = fields.Text(string='Aanvullend')

    xaa_aa_image_1 = fields.Binary(string='Left view of object',
                            tracking=True, attachment=True)
    xaa_aa_image_2 = fields.Binary(string='Front view of object',
                            tracking=True, attachment=True)
    xaa_aa_image_3 = fields.Binary(string='Right view of object',
                            tracking=True, attachment=True)
    xaa_aa_image_4 = fields.Binary(string='Level Measurement',
                            tracking=True, attachment=True)
    xaa_aa_image_5 = fields.Binary(string='Accessibility for Crane',
                            tracking=True, attachment=True)
    xaa_aa_image_6 = fields.Binary(string='Excavated Foundation',
                            tracking=True, attachment=True)
    xaa_aa_image_7 = fields.Binary(string='Crack in Masonry',
                            tracking=True, attachment=True)
    xaa_aa_image_8 = fields.Binary(string='Additional Information',
                            tracking=True, attachment=True)

    xaa_aa_plattegrond_img = fields.Binary(string='Map',
                            tracking=True, attachment=True)
    xaa_aa_fundering_img = fields.Binary(string='Foundation',
                            tracking=True, attachment=True)
    xaa_aa_blueprint_img = fields.Binary(string='Blueprint',
                            tracking=True, attachment=True)
    xaa_aa_lot_img = fields.Binary(string='Lot',
                            tracking=True, attachment=True)
    xaa_aa_extra_drawing_1_img = fields.Binary(string='Extra Drawing 1',
                            tracking=True, attachment=True)
    xaa_aa_extra_drawing_2_img = fields.Binary(string='Extra Drawing 2',
                            tracking=True, attachment=True)
    xaa_aa_note = fields.Text(string='Note')

class FoundationImageSelection(models.Model):
    _name = 'foundation.image.selection'
    _description = 'Formulier Foundation Construction Images'

    xaa_aa_name = fields.Char(string='Name')
    xaa_aa_image = fields.Binary(string='Image', attachment=True)
    xaa_aa_is_selected = fields.Boolean(string='-')
    xaa_aa_formulier_id = fields.Many2one('question.formulier',
                            string='Related Form', readonly=True)

class FoundationImage(models.Model):
    _name = 'foundation.image'
    _description = 'Formulier Foundation Images'

    xaa_aa_name = fields.Char(string='Name')
    xaa_aa_image = fields.Binary(string='Image', attachment=True)
