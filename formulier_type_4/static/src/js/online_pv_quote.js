odoo.define('formulier_type_4.online_pv_quote', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;

    $( document ).ready(function() {

        $(".btn_next_pv_formulier").on('click',function(e){
            var next_tab = $('#'+e.currentTarget.getAttribute('data-id'))[0].firstElementChild.click();
            var tab_id = $('#'+e.currentTarget.getAttribute('data-id'));
            tab_id.addClass('active');
            var prev_tab = $(tab_id[0].previousElementSibling)
            if (prev_tab.hasClass("online_pv_tabs_li")) {
                prev_tab.addClass("filled");
                prev_tab.removeClass("active");
            }
            $('body,html').animate({scrollTop: 0}, 200);
        });
        $(".btn_privoius_pv_formulier").on('click',function(e){
            var next_tab = $('#'+e.currentTarget.getAttribute('data-id'))[0].firstElementChild.click();
            var tab_id = $('#'+e.currentTarget.getAttribute('data-id'));
            tab_id.addClass('active');
            var prev_tab = $(tab_id[0].previousElementSibling)
            if (prev_tab.hasClass("online_pv_tabs_li")) {
                prev_tab.addClass("filled");
                prev_tab.removeClass("active");
            }
            $('body,html').animate({scrollTop: 0}, 200);
        });

        function aa_mounting_sys(roof) {
            ajax.jsonRpc("/formulier/pv_quote_infos", 'call', {'roof_type': roof.value}).then(
                function(data) {
                    if (roof.name.includes('xaa_aa_roof_type_one')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_one']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_two')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_two']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_three')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_three']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_four')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_four']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_five')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_five']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_six')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_six']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_seven')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_seven']");
                    }
                    else if (roof.name.includes('xaa_aa_roof_type_eight')){
                        var roofProduct = $("select[name='xaa_aa_mounting_sys_eight']");
                    }
                    roofProduct.html('');
                    roofProduct.append($('<option>'));
                    if (data.roof_products.length) {
                        _.each(data.roof_products, function(x) {
                            var opt = $('<option>').text(x[1])
                                .attr('value', x[0]);
                            roofProduct.append(opt);
                        });
                    }
                })
            }

        $(".roof_select_page").on('click',function(e){
            var roof_type = $(".roof_type");
            var roof_table = $('.roof_table_value');
            var roof_button = $(".btn-roof-details");
            _.each(roof_button, function(roof){
                $('#'+roof.dataset.id).hide();
            })
            _.each(roof_type, function(roof){
                if (roof.value){
                    $('#'+roof.name).show();
                    aa_mounting_sys(roof);
                }
                else{
                    $('#'+roof.name).hide();
                }
            })
            _.each(roof_table, function(roof){
                var roof_field = $('.'+roof.name);
                if (roof_field.length){
                    roof_field[0].textContent = roof.value;
                }
            })
        });

        $(".btn-roof-details").on('click',function(e){
            $('#'+e.currentTarget.dataset.id).toggle();
        });
    });
});
