odoo.define('formulier_type_4.solar_panel_calculation', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;

    $( document ).ready(function() {

        $(".update_panel_qty").on('click', function(e) {
            if (e.currentTarget.className.match('pf_add')){
                var old_val = e.currentTarget.previousElementSibling;
                if (parseInt(old_val.value) > 0){
                    old_val.value = parseInt(old_val.value) + 1;
                }
            }
            else{
                var old_val = e.currentTarget.nextElementSibling;
                if (parseInt(old_val.value) > 0){
                    old_val.value = parseInt(old_val.value) - 1;
                }
            }
        });
        $(".select_solar_color").on('change', function (e) {
            var solar_color = $("select[name='"+e.currentTarget.name+"']");
            ajax.jsonRpc("/formulier/pv_quote_infos", 'call', {'solar_color': solar_color.val()}).then(
                function(data) {
                    var solarProduct = $("select[name='xaa_aa_solar_product_one']");
                    solarProduct.html('');
                    solarProduct.append($('<option>'));
                    if (data.solar_products.length) {
                        _.each(data.solar_products, function(x) {
                            var opt = $('<option>').text(x[1])
                                .attr('value', x[0]);
                            solarProduct.append(opt);
                        });
                    }
                })
        });

        $("input[name='total_yield_chosen_panels']").on('change',function(e){
            var total_panel = $("input[name='total_yield_chosen_panels']")
            var annual_consumption = $("input[name='annual_consumption']")
            if (total_panel[0].value < annual_consumption[0].value) {
                $(".panel-warning").show();
            }
            else{
                $(".panel-warning").hide();
            }
        });
 
        $(".select_solar_product").on('change', function (e) {
            if (e.currentTarget.value){
                var roof_detail = $(e.currentTarget.parentElement.parentElement.parentElement.parentElement);
                var roof_type = roof_detail.find('.xaa_aa_roof_type_one, .xaa_aa_roof_type_two, .xaa_aa_roof_type_three, .xaa_aa_roof_type_four, .xaa_aa_roof_type_five, .xaa_aa_roof_type_six, .xaa_aa_roof_type_seven, .xaa_aa_roof_type_eight');
                var orientaion_type = roof_detail.find('.xaa_aa_orientaion_type_one, .xaa_aa_orientaion_type_two, .xaa_aa_orientaion_type_three, .xaa_aa_orientaion_type_four, .xaa_aa_orientaion_type_five, .xaa_aa_orientaion_type_six, .xaa_aa_orientaion_type_seven, .xaa_aa_orientaion_type_eight');
                var allData = {
                    "annual_consumption" : parseInt($("input[name='annual_consumption']").val()) || 0,
                    "roof_type": roof_type[0].innerText,
                    "orientaion_type" : orientaion_type[0].innerText,
                    "solar_pannel_product_id" : parseInt(e.currentTarget.value) || false,
                }
                ajax.jsonRpc("/formulier/panels_count", 'call', {
                    'data': allData,
                }).then(function(result) {
                    var solar_pannel = roof_detail.find('.solar_pannel_qty');
                    solar_pannel[0].value = result['panels'];
            });
            }
        });
    });
});
