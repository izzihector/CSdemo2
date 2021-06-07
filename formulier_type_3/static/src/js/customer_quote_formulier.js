odoo.define('formulier_type_3.customer_quote_formulier', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    $( document ).ready(function() {

        // check fields properly filled or not before go on next tab
        $('#quoteation_tab').on("click",function(e){
            var consumtion = parseInt($("input[name='xaa_aa_energy_consumption']").val());
            var count_people = parseInt($("input[name='xaa_aa_count_people_in_house']").val());
            var house_type = parseInt($(".house_info_li.selected").attr('data-id'));
            if (!(consumtion > 0 || (count_people > 0 && house_type))){
                alert("Please filled all required data.");
                return false;
            }
        });
        $('#energy_consumption_inner_tab').on("click",function(e){
            var count_people = parseInt($("input[name='xaa_aa_count_people_in_house']").val());
            if (!(count_people > 0)){
                alert("Please filled all required data.");
                return false;
            }
            return true;
        });
        $('#quote_tab_2').on("click",function(e){
            var location_of_roof = $("select[name='xaa_aa_location_of_roof']").val();
            var flat_roof_covered = $("select[name='xaa_aa_how_flat_roof_covered']").val();
            var roof_covered = $("select[name='xaa_aa_how_roof_covered']").val();
            var house_roof = parseInt($(".house_roof_li.selected").attr('data-id'));
            if (!(location_of_roof && (roof_covered || flat_roof_covered) && house_roof)){
                alert("Please filled all required data.");
                return false;
            }
            return true;
        });
        $("#summery_tab").on("click",function(e){
            var panel_qty = parseInt($("input[name='xaa_aa_choosen_panel_qty']").val());
            var solar_panel = parseInt($(".house_solar_panal_li.selected").attr('data-id'));
            if (!(panel_qty > 0 && solar_panel)){
                alert("Please filled all required data.");
                return false;
            }
            return true;
        })

        $('.house_info_li').on('click', function(e){
            var house_options = $('.house_info_li');
            _.each(house_options, function(house){
                $(house).removeClass('selected');
            })
            $(e.currentTarget).addClass('selected');
            $('.quotation_tab_next')[0].style='display:block';
        });

        $('.house_roof_li').on('click', function(e){
            $(".roof_covered_label")[0].style="display:block";
            if (e.currentTarget.getAttribute('data-name') == "plat dak"){
                $(".flat_roof_covered")[0].style="display:block";
                $(".roof_covered")[0].style="display:none";
            }
            else{
                $(".flat_roof_covered")[0].style="display:none";
                $(".roof_covered")[0].style="display:block";
            }
            var roof_options = $('.house_roof_li');
            _.each(roof_options, function(roof){
                $(roof).removeClass('selected');
            })
            $(e.currentTarget).addClass('selected')
        });

        function penal_count(data){
            ajax.jsonRpc("/formulier/panels/count", 'call', {
                    'quoteData': data,
                }).then(function(result) {
                    $('input[name="xaa_aa_choosen_panel_qty"]').attr2('value', result['xaa_aa_panels']);
                    $('input[name="xaa_aa_calculated_panel_qty"]').attr2('value', result['xaa_aa_panels']);
            });
        }

        $('#quote_tab_3').on('click', function(e){
            var obstacles_on_roof = $("select[name='xaa_aa_obstacles_on_roof']").val();
            if (obstacles_on_roof == 'ja'){
                var shadow_solar = $("select[name='xaa_aa_shadow_cast_solar_panels']").val();
                if (!(shadow_solar && obstacles_on_roof)){
                    alert("Please filled all required data.");
                    return false;
                }
            }
            else{
                if (!(obstacles_on_roof)){
                    alert("Please filled all required data.");
                    return false;
                }
            }
            var allData = {
                "xaa_aa_energy_consumption" : parseInt($("input[name='xaa_aa_energy_consumption']").val()) || 0,
                "xaa_aa_count_people_in_house" : $("input[name='xaa_aa_count_people_in_house']").val() || 0,
                "xaa_aa_type_of_roof_name": $(".house_roof_li.selected").attr('data-name') || '',
                "xaa_aa_location_of_roof" : $("select[name='xaa_aa_location_of_roof']").val(),
                "xaa_aa_solar_pannel_product_id" : parseInt($(".house_solar_panal_li.selected").attr('data-id')) || false,
            }
            if (allData['xaa_aa_solar_pannel_product_id']){
                penal_count(allData);
            }
        })

        $('.house_solar_panal_li').on('click', function(e){
            $('.solar_qty_show')[0].style="display:block";
            var roof_options = $('.house_solar_panal_li');
            _.each(roof_options, function(roof){
                $(roof).removeClass('selected');
            })
            $(e.currentTarget).addClass('selected')
            var allData = {
                "xaa_aa_energy_consumption" : parseInt($("input[name='xaa_aa_energy_consumption']").val()) || 0,
                "xaa_aa_count_people_in_house" : $("input[name='xaa_aa_count_people_in_house']").val() || 0,
                "xaa_aa_type_of_roof_name": $(".house_roof_li.selected").attr('data-name') || '',
                "xaa_aa_location_of_roof" : $("select[name='xaa_aa_location_of_roof']").val(),
                "xaa_aa_solar_pannel_product_id" : parseInt($(".house_solar_panal_li.selected").attr('data-id')) || false,
            }
            penal_count(allData);
        });
        $('.men_icon_class').on('click', function(e){
            var curr = $(e.currentTarget);
            $("input[name='xaa_aa_count_people_in_house']").attr('value', curr.attr('value'));
            curr.css( "color", "#78BD43" );
            curr.prevAll().css("color", "#78BD43");
            curr.nextAll().css("color", "lightgray");
            $('.span_amount').replaceWith("<div class='span_amount'><span> Geschat energieverbruik: "+curr.attr('data')+" kwh</span></div>");
        })

        //show hide form on btn click
        $('.btn_dont_know').click(function(){
            $('#energy_first_section')[0].style = 'display:none;';
            $('#energy_second_section')[0].style = 'display:block;';
        });

        $("input[name='xaa_aa_details_are_correct']").on("click",function(e){
            if (e.currentTarget.value == 'false'){
                $('.incorrect_info')[0].style.display = 'block';
            }
            else{
                $('.incorrect_info')[0].style.display = 'none';
            }
        });

        $("select[name='xaa_aa_obstacles_on_roof']").on("click change",function(e){
            if ($("select[name='xaa_aa_obstacles_on_roof']").val() == 'ja'){
                $(".shadow_cast_solar_panels")[0].style="display:block";
                $(".quotation_options")[0].style="display:block";
            }
            else {
                $(".shadow_cast_solar_panels")[0].style="display:none";
                $(".quotation_options")[0].style="display:none";
            }
        });
        $("input[name='xaa_aa_obstacle_otherwise_namely']").on("click",function(e){
            if ($("input[name='xaa_aa_obstacle_otherwise_namely']")[0].checked){
                $(".explain_otherwise_namely")[0].style="display:block";
            }
            else{
                $(".explain_otherwise_namely")[0].style="display:none";
            }
        })
        $("select[name='xaa_aa_how_flat_roof_covered']").on("click change", function(e){
            if ($("select[name='xaa_aa_how_flat_roof_covered']").val() == 'Groen dak'){
                $(".warning-image-display-flex")[0].style="display:flex";
            }
            else{
                $(".warning-image-display-flex")[0].style="display:none";
            }
        })
        $("select[name='xaa_aa_how_roof_covered']").on("click change", function(e){
            if ($("select[name='xaa_aa_how_roof_covered']").val() == 'Riet'){
                $(".warning-image-display-flex")[0].style="display:flex";
            }
            else{
                $(".warning-image-display-flex")[0].style="display:none";
            }
        })

        // submit website quote
        $("#summery_tab").on("click",function(e){
            var formulier_id = parseInt($(".btn-make-quote").val());
            var allData = {
                "xaa_aa_details_are_correct": $("input[name='xaa_aa_details_are_correct']")[0].checked,
                "xaa_aa_energy_consumption" : parseInt($("input[name='xaa_aa_energy_consumption']").val()) || 0,
                "xaa_aa_count_people_in_house" : $("input[name='xaa_aa_count_people_in_house']").val() || 0,
                "xaa_aa_type_of_house_id" : parseInt($(".house_info_li.selected").attr('data-id')) || false,
                "xaa_aa_type_of_house_name": $(".house_roof_li.selected").attr('data-name') || '',
                "xaa_aa_type_of_roof_ids" : parseInt($(".house_roof_li.selected").attr('data-id')) || false,
                "xaa_aa_type_of_roof_name": $(".house_roof_li.selected").attr('data-name') || '',
                "xaa_aa_how_roof_covered" : $("select[name='xaa_aa_how_roof_covered']").val(),
                "xaa_aa_how_flat_roof_covered" : $("select[name='xaa_aa_how_flat_roof_covered']").val(),
                "xaa_aa_location_of_roof" : $("select[name='xaa_aa_location_of_roof']").val(),
                "xaa_aa_obstacles_on_roof" : $("select[name='xaa_aa_obstacles_on_roof']").val(),
                "xaa_aa_shadow_cast_solar_panels" : $("select[name='xaa_aa_shadow_cast_solar_panels']").val(),
                "xaa_aa_tree" : $("input[name='xaa_aa_tree']")[0].checked,
                "xaa_aa_another_building" : $("input[name='xaa_aa_another_building']")[0].checked,
                "xaa_aa_obstacle_dormer" : $("input[name='xaa_aa_obstacle_dormer']")[0].checked,
                "xaa_aa_obstacle_chimney_or_air_inlet" : $("input[name='xaa_aa_obstacle_chimney_or_air_inlet']")[0].checked,
                "xaa_aa_obstacle_otherwise_namely" : $("input[name='xaa_aa_obstacle_otherwise_namely']")[0].checked,
                "xaa_aa_explain_otherwise_namely" : $("input[name='xaa_aa_explain_otherwise_namely']").val(),
                "xaa_aa_solar_pannel_product_id" : parseInt($(".house_solar_panal_li.selected").attr('data-id')) || false,
                "xaa_aa_choosen_panel_qty" : parseInt($("input[name='xaa_aa_choosen_panel_qty']").val()),
                "xaa_aa_calculated_panel_qty" : parseInt($("input[name='xaa_aa_calculated_panel_qty']").val()),
            }
            ajax.jsonRpc("/formulier/panels/count", 'call', {
                    'quoteData': allData,
                }).then(function(result) {
                    allData['xaa_aa_percentage_correction'] = result['xaa_aa_percentage_correction'];
                    allData['xaa_aa_calculated_energy'] = result['xaa_aa_calculated_energy'];
                    allData['xaa_aa_energy_production'] = parseInt($("input[name='xaa_aa_choosen_panel_qty']").val())*result['xaa_aa_panel_watt'];

                    // Summary view
                    $('.energy_consumtion_summary')[0].innerHTML = result['xaa_aa_energy_consumption'] + ' kwh';
                    $('.percentage_correction')[0].innerHTML = (result['xaa_aa_percentage_correction']*100) +'%';
                    $('.calculated_energy')[0].innerHTML = result['xaa_aa_calculated_energy'] + ' Wp';
                    $('.panel_name')[0].innerHTML = result['xaa_aa_panel_name'];
                    $('.panel_watt')[0].innerHTML = result['xaa_aa_panel_watt'] + ' Wp';
                    $('.calculated_panel_qty')[0].innerHTML = result['xaa_aa_panels'];
                    $('.choosen_panel_qty')[0].innerHTML = allData['xaa_aa_choosen_panel_qty'];
                    $('.energy_production')[0].innerHTML = allData['xaa_aa_energy_production'] + ' Wp';

                    // Save PF
                    $('#loading').show();
                    ajax.jsonRpc("/customer/pv/quote/submit", 'call', {
                                'quoteData': allData,
                                'formulier_id': formulier_id,
                    }).then(function(data) {
                        $('#loading').hide();
                    });
            });
            $(".btn-make-quote").on("click",function(e){
                $('#loading').show();
                if (allData['xaa_aa_solar_pannel_product_id']){
                    ajax.jsonRpc("/customer/pv/quote/create", 'call', {
                        'quoteData': allData,
                        'formulier_id': formulier_id,
                    }).then(function(data) {
                        $('#loading').hide();
                        window.open(data.url, '_self');
                    });
                }
                else{
                    alert("Please add Solar Panel Product");
                }
            })
        });
    });
});
