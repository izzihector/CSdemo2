odoo.define('formulier_type_3.online_pv_quote', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;

    $( document ).ready(function() {
        var clickwatch = (function(){
              var timer = 0;
              return function(callback, ms){
                clearTimeout(timer);
                timer = setTimeout(callback, ms);
              };
        })();

        $(function(){
            $("select[name='xaa_aa_solar_type']").select2();
        });

        if ($("#nav_tabs_solar_form").length) {
            function installation_time() {
                var solar_qty = parseInt($('.solar_qty')[0].value);
                var installation_time = $("select[name='xaa_aa_installation_time']")[0];
                if (solar_qty > 0){
                    ajax.jsonRpc("/formulier/get_installation_time", 'call', {'solar_qty': solar_qty}).then(
                        function(data) {
                            var record = $(this);
                            record.hours = data.hours;
                            _.each(installation_time.options, function(op) {
                                if (op.getAttribute('value') == record.hours){
                                    installation_time.selectedIndex = op.index;
                                }
                            });
                    });
                }
            }
            $(this).on('change', "input[name='xaa_aa_energy_use'] , input[name='xaa_aa_location_correction']", function () {
                clickwatch(function() {
                    if ($("input[name='xaa_aa_energy_use']").val()) {
                        if ($("input[name='xaa_aa_location_correction']").val()) {
                            var loc_calculation = $("input[name='xaa_aa_energy_use']").val() / ($("input[name='xaa_aa_location_correction']").val()/100);
                            $("input[name='xaa_aa_location_calculation']").attr2('value', parseInt(loc_calculation));
                        }
                    }
                }, 500);
            });
            $(this).on('change', "select[name='xaa_aa_solar_type']", function (e) {
                clickwatch(function() {
                    ajax.jsonRpc("/formulier/quote_infos", 'call', {'xaa_aa_solar_type': $("select[name='xaa_aa_solar_type']").val()}).then(
                        function(data) {
                            $('.solar_product').show();
                            // $('.panel_price').hide();
                            $('.solar_product_qty_show').hide();
                            var solar_product = $('.solar_product_section').html('');
                            if (data.solar_product_ids.length) {
                                var selected = '';
                                if (data.solar_product_ids.length == 1){
                                    var selected = 'selected ';
                                }
                                _.each(data.solar_product_ids, function(x) {
                                    var record = '<div class="'+selected+'col-lg-6 col-md-6 col-sm-6 col-xs-12 padding_14_10 solar_product_li product_li text-center mt8" data-id="'+x[0]+'">\
                                    <div class="text-center mt4">'
                                    if(x[2]){
                                        record +='<span style="font-size:16px;">'+x[2]+'</span>';
                                    }
                                    else {
                                        record +='<span style="font-size:16px;">'+x[1]+'</span>';
                                    }
                                    if(x[3]){
                                        record +='<br/><span style="font-size:14px;">'+x[3]+'</span>';
                                    }
                                    record +='</div><div class="img_house_info">\
                                    <img class="img img-fluid" src="/web/image/product.product/'+x[0]+'/xaa_aa_wq_image"/>\
                                    </div><div class="text-left">'
                                    if (x[4]){
                                        record += '<b><span style="font-size:12px;">'+x[4]+'</span></b><br/>';
                                    }
                                    if (x[5]){
                                        record += '<b><span style="font-size:12px;">'+x[5]+'</span></b><br/>';
                                    }
                                    if (x[6]){
                                        record += '<b><span style="font-size:12px;">'+x[6]+'</span></b><br/>';
                                    }
                                    if (x[7]){
                                        record += '<b><span style="font-size:12px;">'+x[7]+'</span></b><br/>';
                                    }
                                    record += '</div></div>'
                                    solar_product.append($(record));
                                });
                                if (selected){
                                    $('.solar_product_li').click();
                                }
                            }
                    })
                });
            });
            $(this).on('click', ".solar_product_li", function (e) {
                $('.solar_product_qty_show')[0].style="display:block";
                var solar_options = $('.solar_product_li');
                _.each(solar_options, function(solar){
                    $(solar).removeClass('selected');
                    $(solar).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                ajax.jsonRpc("/formulier/quote_infos", 'call', {
                    'product_id': parseInt(current.getAttribute('data-id'))
                }).then(function(data) {
                    $("input[name='xaa_aa_solar_watt_piek']").attr2('value', data.energy_wat_piek);
                    if (data.select_product.length) {
                        // $('.panel_price').show();
                        $('input[name="xaa_aa_panel_price"]')[0].value = data.select_product[0][2]
                    }
                    var watt = $("input[name='xaa_aa_solar_watt_piek']").val();
                    var loc_cal = $("input[name='xaa_aa_location_calculation']").val();
                    if (watt && loc_cal) {
                        var sQty = loc_cal / watt;
                        if (!isNaN(sQty) && isFinite(sQty)) {
                            $(".solar_qty")[0].value = parseInt(sQty) + 1;
                        }
                        else {
                            $(".solar_qty")[0].value = 1;
                        }
                    }
                    else {
                        $(".solar_qty")[0].value = 1;
                    }
                    var calculation = $(".solar_qty")[0].value * data.energy_wat_piek;
                    var energy_wat_piek = $("input[name='xaa_aa_energy_wat_piek']");
                    energy_wat_piek.attr2('value', calculation);
                    energy_wat_piek.change();
                    installation_time();
                });
            });
            function update_from_solar_qty() {
                var dialog = new Dialog(self, {
                title: _t("This will clear some calculated fields below"),
                buttons: [{text: _t("Reset"), classes: 'btn-primary', close: true, click: function () {
                        $("select[name='xaa_aa_need_converter']").val("");
                        $("select[name='xaa_aa_need_optimiser']").val("");
                        $("select[name='xaa_aa_pf_select_roof']").val("");
                        // $("select[name='xaa_aa_need_discount_2']").val("");
                        $("input[name='xaa_aa_converter_price']").val("");
                        $(".converter_product_li.selected").removeClass('selected');
                        $(".optimiser_product_li.selected").removeClass('selected');
                        $(".discount_product_li.selected").removeClass('selected');
                        $(".flat_product_li.selected").removeClass('selected');
                        $(".slanted_product_li.selected").removeClass('selected');
                    }}, {text: _t("Cancel"), close: true}],
                }).open();
            }
            $(".update_solar_qty").on('keyup click',function(e) {
                if (e.currentTarget.className.match('add_solar_qty')){
                    update_from_solar_qty();
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('solar_qty');
                    old_val[0].value = parseInt(old_val[0].value) + 1;
                    var calculation = old_val[0].value * $("input[name='xaa_aa_solar_watt_piek']").val();
                    var energy_wat_piek = $("input[name='xaa_aa_energy_wat_piek']")
                    energy_wat_piek.attr2('value', calculation);
                    energy_wat_piek.change();
                    if ($(".o_qty").length){
                        $(".o_qty").text(old_val[0].value);
                    }
                }
                else if(e.currentTarget.className.match('remove_solar_qty')){
                    update_from_solar_qty();
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('solar_qty');
                    if (parseInt(old_val[0].value) > 0){
                        old_val[0].value = parseInt(old_val[0].value) - 1;
                        var calculation = old_val[0].value * $("input[name='xaa_aa_solar_watt_piek']").val();
                        var energy_wat_piek = $("input[name='xaa_aa_energy_wat_piek']")
                        energy_wat_piek.attr2('value', calculation);
                        energy_wat_piek.change();
                        if ($(".o_qty").length) {
                            $(".o_qty").text(old_val[0].value);
                        }
                    }
                }
                else if(e.currentTarget.className.match('solar_qty')){
                    var solar_qty = $('.solar_qty')[0].value;
                    var calculation = solar_qty * $("input[name='xaa_aa_solar_watt_piek']").val();
                    var energy_wat_piek = $("input[name='xaa_aa_energy_wat_piek']")
                    energy_wat_piek.attr2('value', calculation);
                    energy_wat_piek.change();
                    if ($(".o_qty").length) {
                        $(".o_qty").text(solar_qty);
                    }
                }
                installation_time();
            });
            $(".update_solar_qty").on('change',function(e) {
                update_from_solar_qty();
            });
            $(this).on('change', "input[name='xaa_aa_energy_wat_piek']", function (e) {
                clickwatch(function() {
                    if ($("input[name='xaa_aa_energy_wat_piek']").val()) {
                        ajax.jsonRpc("/formulier/quote_infos", 'call', {'energy': parseFloat($("input[name='xaa_aa_energy_wat_piek']").val())}).then(
                            function(data) {
                            // $('.converter_price').hide();
                            $('.converter_product_qty_show').hide();
                            var converter_product = $('.converter_product_section').html('');
                            if (data.converter_product_ids.length) {
                                var selected = '';
                                if (data.converter_product_ids.length == 1){
                                    var selected = 'selected ';
                                }
                                _.each(data.converter_product_ids, function(x) {
                                    var record = '<div class="'+selected+'col-lg-6 col-md-6 col-sm-6 col-xs-12 padding_14_10 converter_product_li product_li text-center mt8" data-id="'+x[0]+'">\
                                    <div class="text-center mt4">'
                                    if(x[2]){
                                        record +='<span style="font-size:16px;">'+x[2]+'</span>';
                                    }
                                    else {
                                        record +='<span style="font-size:16px;">'+x[1]+'</span>';
                                    }
                                    if(x[3]){
                                        record +='<br/><span style="font-size:14px;">'+x[3]+'</span>';
                                    }
                                    record +='</div><div class="img_house_info">\
                                    <img class="img img-fluid" src="/web/image/product.product/'+x[0]+'/xaa_aa_wq_image"/>\
                                    </div><div class="text-left">'
                                    if (x[4]){
                                        record += '<b><span style="font-size:12px;">'+x[4]+'</span></b><br/>';
                                    }
                                    if (x[5]){
                                        record += '<b><span style="font-size:12px;">'+x[5]+'</span></b><br/>';
                                    }
                                    if (x[6]){
                                        record += '<b><span style="font-size:12px;">'+x[6]+'</span></b><br/>';
                                    }
                                    if (x[7]){
                                        record += '<b><span style="font-size:12px;">'+x[7]+'</span></b><br/>';
                                    }
                                    record += '</div></div>';
                                    converter_product.append($(record));
                                });
                                $("select[name='xaa_aa_need_converter']").click();
                                if (selected){
                                    $('.converter_product_li').click();
                                }
                            }
                        });
                    }
                });
            });
            $(this).on('change click', "select[name='xaa_aa_need_converter']", function () {
                if ($("select[name='xaa_aa_need_converter']").val() == 'ja'){
                    $(".converter_field")[0].style = 'display: block;';
                    if ($('.converter_product_li').length == 1){
                        $('.converter_product_qty_show').show();
                        $('.converter_product_li').addClass('selected');
                    }
                }
                else {
                    $(".converter_field").hide();
                    // $(".converter_price").hide();
                    $('.converter_product_qty_show').hide();
                }
            });
            $(this).on('change click', "select[name='xaa_aa_pv_need_custm_extra_product']", function () {
                var extra_pro = $("select[name='xaa_aa_pv_need_custm_extra_product']").val();
                if (extra_pro == 'ja 2' || extra_pro == 'ja 3'){
                    $(".pv_extra_product_description_two")[0].style = 'display: flex;';
                    $(".pv_extra_product_cost_two")[0].style = 'display: flex;';
                    $(".pv_extra_product_sale_two")[0].style = 'display: flex;';
                    $(".pv_extra_product_description_three").hide();
                    $(".pv_extra_product_cost_three").hide();
                    $(".pv_extra_product_sale_three").hide();
                }
                if (extra_pro == 'ja 3'){
                    $(".pv_extra_product_description_three")[0].style = 'display: flex;';
                    $(".pv_extra_product_cost_three")[0].style = 'display: flex;';
                    $(".pv_extra_product_sale_three")[0].style = 'display: flex;';
                }
                if (extra_pro == 'ja 1' || extra_pro == 'ja 2' || extra_pro == 'ja 3'){
                    $(".pv_extra_product_description")[0].style = 'display: flex;';
                    $(".pv_extra_product_cost")[0].style = 'display: flex;';
                    $(".pv_extra_product_sale")[0].style = 'display: flex;';
                }
                else {
                    $(".pv_extra_product_description").hide();
                    $(".pv_extra_product_cost").hide();
                    $(".pv_extra_product_sale").hide();
                    $(".pv_extra_product_description_two").hide();
                    $(".pv_extra_product_cost_two").hide();
                    $(".pv_extra_product_sale_two").hide();
                    $(".pv_extra_product_description_three").hide();
                    $(".pv_extra_product_cost_three").hide();
                    $(".pv_extra_product_sale_three").hide();
                }
            });
            $(this).on('click', ".converter_product_li", function (e) {
                $('.converter_product_qty_show').show();
                var converter_options = $('.converter_product_li');
                _.each(converter_options, function(converter){
                    $(converter).removeClass('selected');
                    $(converter).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                ajax.jsonRpc("/formulier/quote_infos", 'call', {
                    'product_id': parseInt(current.getAttribute('data-id'))
                }).then(function(data) {
                    if (data.select_product.length) {
                        // $('.converter_price').show();
                        $('input[name="xaa_aa_converter_price"]')[0].value = data.select_product[0][2]
                    }
                    var optimiser_product = $('.optimiser_product_section').html('');
                    // $('.optimisers_price').hide();
                    $('.optimiser_product_qty_show').hide();
                    if (data.optimiser_products.length) {
                        var selected = '';
                        if (data.optimiser_products.length == 1){
                            var selected = 'selected ';
                        }
                        _.each(data.optimiser_products, function(x) {
                            var record = '<div class="'+selected+'col-lg-6 col-md-6 col-sm-6 col-xs-12 padding_14_10 optimiser_product_li product_li text-center mt8" data-id="'+x[0]+'">\
                            <div class="text-center mt4">'
                            if(x[2]){
                                record +='<span style="font-size:16px;">'+x[2]+'</span>';
                            }
                            else {
                                record +='<span style="font-size:16px;">'+x[1]+'</span>';
                            }
                            if(x[3]){
                                record +='<br/><span style="font-size:14px;">'+x[3]+'</span>';
                            }
                            record +='</div><div class="img_house_info">\
                            <img class="img img-fluid" src="/web/image/product.product/'+x[0]+'/xaa_aa_wq_image"/>\
                            </div><div class="text-left">'
                            if (x[4]){
                                record += '<b><span style="font-size:12px;">'+x[4]+'</span></b><br/>';
                            }
                            if (x[5]){
                                record += '<b><span style="font-size:12px;">'+x[5]+'</span></b><br/>';
                            }
                            if (x[6]){
                                record += '<b><span style="font-size:12px;">'+x[6]+'</span></b><br/>';
                            }
                            if (x[7]){
                                record += '<b><span style="font-size:12px;">'+x[7]+'</span></b><br/>';
                            }
                            record += '</div></div>'
                            optimiser_product.append($(record));
                        });
                        if (selected){
                            $('.optimiser_product_li').click();
                        }
                    }
                });
            });
            $(".update_converter_qty").on('click',function(e) {
                if (e.currentTarget.className.match('add_converter_qty')){
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('converter_qty');
                    old_val[0].innerText = parseInt(old_val[0].innerText) + 1;
                }
                else{
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('converter_qty');
                    if (parseInt(old_val[0].innerText) > 0){
                        old_val[0].innerText = parseInt(old_val[0].innerText) - 1;
                    }
                }
            });
            $(this).on('change click', "select[name='xaa_aa_need_optimiser']", function () {
                console.log($("select[name='xaa_aa_need_optimiser']").val());

                if ($("select[name='xaa_aa_need_optimiser']").val() == 'ja'){
                    $(".optimiser_field")[0].style = 'display: block;';
                    if ($('.optimiser_product_li').length == 1){
                        $('.optimiser_product_qty_show').show();
                        $('.optimiser_product_li').addClass('selected');
                    }
                }
                else {
                    $(".optimiser_field").hide();
                    // $(".optimisers_price").hide();
                    $('.optimiser_product_qty_show').hide();
                }
            });
            $(this).on('click', ".optimiser_product_li", function (e) {
                $('.optimiser_product_qty_show').show();
                var optimiser_options = $('.optimiser_product_li');
                _.each(optimiser_options, function(optimiser){
                    $(optimiser).removeClass('selected');
                    $(optimiser).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                ajax.jsonRpc("/formulier/quote_infos", 'call', {
                    'product_id': parseInt(current.getAttribute('data-id'))
                }).then(function(data) {
                    if (data.select_product.length) {
                        // $('.optimisers_price').show();
                        $('input[name="xaa_aa_optimisers_price"]')[0].value = data.select_product[0][2];
                        $(".o_qty").text(parseInt($(".solar_qty")[0].value));
                    }
                });
            });
            $(".update_optimiser_qty").on('click',function(e) {
                if (e.currentTarget.className.match('add_optimiser_qty')){
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('optimiser_qty');
                    old_val[0].innerText = parseInt(old_val[0].innerText) + 1;
                }
                else{
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('optimiser_qty');
                    if (parseInt(old_val[0].innerText) > 0){
                        old_val[0].innerText = parseInt(old_val[0].innerText) - 1;
                    }
                }
            });
            $(this).on('change click', "select[name='xaa_aa_pf_select_roof']", function (e) {
                clickwatch(function() {
                    $('.flat_product').hide();
                    $('.slanted_product').hide();
                    $('.flat_product_qty_show').hide();
                    $('.slanted_product_qty_show').hide();
                    if ($("select[name='xaa_aa_pf_select_roof']").val()) {
                        ajax.jsonRpc("/formulier/quote_infos", 'call', {'roof': $("select[name='xaa_aa_pf_select_roof']").val()}).then(
                            function(data) {
                                if (data.flat_product_ids.length) {
                                    $('.flat_product')[0].style = 'display: block;';
                                    if (data.flat_product_ids.length == 1){
                                        $('.flat_product_li').click();
                                    }
                                }
                                if (data.slanted_product_ids.length) {
                                    $(".slanted_product")[0].style = 'display: block;';
                                    if (data.slanted_product_ids.length == 1){
                                        $('.slanted_product_li').click();
                                    }
                                }
                            });
                    }
                }, 500);
            });

            // call on page load
            $("select[name='xaa_aa_pf_select_roof']").change();

            $(this).on('change', "input[name='xaa_aa_location_correction']", function (e) {
                clickwatch(function() {
                    if (e.currentTarget.value != parseInt(e.currentTarget.value)){
                        e.currentTarget.value = 0 ;
                        alert('Please enter valid number');
                    }
                    var loc_cor = $("input[name='xaa_aa_location_correction']").val();
                    if (loc_cor && $("input[name='xaa_aa_energy_use']").val()) {
                        var loc_calculation = $("input[name='xaa_aa_energy_use']").val() / (loc_cor/100);
                        $("input[name='xaa_aa_location_calculation']").attr2('value', parseInt(loc_calculation));
                    }
                    var watt = $("input[name='xaa_aa_solar_watt_piek']").val();
                    var loc_cal = $("input[name='xaa_aa_location_calculation']").val();
                    if (watt && loc_cal) {
                        var sQty = loc_cal / watt;
                        if (!isNaN(sQty)) {
                            $(".solar_qty")[0].value = parseInt(sQty) + 1;
                        }
                        else {
                            $(".solar_qty")[0].value = sQty;
                        }
                    }
                    else {
                        $(".solar_qty")[0].value = 1;
                    }
                    var calculation = parseInt($(".solar_qty")[0].value) * $("input[name='xaa_aa_solar_watt_piek']").val();
                    var energy_wat_piek = $("input[name='xaa_aa_energy_wat_piek']");
                    energy_wat_piek.attr2('value', calculation);
                    energy_wat_piek.change()
                    if ($(".o_qty").length) {
                        $(".o_qty").text(parseInt($(".solar_qty")[0].value));
                    }
                }, 500);
            });
            $(this).on('click', ".flat_product_li", function (e) {
                $('.flat_product_qty_show').show();
                var flat_options = $('.flat_product_li');
                _.each(flat_options, function(flat){
                    $(flat).removeClass('selected');
                    $(flat).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                var opt_qty = $('.solar_qty');
                var roof_qty = $(".flat_roof_qty");
                if (opt_qty.length && roof_qty.length){
                    roof_qty[0].innerText = parseInt(opt_qty[0].value)
                }
            });
            $(this).on('click', ".slanted_product_li", function (e) {
                $('.slanted_product_qty_show').show();
                var slanted_options = $('.slanted_product_li');
                _.each(slanted_options, function(slanted){
                    $(slanted).removeClass('selected');
                    $(slanted).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                var opt_qty = $('.solar_qty');
                var roof_qty = $(".slanted_roof_qty");
                if (opt_qty.length && roof_qty.length){
                    roof_qty[0].innerText = parseInt(opt_qty[0].value)
                }
            });
            $(".update_roof_qty").on('click',function(e) {
                if (e.currentTarget.className.match('add_roof_qty')){
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('roof_qty');
                    old_val[0].innerText = parseInt(old_val[0].innerText) + 1;
                }
                else{
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('roof_qty');
                    if (parseInt(old_val[0].innerText) > 0){
                        old_val[0].innerText = parseInt(old_val[0].innerText) - 1;
                    }
                }
            });
            $(this).on('change click', "select[name='xaa_aa_need_discount']", function () {
                if ($("select[name='xaa_aa_need_discount']").val() == 'ja'){
                    $(".discount_field").show();
                    $(".discount_qty")[0].style = 'display: flex;';
                    if ($('.discount_product_li').length == 1){
                        $('.discount_product_li').addClass('selected');
                    }
                }
                else {
                    $(".discount_field").hide();
                    $(".discount_qty").hide();
                }
            });
            $(this).on('click', ".discount_product_li", function (e) {
                var discount_options = $('.discount_product_li');
                _.each(discount_options, function(discount){
                    $(discount).removeClass('selected');
                    $(discount).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
            });
            // $(this).on('change click', "select[name='xaa_aa_need_discount_2']", function () {
            //     if ($("select[name='xaa_aa_need_discount_2']").val() == 'ja'){
            //         $(".amount_range")[0].style='display: flex;';
            //     }
            //     else {
            //         $(".amount_range").hide();
            //     }
            // });
            // $(this).on('change', "input[name='xaa_aa_amount_range']", function (e) {
            //     clickwatch(function() {
            //         if (e.currentTarget.value != parseInt(e.currentTarget.value)){
            //             e.currentTarget.value = 0 ;
            //             alert('Please enter valid number');
            //         }
            //     });
            // });
            $(this).on('click', ".o_website_create_quote, .o_website_eval_quote", function (e) {
                var formulier_id = parseInt($('input[name="formulier_id"]').val());
                var vals = {
                        "xaa_aa_solar_product": parseInt($(".solar_product_li.selected").attr('data-id')) || false,
                        "xaa_aa_converter_product": parseInt($(".converter_product_li.selected").attr('data-id')) || false,
                        "xaa_aa_optimiser_product": parseInt($(".optimiser_product_li.selected").attr('data-id')) || false,
                        "xaa_aa_flat_roof_product": parseInt($(".flat_product_li.selected").attr('data-id')) || false,
                        "xaa_aa_slanted_roof_product": parseInt($(".slanted_product_li.selected").attr('data-id')) || false,
                        // "xaa_aa_discount_product": parseInt($(".discount_product_li.selected").attr('data-id')) || false,
                }
                ajax.jsonRpc("/formulier/update_formulier", 'call', {
                                'quoteData': vals,
                                'formulier_id': formulier_id,
                }).then(function(data) {});
                var allData = {
                    'xaa_aa_solar_product': parseInt($(".solar_product_li.selected").attr('data-id')) || false,
                    'solar_qty': parseInt($('.solar_qty')[0].value),
                    'xaa_aa_location_correction': parseInt($('input[name="xaa_aa_location_correction"]').val()),
                    'xaa_aa_need_converter': $("select[name='xaa_aa_need_converter']").val(),
                    'xaa_aa_converter_product': parseInt($(".converter_product_li.selected").attr('data-id')) || false,
                    'converter_qty': parseInt($('.converter_qty').text()),
                    'xaa_aa_converter_price': parseInt($('input[name="xaa_aa_converter_price"]').val()),
                    'xaa_aa_panel_price': parseInt($('input[name="xaa_aa_panel_price"]').val()),
                    'xaa_aa_optimisers_price' : parseInt($('input[name="xaa_aa_optimisers_price"]').val()),
                    'optimiser_qty': parseInt($('.optimiser_qty').text()),
                    'xaa_aa_need_optimiser': $("select[name='xaa_aa_need_optimiser']").val(),
                    'xaa_aa_optimiser_product': parseInt($(".optimiser_product_li.selected").attr('data-id')) || false,
                    'xaa_aa_pf_select_roof': $("select[name='xaa_aa_pf_select_roof']").val(),
                    'xaa_aa_flat_roof_product': parseInt($(".flat_product_li.selected").attr('data-id')) || false,
                    'flat_roof_qty': parseInt($('.flat_roof_qty').text()),
                    'xaa_aa_slanted_roof_product': parseInt($(".slanted_product_li.selected").attr('data-id')) || false,
                    'slanted_roof_qty': parseInt($('.slanted_roof_qty').text()),
                    'xaa_aa_installation_time': $("select[name='xaa_aa_installation_time']").val(),
                    'xaa_aa_need_discount': $("select[name='xaa_aa_need_discount']").val(),
                    // 'xaa_aa_discount_product': parseInt($(".discount_product_li.selected").attr('data-id')) || false,
                    'xaa_aa_discount_qty': parseInt($("input[name='xaa_aa_discount_qty']").val()),
                    // 'xaa_aa_need_discount_2': $("select[name='xaa_aa_need_discount_2']").val(),
                    'xaa_aa_need_schouw': $("select[name='xaa_aa_need_schouw']").val(),
                    'xaa_aa_pv_need_custm_extra_product': $("select[name='xaa_aa_pv_need_custm_extra_product']").val(),
                    'xaa_aa_pv_extra_product_description': $("input[name='xaa_aa_pv_extra_product_description']").val(),
                    'xaa_aa_pv_extra_product_cost': parseInt($("input[name='xaa_aa_pv_extra_product_cost']").val()),
                    'xaa_aa_pv_extra_product_sale': parseInt($("input[name='xaa_aa_pv_extra_product_sale']").val()),
                    'xaa_aa_pv_extra_product_description_two': $("input[name='xaa_aa_pv_extra_product_description_two']").val(),
                    'xaa_aa_pv_extra_product_cost_two': parseInt($("input[name='xaa_aa_pv_extra_product_cost_two']").val()),
                    'xaa_aa_pv_extra_product_sale_two': parseInt($("input[name='xaa_aa_pv_extra_product_sale_two']").val()),
                    'xaa_aa_pv_extra_product_description_three': $("input[name='xaa_aa_pv_extra_product_description_three']").val(),
                    'xaa_aa_pv_extra_product_cost_three': parseInt($("input[name='xaa_aa_pv_extra_product_cost_three']").val()),
                    'xaa_aa_pv_extra_product_sale_three': parseInt($("input[name='xaa_aa_pv_extra_product_sale_three']").val()),
                    // 'xaa_aa_amount_range': $("input[name='xaa_aa_amount_range']").val(),
                    'xaa_aa_quote_template_id': parseInt($("select[name='xaa_aa_quote_template_id']").val()),
                }
                if (e.target.className.search('o_website_eval_quote') != -1){
                    $('#loading').show();
                    ajax.jsonRpc("/formulier/pv/quote_create", 'call', {
                                    'quoteData': allData,
                                    'formulier_id': formulier_id,
                                    'eval_quote':true,
                        }).then(
                            function(data) {
                                $('#loading').hide();
                                var quote_button = $('#quote_create');
                                if (data.length > 2){
                                    quote_button.before('<div class="form-group row form-field col-lg-9 col-lg-offset-2"><div class="col-lg-6"><strong>Score:</strong><span> '+String(data[0])+'</span></div><div class="col-lg-6"><strong>Totaal excl btw:</strong><span> '+String(data[1])+'</span></div><div class="col-lg-6 mt4"><strong>Totaal Commissie:</strong><span> '+String(data[2])+'</span></div></div>')
                                }
                                if (data.length < 3){
                                    quote_button.before('<div class="form-group row form-field col-lg-9 col-lg-offset-2"><div class="col-lg-6"><strong>Totaal excl btw:</strong><span> '+String(data[0])+'</span></div><div class="col-lg-6 mt4"><strong>Totaal Commissie:</strong><span> '+String(data[1])+'</span></div></div>')
                                }
                            }
                        );
                }
                else{
                    $('.custom_progress').click();
                    ajax.jsonRpc("/formulier/pv/quote_create", 'call', {
                                'quoteData': allData,
                                'formulier_id': formulier_id,
                                'eval_quote':false,
                    }).then(
                        function(data) {
                            window.open(data.url, '_blank');
                            $('.o_website_form_send').click();
                            $('.percentage_div').hide();
                        }
                    );
                }
            });
            $('.reset_value').on("click",function(e){
                var formulier_id = parseInt($('input[name="formulier_id"]').val())
                $('#loading').show();
                var vals = {
                            "xaa_aa_energy_use" : 0,
                            "xaa_aa_location_correction" : 0,
                            "xaa_aa_location_calculation": 0,
                            "xaa_aa_solar_type": [[6, false, []]],
                            "xaa_aa_solar_product":false,
                            "xaa_aa_solar_watt_piek": false,
                            "xaa_aa_energy_wat_piek": 0,
                            "xaa_aa_need_converter": false,
                            "xaa_aa_converter_product": false,
                            "xaa_aa_pf_select_roof": false,
                            "xaa_aa_need_optimiser": false,
                            "xaa_aa_optimiser_product": false,
                            "xaa_aa_flat_roof_product": false,
                            "xaa_aa_slanted_roof_product": false,
                            "xaa_aa_installation_time": false,
                            "xaa_aa_need_discount": false,
                            // "xaa_aa_need_discount_2": false,
                            "xaa_aa_need_schouw": false,
                            // "xaa_aa_amount_range": 0,
                            // "xaa_aa_discount_product": false,
                            "xaa_aa_discount_qty": 0,
                            "xaa_aa_converter_price": 0,
                            "xaa_aa_panel_price": 0,
                            "xaa_aa_optimisers_price": 0,
                            "xaa_aa_pv_cost_price_total": 0,
                            "xaa_aa_pv_need_custm_extra_product": false,
                            "xaa_aa_pv_extra_product_description": '',
                            "xaa_aa_pv_extra_product_cost": 0,
                            "xaa_aa_pv_extra_product_sale": 0,
                            "xaa_aa_pv_extra_product_description_two": '',
                            "xaa_aa_pv_extra_product_cost_two": 0,
                            "xaa_aa_pv_extra_product_sale_two": 0,
                            "xaa_aa_pv_extra_product_description_three": '',
                            "xaa_aa_pv_extra_product_cost_three": 0,
                            "xaa_aa_pv_extra_product_sale_three": 0,
                }
                ajax.jsonRpc("/formulier/update_formulier", 'call', {
                                'quoteData': vals,
                                'formulier_id': formulier_id,
                }).then(function(data) {
                    $('#loading').hide();
                    location.reload();
                });
            });
        }
        $("select[name='xaa_aa_is_earthing_total_length']").on('click', function(e){
            if (e.currentTarget.value == 'ja'){
                $('.is_earthing_total_length')[0].style = 'display: flex;';
            }
            else{
                $('.is_earthing_total_length')[0].style = 'display:none;';
            }
        });
        $("select[name='xaa_aa_is_utp_total_length']").on('click', function(e){
            if (e.currentTarget.value == 'ja'){
                $('.is_utp_total_length')[0].style = 'display: flex;';
            }
            else{
                $('.is_utp_total_length')[0].style = 'display:none;';
            }
        });
    });

});
