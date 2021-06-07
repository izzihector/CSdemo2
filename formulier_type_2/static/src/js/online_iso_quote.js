odoo.define('formulier_type_2.online_iso_quote', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $( document ).ready(function() {
        var clickwatch = (function(){
              var timer = 0;
              return function(callback, ms){
                clearTimeout(timer);
                timer = setTimeout(callback, ms);
              };
        })();

        if ($("#nav_tabs_iso_form").length) {
            $(this).on('change', "select[name='xaa_aa_kind_of_isolate']", function (e) {
                clickwatch(function() {
                    if ($('select[name="xaa_aa_kind_of_isolate"]').val() == 'Cavity'){
                        $('.ventilation_section').show();
                        $("select[name='xaa_aa_need_ventilation_grid']").click();
                        var quote_template = $('select[name="xaa_aa_quote_template_id"]')[0];
                        _.forEach(quote_template.options, function(op){
                            if (op.text == 'Spouwmuurisolatie'){
                                quote_template.selectedIndex = op.index;
                            }
                        })
                    }
                    else{
                        $('.ventilation_section').hide();
                        $('.ventilation_product').hide();
                    }
                    if ($('select[name="xaa_aa_kind_of_isolate"]').val() == 'Floor'){
                        $('.spacing').show();
                        $('.iso_type').show();
                        $('.xaa_aa_iso_installation_time').show();
                        $("select[name='xaa_aa_spacing']").change();
                        $('.tickness_of_wall').hide();
                        $('.need_cavity_boundary').hide();
                        $('.cavity_boundary_product').hide();
                        $('.extra_support').hide();
                        $('.need_extra_product').hide();
                        $('.need_custm_extra_product').hide();
                        $('.extra_product_description').hide();
                        $('.extra_product_cost').hide();
                        $('.extra_product_sale').hide();
                        $('.extra_product_description_two').hide();
                        $('.extra_product_cost_two').hide();
                        $('.extra_product_sale_two').hide();
                        $('.extra_product_description_three').hide();
                        $('.extra_product_cost_three').hide();
                        $('.extra_product_sale_three').hide();
                    }
                    else{
                        $("select[name='xaa_aa_tickness_of_wall']").change();
                        $('.need_extra_product').show();
                        $('.xaa_aa_iso_installation_time').hide();
                        $("select[name='xaa_aa_need_custm_extra_product']").click();
                        $('.extra_support').show();
                        $('.need_cavity_boundary').show();
                        $("select[name='xaa_aa_need_cavity_boundary']").click();
                        $('.tickness_of_wall').show();
                        $('.iso_type').hide();
                        $('.spacing').hide();
                    }
                    // $(".material_price").hide();
                    // $(".service_price").hide();
                    var isolation_options = $('.isolation_product_li');
                    _.each(isolation_options, function(isolation){
                        $(isolation).removeClass('selected');
                        $(isolation).show();
                    })
                    if ($('select[name="xaa_aa_kind_of_isolate"]').val()){
                        $('.isolation_product').show();
                        $('.isolation_qty').show();
                    }
                    else{
                        $('.isolation_product').hide();
                        $('.isolation_qty').hide();
                    }
                });
            });
            $(this).on('change', "input[name='xaa_aa_m2_count']", function (e) {
                clickwatch(function() {
                    if (e.currentTarget.value != parseInt(e.currentTarget.value)){
                        e.currentTarget.value = 0 ;
                        alert('Please enter valid number');
                    }
                }, 500);
            });
            $(this).on('change click', "select[name='xaa_aa_tickness_of_wall']", function (e) {
                clickwatch(function() {
                    if($("select[name='xaa_aa_tickness_of_wall']").val()){
                        ajax.jsonRpc("/formulier/iso_quote_infos", 'call', {'cavity_thickness': parseInt($("select[name='xaa_aa_tickness_of_wall']").val())}).then(
                            function(data) {
                                // $('.material_price').hide();
                                // $('.service_price').hide();
                                var isolationProduct = $('.isolation_product_section').html('');
                                if (data.isolation_product.length) {
                                    var selected = '';
                                    if (data.isolation_product.length == 1){
                                        var selected = 'selected ';
                                    }
                                    _.each(data.isolation_product, function(x) {
                                        var record = '<div class="'+selected+'col-lg-6 col-md-6 col-sm-6 col-xs-12 padding_14_10 isolation_product_li product_li text-center mt8" data-id="'+x[0]+'">\
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
                                        isolationProduct.append($(record));
                                    });
                                    if (selected){
                                        $('.isolation_product_li').click();
                                    }
                                }
                        })
                    }
                    else{
                        $('.isolation_product_section').html('');
                    }
                });
            });
            $(this).on('change click', "select[name='xaa_aa_spacing']", function (e) {
                clickwatch(function() {
                    if($("select[name='xaa_aa_spacing']").val()){
                        ajax.jsonRpc("/formulier/iso_quote_infos", 'call', {'spacing': $("select[name='xaa_aa_spacing']").val()}).then(
                            function(data) {
                                // $('.material_price').hide();
                                // $('.service_price').hide();
                                var isolationProduct = $('.isolation_product_section').html('');
                                if (data.isolation_product.length) {
                                    var selected = '';
                                    if (data.isolation_product.length == 1){
                                        var selected = 'selected ';
                                    }
                                    _.each(data.isolation_product, function(x) {
                                        var record = '<div class="'+selected+'col-lg-6 col-md-6 col-sm-6 col-xs-12 padding_14_10 isolation_product_li product_li text-center mt8" data-id="'+x[0]+'">\
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
                                        isolationProduct.append($(record));
                                    });
                                    if (selected){
                                        $('.isolation_product_li').click();
                                    }
                                }
                        })
                    }
                    else {
                        $('.isolation_product_section').html('');
                    }
                });
            });
            $(this).on('click', ".isolation_product_li", function (e) {
                var isolation_options = $('.isolation_product_li');
                _.each(isolation_options, function(isolation){
                    $(isolation).removeClass('selected');
                    $(isolation).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                ajax.jsonRpc("/formulier/iso_quote_infos", 'call', {
                    'product_id': parseInt($(".isolation_product_li.selected").attr('data-id')),
                }).then(function(data) {
                    if (data.selected_product.length) {
                        // $(".material_price").show();
                        // $(".service_price").show();
                        $("input[name='xaa_aa_material_price']")[0].value = data.selected_product[0][2];
                        // $("#service_price")[0].value = data.selected_product[0][2];
                    }
                });
            });
            $(this).on('change click', "select[name='xaa_aa_need_ventilation_grid']", function () {
                if ($("select[name='xaa_aa_need_ventilation_grid']").val() == 'ja'){
                    $(".ventilation_product").show();
                }
                else {
                    $(".ventilation_product").hide();
                    $('.ventilation_product_qty_show').hide();
                }
            });
            $(this).on('click', ".ventilation_product_li", function (e) {
                $('.ventilation_product_qty_show').show();
                var ventilation_options = $('.ventilation_product_li');
                _.each(ventilation_options, function(ventilation){
                    $(ventilation).removeClass('selected');
                    $(ventilation).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
                // ajax.jsonRpc("/formulier/iso_quote_infos", 'call', {
                //     'product_id': parseInt(current.getAttribute('data-id'))
                // }).then(function(data) {
                //     if (data.selected_product.length) {
                //         $(".ventilation_price").show();
                //         $("input[name='xaa_aa_ventilation_price']")[0].value = data.selected_product[0][2];
                //     }
                // });
            });
            $(".update_ventilation_qty").on('click',function(e) {
                if (e.currentTarget.className.match('add_ventilation_qty')){
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('ventilation_qty');
                    old_val[0].innerText = parseInt(old_val[0].innerText) + 1;
                }
                else{
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('ventilation_qty');
                    if (parseInt(old_val[0].innerText) > 0){
                        old_val[0].innerText = parseInt(old_val[0].innerText) - 1;
                    }
                }
            });
            $(this).on('change click', "select[name='xaa_aa_need_cavity_boundary']", function () {
                if ($("select[name='xaa_aa_need_cavity_boundary']").val() == 'ja'){
                    $(".cavity_boundary_product").show();
                }
                else {
                    $(".cavity_boundary_product").hide();
                    $(".cavity_boundary_product_qty_show").hide();
                }
            });
            $(this).on('click', ".cavity_boundary_product_li", function (e) {
                $('.cavity_boundary_product_qty_show').show();
                var cavity_boundary_options = $('.cavity_boundary_product_li');
                _.each(cavity_boundary_options, function(cavity_boundary){
                    $(cavity_boundary).removeClass('selected');
                    $(cavity_boundary).hide();
                })
                var current = e.currentTarget;
                $(current).addClass('selected');
                $(current).show();
            });
            $(".update_cavity_boundary_qty").on('click',function(e) {
                if (e.currentTarget.className.match('add_cavity_boundary_qty')){
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('cavity_boundary_qty');
                    old_val[0].innerText = parseInt(old_val[0].innerText) + 1;
                }
                else{
                    var parent_ele = e.currentTarget.parentElement.parentElement;
                    var old_val = parent_ele.getElementsByClassName('cavity_boundary_qty');
                    if (parseInt(old_val[0].innerText) > 0){
                        old_val[0].innerText = parseInt(old_val[0].innerText) - 1;
                    }
                }
            });
            $(this).on('change click', "select[name='xaa_aa_need_custm_extra_product']", function () {
                var extra_pro = $("select[name='xaa_aa_need_custm_extra_product']").val();
                if (extra_pro == 'ja 2' || extra_pro == 'ja 3'){
                    $(".extra_product_description_two").show();
                    $(".extra_product_cost_two").show();
                    $(".extra_product_sale_two").show();
                    $(".extra_product_description_three").hide();
                    $(".extra_product_cost_three").hide();
                    $(".extra_product_sale_three").hide();
                }
                if (extra_pro == 'ja 3'){
                    $(".extra_product_description_three").show();
                    $(".extra_product_cost_three").show();
                    $(".extra_product_sale_three").show();
                }
                if (extra_pro == 'ja 1' || extra_pro == 'ja 2' || extra_pro == 'ja 3'){
                    $(".extra_product_description").show();
                    $(".extra_product_cost").show();
                    $(".extra_product_sale").show();
                }
                else {
                    $(".extra_product_description").hide();
                    $(".extra_product_cost").hide();
                    $(".extra_product_sale").hide();
                    $(".extra_product_description_two").hide();
                    $(".extra_product_cost_two").hide();
                    $(".extra_product_sale_two").hide();
                    $(".extra_product_description_three").hide();
                    $(".extra_product_cost_three").hide();
                    $(".extra_product_sale_three").hide();
                }
            });
            $(this).on('change click', "select[name='xaa_aa_need_discount']", function () {
                if ($("select[name='xaa_aa_need_discount']").val() == 'ja'){
                    $(".discount_qty").show();
                }
                else {
                    $(".discount_qty").hide();
                }
            });
            $('.reset_value_iso').on("click",function(e){
                var formulier_id = parseInt($('input[name="formulier_id"]').val())
                $('#loading').show();
                var vals = {
                            "xaa_aa_kind_of_isolate": false,
                            "xaa_aa_m2_count": 0,
                            "xaa_aa_iso_type": false,
                            "xaa_aa_isolation_product": false,
                            "xaa_aa_tickness_of_wall": false,
                            "xaa_aa_spacing": false,
                            "xaa_aa_need_ventilation_grid": false,
                            "xaa_aa_ventilation_product": false,
                            "xaa_aa_need_cavity_boundary": false,
                            "xaa_aa_cavity_boundary_product": false,
                            "xaa_aa_extra_support": false,
                            "xaa_aa_need_custm_extra_product": false,
                            "xaa_aa_extra_product_description": '',
                            "xaa_aa_extra_product_cost": 0,
                            "xaa_aa_extra_product_sale": 0,
                            "xaa_aa_extra_product_description_two": '',
                            "xaa_aa_extra_product_cost_two": 0,
                            "xaa_aa_extra_product_sale_two": 0,
                            "xaa_aa_extra_product_description_three": '',
                            "xaa_aa_extra_product_cost_three": 0,
                            "xaa_aa_extra_product_sale_three": 0,
                            "xaa_aa_need_discount": false,
                            "xaa_aa_discount_qty": 0,
                            "xaa_aa_quote_template_id": false,
                            "xaa_aa_service_price": 0,
                            "xaa_aa_iso_installation_time":false,
                }
                ajax.jsonRpc("/formulier/update_formulier", 'call', {
                                'quoteData': vals,
                                'formulier_id': formulier_id,
                }).then(function(data) {
                    $('#loading').hide();
                    location.reload();
                });
            });
            $(this).on('click', ".o_website_create_iso_quote, .o_website_eval_iso_quote", function (e) {
                var allData = {
                    'xaa_aa_kind_of_isolate': $("select[name='xaa_aa_kind_of_isolate']").val(),
                    'xaa_aa_isolation_product': parseInt($(".isolation_product_li.selected").attr('data-id')) || false,
                    'isolation_qty': parseInt($("input[name='xaa_aa_m2_count']").val()),
                    'xaa_aa_material_price': parseInt($("input[name='xaa_aa_material_price']").val()),
                    'xaa_aa_service_price': parseInt($("input[name='xaa_aa_service_price']").val()),
                    'xaa_aa_need_ventilation_grid': $("select[name='xaa_aa_need_ventilation_grid']").val(),
                    'xaa_aa_ventilation_product': parseInt($(".ventilation_product_li.selected").attr('data-id')) || false,
                    'ventilation_qty': parseInt($('.ventilation_qty').text()),
                    'xaa_aa_ventilation_price' : parseInt($("input[name='xaa_aa_ventilation_price']").val()),
                    'xaa_aa_need_cavity_boundary': $("select[name='xaa_aa_need_cavity_boundary']").val(),
                    'xaa_aa_cavity_boundary_product': parseInt($(".cavity_boundary_product_li.selected").attr('data-id')) || false,
                    'cavity_boundary_qty': parseInt($('.cavity_boundary_qty').text()),
                    'xaa_aa_need_custm_extra_product': $("select[name='xaa_aa_need_custm_extra_product']").val(),
                    'xaa_aa_extra_product_description': $("input[name='xaa_aa_extra_product_description']").val(),
                    'xaa_aa_extra_product_cost': parseInt($("input[name='xaa_aa_extra_product_cost']").val()),
                    'xaa_aa_extra_product_sale': parseInt($("input[name='xaa_aa_extra_product_sale']").val()),
                    'xaa_aa_extra_product_description_two': $("input[name='xaa_aa_extra_product_description_two']").val(),
                    'xaa_aa_extra_product_cost_two': parseInt($("input[name='xaa_aa_extra_product_cost_two']").val()),
                    'xaa_aa_extra_product_sale_two': parseInt($("input[name='xaa_aa_extra_product_sale_two']").val()),
                    'xaa_aa_extra_product_description_three': $("input[name='xaa_aa_extra_product_description_three']").val(),
                    'xaa_aa_extra_product_cost_three': parseInt($("input[name='xaa_aa_extra_product_cost_three']").val()),
                    'xaa_aa_extra_product_sale_three': parseInt($("input[name='xaa_aa_extra_product_sale_three']").val()),
                    'xaa_aa_need_schouw': $("select[name='xaa_aa_need_schouw']").val(),
                    'xaa_aa_need_discount': $("select[name='xaa_aa_need_discount']").val(),
                    'xaa_aa_discount_qty': parseInt($("input[name='xaa_aa_discount_qty']").val()),
                    'xaa_aa_quote_template_id': parseInt($("select[name='xaa_aa_quote_template_id']").val()),
                    'xaa_aa_iso_installation_time': $("select[name='xaa_aa_iso_installation_time']").val(),
                }
                // $('.custom_progress').click();
                var formulier_id = parseInt($('input[name="formulier_id"]').val())
                var vals = {
                        'xaa_aa_isolation_product': parseInt($(".isolation_product_li.selected").attr('data-id')) || false,
                        'xaa_aa_ventilation_product': parseInt($(".ventilation_product_li.selected").attr('data-id')) || false,
                        'xaa_aa_cavity_boundary_product': parseInt($(".cavity_boundary_product_li.selected").attr('data-id')) || false,
                }
                ajax.jsonRpc("/formulier/update_formulier", 'call', {
                                'quoteData': vals,
                                'formulier_id': formulier_id,
                }).then(function(data) {});
                if (e.target.className.search('o_website_eval_iso_quote') != -1){
                    $('#loading').show();
                    ajax.jsonRpc("/formulier/iso/quote_create", 'call', {
                                    'quoteData': allData,
                                    'formulier_id': formulier_id,
                                    'eval_quote':true,
                        }).then(
                            function(data) {
                                // $('.percentage_div').hide();
                                $('#loading').hide();
                                var quote_button = $('#iso_quote_create');
                                if (data.length > 2){
                                    quote_button.before('<div class="row"><div class="col-lg-5"><strong>Score:</strong><span> '+String(data[0])+'</span></div><div class="col-lg-6"><strong>Totaal excl btw:</strong><span> '+String(data[1])+'</span></div><div class="col-lg-6 mt4"><strong>Totaal Commissie:</strong><span> '+String(data[2])+'</span></div></div>')
                                }
                                if (data.length < 3){
                                    quote_button.before('<div class="row"><div class="col-lg-6"><strong>Totaal excl btw:</strong><span> '+String(data[0])+'</span></div><div class="col-lg-6 mt4"><strong>Totaal Commissie:</strong><span> '+String(data[1])+'</span></div></div>')
                                }
                            }
                        );
                }
                else{
                    $('.custom_progress').click();
                    ajax.jsonRpc("/formulier/iso/quote_create", 'call', {
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
        }
    });

});
