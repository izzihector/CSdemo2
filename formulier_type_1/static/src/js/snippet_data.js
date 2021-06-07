function formulier_type_one(){
    var curr_page = $(document);
    url = curr_page.attr('location').pathname
    if (url.indexOf('/my/orders/') == 0){
        sale_id = url.split('/')[3];
        $.ajax({
            url: "/order/snippet/dynamic_value",
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'sale_id': parseInt(sale_id)} }),
            async: false,
            success: function (result) {
                if(result.result.formulier_id){
                    var que_id = result.result.formulier_id;
                    var record = result.result;
                    if($('#quotation_snippet_structure').find($('#quotation_template_pdf')).length && record.quotation_template_id && record.pdf_name){
                        $('#quotation_template_pdf')[0].href='/web/content?model=sale.order.template&field=xaa_aa_pdf_attachment&id='+record.quotation_template_id+'&filename='+record.pdf_name+'&download=true';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_1')).length && record.xaa_aa_image_1 != false){
                        $('#f_image_1')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_1';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_2')).length && record.xaa_aa_image_2 != false){
                        $('#f_image_2')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_2';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_3')).length && record.xaa_aa_image_3 != false){
                        $('#f_image_3')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_3';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_4')).length && record.xaa_aa_image_4 != false){
                        $('#f_image_4')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_4';
                    }
                    if($('#quotation_snippet_structure').find($('#g_s_analysis')).length){
                        $('#g_s_analysis').replaceWith('<div class="s_features_grid_content"id="g_s_houseinfo" ><h4> Analysis cracking / settlement </h4><p>'+ record.xaa_aa_analysis_settlement +'</p></div>');
                    }
                    if($('#quotation_snippet_structure').find($('#g_s_goal_owner')).length){
                        $('#g_s_goal_owner').replaceWith('<div class="s_features_grid_content"id="g_s_houseinfo" ><h4> Leads </h4><p>'+ record.xaa_aa_goal_owner +'</p></div>');
                    }
                    if($('#quotation_snippet_structure').find($('#ac_totle')).length){
                        $('#ac_totle').replaceWith('<div class="s_features_grid_content"id="g_s_houseinfo" ><h4> Action Total Wall </h4><p>'+ record.xaa_aa_action_total_wall +'</p></div>');
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_5')).length && record.xaa_aa_image_5 != false){
                        $('#f_image_5')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_5';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_6')).length && record.xaa_aa_image_6 != false){
                        $('#f_image_6')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_6';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_7')).length && record.xaa_aa_image_7 != false){
                        $('#f_image_7')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_7';
                    }
                    if($('#quotation_snippet_structure').find($('#f_image_8')).length && record.xaa_aa_image_8 != false){
                        $('#f_image_8')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image_8';
                    }
                    if($('#quotation_snippet_structure').find($('#quot_name')).length){
                        $('#quot_name').replaceWith('<span id="quot_name">'+ record.quot_name +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#quote_soort')).length){
                        $('#quote_soort').replaceWith('<span id="quote_soort">'+ record.quote_soort +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#customer_city')).length){
                        $('#customer_city').replaceWith('<span id="customer_city">'+ record.customer_city +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#customer_street')).length){
                        $('#customer_street').replaceWith('<span id="customer_street">'+ record.customer_street +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#quote_date')).length){
                        $('#quote_date').replaceWith('<span id="quote_date">'+ record.quote_date +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#g_s_houseinfo_new')).length){
                        $('#g_s_houseinfo_new').replaceWith('<div class="s_features_grid_content"id="g_s_houseinfo_new" ><p>'+ record.xaa_aa_house_info +'</p></div>');
                    }
                    if($('#quotation_snippet_structure').find($('#faced_construction_id')).length){
                        $('#faced_construction_id').replaceWith('<span>'+ record.xaa_aa_faced_construction +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#flore_construction_id')).length){
                        $('#flore_construction_id').replaceWith('<span>'+ record.xaa_aa_floor_construction +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#floor_construction_verd_id')).length){
                        $('#floor_construction_verd_id').replaceWith('<span>'+ record.xaa_aa_floor_construction_verd +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#floor_construction_verd_2_id')).length){
                        $('#floor_construction_verd_2_id').replaceWith('<span>'+ record.xaa_aa_floor_construction_verd_2 +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#Dakbouw_id')).length){
                        $('#Dakbouw_id').replaceWith('<span>'+ record.xaa_aa_dakbouw +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#action_resident_id')).length){
                        $('#action_resident_id').replaceWith('<span>'+ record.xaa_aa_action_resident +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#lead_id')).length){
                        $('#lead_id').replaceWith('<span id="lead_id">'+ record.leads +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#foundation_construction_name_image_id')).length){
                        $('#foundation_construction_name_image_id').replaceWith('<span id="foundation_construction_name_image_id">'+ record.foundation_construction_name + '<img src="data:image/jpeg;base64,'+record.foundation_construction_image+'"/> </span>');
                    }
                    if($('#quotation_snippet_structure').find($('#inspection_foundation_depth_id')).length){
                        $('#inspection_foundation_depth_id').replaceWith('<span id="inspection_foundation_depth_id">'+ record.xaa_aa_inspection_foundation_depth +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#location_pipping_ground_id')).length){
                        $('#location_pipping_ground_id').replaceWith('<span id="location_pipping_ground_id">'+ record.xaa_aa_location_pipping_ground +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#possible_settings_id')).length){
                        $('#possible_settings_id').replaceWith('<span id="possible_settings_id">'+ record.xaa_aa_possible_settings +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#action_total_wall_id')).length){
                        $('#action_total_wall_id').replaceWith('<span id="action_total_wall_id">'+ record.xaa_aa_action_total_wall +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#parkeren')).length){
                        $('#parkeren').replaceWith('<span id="parkeren">'+ record.xaa_aa_parkeren +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#toegang')).length){
                        $('#toegang').replaceWith('<span id="toegang">'+ record.xaa_aa_toegang +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#tuin')).length){
                        $('#tuin').replaceWith('<span id="tuin">'+ record.xaa_aa_tuin +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#bomen')).length){
                        $('#bomen').replaceWith('<span id="bomen">'+ record.xaa_aa_bomen +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#kraan')).length){
                        $('#kraan').replaceWith('<span id="kraan">'+ record.xaa_aa_kraan +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#grondwerk')).length){
                        $('#grondwerk').replaceWith('<span id="grondwerk">'+ record.xaa_aa_grondwerk +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#aanvullend')).length){
                        $('#aanvullend').replaceWith('<span id="aanvullend">'+ record.xaa_aa_aanvullend +'</span>');
                    }
                    if($('#quotation_snippet_structure').find($('#level_measurement_img')).length && record.image != false){
                        $('#level_measurement_img')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_image';
                    }
                    if($('#quotation_snippet_structure').find($('#f_map')).length && record.xaa_aa_plattegrond_img != false){
                        $('#f_map')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_plattegrond_img';
                    }
                    if($('#quotation_snippet_structure').find($('#f_foundation')).length && record.xaa_aa_fundering_img != false){
                        $('#f_foundation')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_fundering_img';
                    }
                    if($('#quotation_snippet_structure').find($('#f_blue_print')).length && record.xaa_aa_blueprint_img != false){
                        $('#f_blue_print')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_blueprint_img';
                    }
                    if($('#quotation_snippet_structure').find($('#f_lot')).length && record.xaa_aa_lot_img != false){
                        $('#f_lot')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_lot_img';
                    }
                    if($('#quotation_snippet_structure').find($('#f_extra_Drawing_1')).length && record.xaa_aa_extra_drawing_1_img != false){
                        $('#f_extra_Drawing_1')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_extra_drawing_1_img';
                    }
                    if($('#quotation_snippet_structure').find($('#f_extra_Drawing_2')).length && record.xaa_aa_extra_drawing_2_img != false){
                        $('#f_extra_Drawing_2')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_extra_drawing_2_img';
                    }
                    if($('#quotation_snippet_structure').find($('#plattegrond_img_id')).length && record.xaa_aa_plattegrond_img != false){
                        $('#plattegrond_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_plattegrond_img';
                    }
                    if($('#quotation_snippet_structure').find($('#fundering_img_id')).length && record.xaa_aa_fundering_img != false){
                        $('#fundering_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_fundering_img';
                    }
                    if($('#quotation_snippet_structure').find($('#blueprint_img_id')).length && record.xaa_aa_blueprint_img != false){
                        $('#blueprint_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_blueprint_img';
                    }
                    if($('#quotation_snippet_structure').find($('#lot_img_id')).length && record.xaa_aa_lot_img != false){
                        $('#lot_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_lot_img';
                    }
                    if($('#quotation_snippet_structure').find($('#extra_drawing_1_img_id')).length && record.xaa_aa_extra_drawing_1_img != false){
                        $('#extra_drawing_1_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_extra_drawing_1_img';
                    }
                    if($('#quotation_snippet_structure').find($('#extra_drawing_2_img_id')).length && record.xaa_aa_extra_drawing_2_img != false){
                        $('#extra_drawing_2_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_extra_drawing_2_img';
                    }
                }
            },
        });
    }
}
