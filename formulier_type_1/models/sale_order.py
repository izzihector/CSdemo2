# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    xaa_aa_formulier_type = fields.Selection(
        selection_add=[('formulier_one', 'Formulier one')])

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def fill_drawing_images(self):
        res = super(SaleOrder, self).fill_drawing_images()
        footer = ""
        description = ""
        imgDict = {}
        formulier_id = self.xaa_aa_formulier_id
        if self.website_description:
            description = self.website_description.encode('utf-8')
        if self.xaa_aa_website_desc_footer:
            footer = self.xaa_aa_website_desc_footer.encode('utf-8')

        if formulier_id and (description or footer):
            if self.sale_order_template_id and self.sale_order_template_id.xaa_aa_pdf_attachment and self.sale_order_template_id.xaa_aa_file_name_pdf:
                imgDict.update({' <a href="#" id="quotation_template_pdf" target="_blank">':
                                ' <a href="/web/content?model=sale.order.template&field=xaa_aa_pdf_attachment&id='+str(self.sale_order_template_id.id)+'&filename='+self.sale_order_template_id.xaa_aa_file_name_pdf+'&download=true" id="quotation_template_pdf" target="_blank">'})

            commonKey = '<img class="card-img-top img-border-style" src="/formulier_type_1/static/src/images/blank_image.jpg" alt="Odoo - Sample 1 for three columns"'
            commonVal = '<img class="card-img-top img-border-style" src=/web/image/question.formulier/' + str(formulier_id.id)
            img_key = '<img class="img img-fluid one_image_height_300" src="/formulier_type_1/static/src/images/blank_image.jpg"'
            img_val = '<img class="img img-fluid one_image_height_300" src=/web/image/question.formulier/'+ str(formulier_id.id)
            alt = 'alt="Odoo - Sample 1 for three columns"'

            # 6 image snippet and 1 main image
            if formulier_id.xaa_aa_plattegrond_img:
                imgDict.update({'%s id="f_map" loading="lazy">' % (commonKey):commonVal + '/xaa_aa_plattegrond_img' +' '+ alt + ' ' +'id="f_map" loading="lazy">'})
                imgDict.update({img_key+' alt="Pallateground Image" id="plattegrond_img_id" loading="lazy">':
                    img_val+'/xaa_aa_plattegrond_img' + ' ' + 'alt="Pallateground Image" id="plattegrond_img_id" loading="lazy">'})
            if formulier_id.xaa_aa_fundering_img:
                imgDict.update({'%s id="f_foundation" loading="lazy">' % (commonKey):commonVal + '/xaa_aa_fundering_img' +' '+ alt + ' ' +'id="f_foundation" loading="lazy">'})
                imgDict.update({img_key+' alt="Sondering Image" id="fundering_img_id" loading="lazy">':
                    img_val+'/xaa_aa_fundering_img' + ' ' + 'alt="Sondering Image" id="fundering_img_id" loading="lazy">'})
            if formulier_id.xaa_aa_blueprint_img:
                imgDict.update({'%s id="f_blue_print" loading="lazy">' % (commonKey): commonVal + '/xaa_aa_blueprint_img' +' '+ alt + ' ' +'id="f_blue_print" loading="lazy">',})
                imgDict.update({img_key+' alt="Bouwtekening Image" id="blueprint_img_id" loading="lazy">':
                    img_val+'/xaa_aa_blueprint_img' + ' ' + 'alt="Bouwtekening Image" id="blueprint_img_id" loading="lazy">'})
            if formulier_id.xaa_aa_lot_img:
                imgDict.update({'%s id="f_lot" loading="lazy">' % (commonKey): commonVal + '/xaa_aa_lot_img' +' '+ alt + ' ' +'id="f_lot" loading="lazy">',})
                imgDict.update({img_key+' alt="Kavel Image" id="lot_img_id" loading="lazy">':
                    img_val+'/xaa_aa_lot_img' + ' ' + 'alt="Kavel Image" id="lot_img_id" loading="lazy">'})
            if formulier_id.xaa_aa_extra_drawing_1_img:
                imgDict.update({'%s id="f_extra_Drawing_1" loading="lazy">' % (commonKey): commonVal + '/xaa_aa_extra_drawing_1_img' +' '+ alt + ' ' +'id="f_extra_Drawing_1" loading="lazy">',})
                imgDict.update({img_key+' alt="Extra tekening 1 Image" id="extra_drawing_1_img_id" loading="lazy">':
                    img_val+'/xaa_aa_extra_drawing_1_img' + ' ' + 'alt="Extra tekening 1 Image" id="extra_drawing_1_img_id" loading="lazy">'})
            if formulier_id.xaa_aa_extra_drawing_2_img:
                imgDict.update({'%s id="f_extra_Drawing_2" loading="lazy">' % (commonKey): commonVal + '/xaa_aa_extra_drawing_2_img' +' '+ alt + ' ' +'id="f_extra_Drawing_2" loading="lazy">'})
                imgDict.update({img_key+' alt="Extra tekening 2 Image" id="extra_drawing_2_img_id" loading="lazy">':
                    img_val+'/xaa_aa_extra_drawing_2_img' + ' ' + 'alt="Extra tekening 2 Image" id="extra_drawing_2_img_id" loading="lazy">'})
            if formulier_id.xaa_aa_image:
                bannerKey = '<img src="/formulier_type_1/static/src/images/blank_image.jpg" class="img img-fluid" alt="Project Formulier" id="level_measurement_img" loading="lazy">' 
                imgDict.update({bannerKey:
                    '<img class="img img-fluid" src=/web/image/question.formulier/'+ str(formulier_id.id) + '/xaa_aa_image' + ' ' + 'alt="Project Formulier" id="level_measurement_img" loading="lazy">'})

            # 8 image snippet
            commonKey = '<img class="card-img-top img-height-65" src="/formulier_type_1/static/src/images/blank_image.jpg" alt="PF image"'
            commonVal = '<img class="card-img-top img-height-65" src=/web/image/question.formulier/' + str(formulier_id.id)

            if formulier_id.xaa_aa_image_1:
                imgDict.update({commonKey+' id="f_image_1" loading="lazy">':
                    commonVal+'/xaa_aa_image_1' + ' ' + ' alt="PF image" id="f_image_1" loading="lazy"/>'})
            if formulier_id.xaa_aa_image_2:
                imgDict.update({commonKey+' id="f_image_2" loading="lazy">':
                    commonVal+'/xaa_aa_image_2' + ' ' + ' alt="PF image" id="f_image_2" loading="lazy">'})
            if formulier_id.xaa_aa_image_3:
                imgDict.update({commonKey+' id="f_image_3" loading="lazy">':
                    commonVal+'/xaa_aa_image_3' + ' ' + ' alt="PF image" id="f_image_3" loading="lazy">'})
            if formulier_id.xaa_aa_image_4:
                imgDict.update({commonKey+' id="f_image_4" loading="lazy">':
                    commonVal+'/xaa_aa_image_4' + ' ' + ' alt="PF image" id="f_image_4" loading="lazy">'})
            if formulier_id.xaa_aa_image_5:
                imgDict.update({commonKey+' id="f_image_5" loading="lazy">':
                    commonVal+'/xaa_aa_image_5' + ' ' + ' alt="PF image" id="f_image_5" loading="lazy">'})
            if formulier_id.xaa_aa_image_6:
                imgDict.update({commonKey+' id="f_image_6" loading="lazy">':
                    commonVal+'/xaa_aa_image_6' + ' ' + ' alt="PF image" id="f_image_6" loading="lazy">'})
            if formulier_id.xaa_aa_image_7:
                imgDict.update({commonKey+' id="f_image_7" loading="lazy">':
                    commonVal+'/xaa_aa_image_7' + ' ' + ' alt="PF image" id="f_image_7" loading="lazy">'})
            if formulier_id.xaa_aa_image_8:
                imgDict.update({commonKey+' id="f_image_8" loading="lazy">':
                    commonVal+'/xaa_aa_image_8' + ' ' + ' alt="PF image" id="f_image_8" loading="lazy">'})

            # Situatie snippet
            if formulier_id.xaa_aa_house_info:
                imgDict.update({'<p id="g_s_houseinfo_new_value" class="o_default_snippet_text">Double click an icon to replace it with one of your choice.</p>':
                                '<p id="g_s_houseinfo_new_value" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_house_info)+'</p>'})
            if formulier_id.xaa_aa_goal_owner:
                imgDict.update({'<p id="g_s_goal_owner_new_value" class="o_default_snippet_text">Double click an icon to replace it with one of your choice.</p>':
                                '<p id="g_s_goal_owner_new_value" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_goal_owner)+'</p>'})
            if formulier_id.xaa_aa_analysis_settlement:
                imgDict.update({'<p id="g_s_analysis_new_value" class="o_default_snippet_text">Duplicate blocks and columns to add more features.</p>':
                                '<p id="g_s_analysis_new_value" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_analysis_settlement)+'</p>'})

            # Snippet Inleiding
            if formulier_id.xaa_aa_lead_id and formulier_id.xaa_aa_lead_id.user_id:
                imgDict.update({'<span id="quot_name" class="o_default_snippet_text">Dhr Ferry Nieuwboer':
                                '<span id="quot_name" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_lead_id.user_id.name)})
            if formulier_id.xaa_aa_date_opportunity:
                imgDict.update({'<span id="quote_date" class="o_default_snippet_text">date</span>':
                                '<span id="quote_date" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_date_opportunity)+'</span>'})
            if formulier_id.xaa_aa_lead_id:
                imgDict.update({'<span id="quote_soort" class="o_default_snippet_text">aanbouw/ hoek/ kopgevel/groot deel </span>':
                                '<span id="quote_soort" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_lead_id.xaa_aa_soort)+'</span>'})
            if formulier_id.xaa_aa_partner_id and formulier_id.xaa_aa_partner_id.street:
                imgDict.update({'<span id="customer_street" class="o_default_snippet_text">street</span>':
                                '<span id="customer_street" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_partner_id.street)+'</span>'})
            if formulier_id.xaa_aa_partner_id and formulier_id.xaa_aa_partner_id.city:
                imgDict.update({'<span id="customer_city" class="o_default_snippet_text">Great stories</span>':
                                '<span id="customer_city" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_partner_id.city)+'</span>'})

            # Snippet Opportunity Question Table
            if (description and str(description).find('formiler_data_table') != -1) or (footer and str(footer).find('formiler_data_table') != -1):
                my_dict = {}
                for foundation_construction_id in formulier_id.xaa_aa_foundation_construction_ids:
                    if foundation_construction_id.xaa_aa_is_selected == True:
                        my_dict.update({'foundation_construction_name': foundation_construction_id.xaa_aa_name,
                                        'foundation_construction_image': foundation_construction_id.xaa_aa_image})
                if my_dict:
                    imgDict.update({'<span id="foundation_construction_name_image_id" class="o_default_snippet_text">foundation construction ids</span>':
                                    '<span id="foundation_construction_name_image_id" class="o_default_snippet_text">' + my_dict.get('foundation_construction_name') + '<img src="data:image/jpeg;base64,'+str(my_dict.get('foundation_construction_image'))+'"/> </span>'})
                if formulier_id.xaa_aa_faced_construction:
                    imgDict.update({'<span id="faced_construction_id" class="o_default_snippet_text">Gevelopbouw</span>':
                                    '<span id="faced_construction_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_faced_construction)+'</span>'})
                if formulier_id.xaa_aa_floor_construction:
                    imgDict.update({'<span id="flore_construction_id" class="o_default_snippet_text">Vloeropbouw bgg</span>':
                                    '<span id="flore_construction_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_floor_construction)+'</span>'})
                if formulier_id.xaa_aa_floor_construction_verd:
                    imgDict.update({'<span id="floor_construction_verd_id" class="o_default_snippet_text">Vloeropbouw 1* verdieping</span>':
                                    '<span id="floor_construction_verd_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_floor_construction_verd)+'</span>'})
                if formulier_id.xaa_aa_floor_construction_verd_2:
                    imgDict.update({'<span id="floor_construction_verd_2_id" class="o_default_snippet_text">Vloeropbouw 2* verdieping</span>':
                                    '<span id="floor_construction_verd_2_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_floor_construction_verd_2)+'</span>'})
                if formulier_id.xaa_aa_leads:
                    imgDict.update({'<span id="lead_id" class="o_default_snippet_text">Leads</span>':
                                    '<span id="lead_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_leads)+'</span>'})
                if formulier_id.xaa_aa_dakbouw:
                    imgDict.update({'<span id="Dakbouw_id" class="o_default_snippet_text">Dakopbouw</span>':
                                    '<span id="Dakbouw_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_dakbouw)+'</span>'})
                if formulier_id.xaa_aa_inspection_foundation_depth:
                    imgDict.update({'<span id="inspection_foundation_depth_id" class="o_default_snippet_text">Inspectie Putje</span>':
                                    '<span id="inspection_foundation_depth_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_inspection_foundation_depth)+'</span>'})
                if formulier_id.xaa_aa_location_pipping_ground:
                    imgDict.update({'<span id="location_pipping_ground_id" class="o_default_snippet_text">Ligging leidingwerk</span>':
                                    '<span id="location_pipping_ground_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_location_pipping_ground)+'</span>'})
                if formulier_id.xaa_aa_possible_settings:
                    imgDict.update({'<span id="possible_settings_id" class="o_default_snippet_text">Maximale gemeten zetting</span>':
                                    '<span id="possible_settings_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_possible_settings)+'</span>'})
                if formulier_id.xaa_aa_action_resident:
                    imgDict.update({'<span id="action_resident_id" class="o_default_snippet_text">Actie Bewoner</span>':
                                    '<span id="action_resident_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_action_resident)+'</span>'})
                if formulier_id.xaa_aa_action_total_wall:
                    imgDict.update({'<span id="action_total_wall_id" class="o_default_snippet_text">Actie DFH</span>':
                                    '<span id="action_total_wall_id" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_action_total_wall)+'</span>'})
                if formulier_id.xaa_aa_parkeren:
                    imgDict.update({'<span id="parkeren" class="o_default_snippet_text">Parkeren</span>':
                                    '<span id="parkeren" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_parkeren)+'</span>'})
                if formulier_id.xaa_aa_toegang:
                    imgDict.update({'<span id="toegang" class="o_default_snippet_text">Toegang</span>':
                                    '<span id="toegang" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_toegang)+'</span>'})
                if formulier_id.xaa_aa_tuin:
                    imgDict.update({'<span id="tuin" class="o_default_snippet_text">Tuin</span>':
                                    '<span id="tuin" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_tuin)+'</span>'})
                if formulier_id.xaa_aa_bomen:
                    imgDict.update({'<span id="bomen" class="o_default_snippet_text">Bomen</span>':
                                    '<span id="bomen" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_bomen)+'</span>'})
                if formulier_id.xaa_aa_kraan:
                    imgDict.update({'<span id="kraan" class="o_default_snippet_text">Kraan</span>':
                                    '<span id="kraan" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_kraan)+'</span>'})
                if formulier_id.xaa_aa_grondwerk:
                    imgDict.update({'<span id="grondwerk" class="o_default_snippet_text">Grondwerk</span>':
                                    '<span id="grondwerk" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_grondwerk)+'</span>'})
                if formulier_id.xaa_aa_aanvullend:
                    imgDict.update({'<span id="aanvullend" class="o_default_snippet_text">Aanvullend</span>':
                                    '<span id="aanvullend" class="o_default_snippet_text">'+str(formulier_id.xaa_aa_aanvullend)+'</span>'})

            if description:
                for key, val in imgDict.items():
                    description = description.replace(
                        key.encode('utf-8'), val.encode('utf-8'))
                self.website_description = description
            if footer:
                for key, val in imgDict.items():
                    footer = footer.replace(
                        key.encode('utf-8'), val.encode('utf-8'))
                self.xaa_aa_website_desc_footer = footer
        return self.website_description

