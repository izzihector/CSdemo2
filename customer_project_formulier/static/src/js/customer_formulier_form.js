odoo.define('customer_project_formulier.customer_formulier_form', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function() {
        $(".formulier_type").on('click',function(e){
            if (e.currentTarget.className.includes('active')){
                $(e.currentTarget).removeClass('active');
            }
            else{
                $(e.currentTarget).addClass('active');
            }
        })
        $(".telephone_change").on('click',function(e){
            $("select[name='title']").attr("disabled",false);
            $("input[name='first_name']").attr("readonly",false);
            $("input[name='last_name']").attr("readonly",false);
            $("input[name='phone']").attr("readonly",false);
            $("#current_customer_edit").hide();
            $("#telephone_button").hide();
            $("#address_button").hide();
            $("#next_customer_edit").show();
        })
        $(".address_change").on('click',function(e){
            $("input[name='street_number2']").attr("readonly",false);
            $("input[name='street_number']").attr("readonly",false);
            $("input[name='zip']").attr("readonly",false);
            $("#current_customer_edit").hide();
            $("#telephone_button").hide();
            $("#address_button").hide();
            $("#next_customer_edit").show();
        })
        $(".customer_data_save").on('click',function(e){
            var data = {
                'title': $("select[name='title']").val(),
                'filled_email': $("input[name='filled_email']").val(),
                'first_name': $("input[name='first_name']").val(),
                'last_name': $("input[name='last_name']").val(),
                'phone': $("input[name='phone']").val(),
                'zip': $("input[name='zip']").val(),
                'street_number': $("input[name='street_number']").val(),
                'street_name': $("input[name='street_name']").val(),
                'city': $("input[name='city']").val(),
                'street_number2': $("input[name='street_number2']").val(),
            }
            ajax.jsonRpc("/update_contact_data", 'call', {
                        'data': data,
            }).then(function(data) {
                console.log('data........................');
            })
        });
        $("#back_customer_form_tab").on('click',function(e){
            var title = $("select[name='title']");
            var filled_email = $("input[name='filled_email']");
            var first_name = $("input[name='first_name']");
            var last_name = $("input[name='last_name']");
            var phone = $("input[name='phone']");
            var zip = $("input[name='zip']");
            var street_number = $("input[name='street_number']");
            var street_name = $("input[name='street_name']");
            var city = $("input[name='city']");
            var street_number2 = $("input[name='street_number2']");

            title.attr("disabled",true);
            first_name.attr("readonly",true);
            last_name.attr("readonly",true);
            phone.attr("readonly",true);
            street_number2.attr("readonly",true);
            street_number.attr("readonly",true);
            zip.attr("readonly",true);
            $("#current_customer_edit").show();
            $("#next_customer_edit").hide();
            $("#telephone_button").show();
            $("#address_button").show();
        })
        $(".get_address").on('click',function(e){
            var postcode = $("input[name='zip']").val();
            var house_number = $("input[name='street_number']").val();
            var street_name = $("input[name='street_name']");
            var city = $("input[name='city']");
            if (house_number.length && postcode.length){
                street_name.show();
                city.show();
                ajax.jsonRpc("/get_address", 'call', {
                            'house_number': house_number,
                            'postcode': postcode,
                }).then(function(data) {
                    if (data.street_name && data.city){
                        street_name[0].value = data.street_name || '';
                        city[0].value = data.city || '';
                        $("#postcode_warning").hide();
                        street_name.attr("readonly",true);
                        city.attr("readonly",true);
                    }
                    else{
                        street_name[0].value = '';
                        city[0].value = '';
                        $("#postcode_warning").show();
                        street_name.attr("readonly",false);
                        city.attr("readonly",false);
                    }
                })
            }
            else{
                street_name.hide();
                city.hide();
                street_name[0].value = '';
                city[0].value = '';
            }
        });
        $("input[name='street_number2']").on('keydown',function(e){
            var valid_keys = [8, 9, 17, 37, 39, 46, 16]
            if (valid_keys.includes(e.keyCode)){
                return true;
            }
            var numExpr = /^[0-9]+$/;
            if (!(e.originalEvent.key.match(numExpr))){
                return false;
            }
        });
        $("input[name='phone']").on('click',function(e){
            $(".phone_alert").show();
        });
        $("input[name='phone']").on('change',function(e){
            $(".phone_alert").hide();
        });
        $("input[name='phone']").on('keydown',function(e){
            if (e.keyCode == 32) {
                return false;
            }
            var valid_keys = [8, 9, 17, 37, 39, 46, 16]
            if (valid_keys.includes(e.keyCode)){
                return true;
            }
            var phoneno = /^[\+\d]+(?:[\d-.\s()]*)$/mg;
            if ((e.originalEvent.key.match(phoneno) && e.currentTarget.value.length < 12)){
                if (!(e.target.value.length) && !(e.originalEvent.key.startsWith('+'))){
                    return false;
                }
                return true;
            }
            else{
                return false
            }
        });
        $("input[name='zip']").on('keydown',function(e){
            if (e.keyCode == 32) {
                return false;
            }
            var valid_keys = [8, 9, 17, 37, 39, 46, 16]
            if (valid_keys.includes(e.keyCode)){
                return true;
            }
            var charExpr = /^[a-zA-Z]+$/;
            var numExpr = /^[0-9]+$/;
            if ((e.currentTarget.value.length < 6)){
                if (!(e.target.value.length) && !(e.originalEvent.key.match(numExpr))){
                    return false;
                }
                if (e.target.value.length && e.target.value.length < 4 && 
                    !(e.originalEvent.key.match(numExpr))){
                    return false;
                }
                if (e.target.value.length && e.target.value.length > 3 && 
                    !(e.originalEvent.key.match(charExpr))){
                    return false;
                }
                return true;
            }
            else{
                return false
            }
            
        });
        function filled_product_info(data) {
            var formulier_type = $('.formulier_type');
            var type_option = $('.type_option');
            var type_install = $('.type_install');
            _.each(formulier_type, function(f_type_in){
                if (f_type_in.className.includes('active')){
                    $(f_type_in).removeClass('active');
                }
            })
            if (data.formulier_type){
                _.each(data.formulier_type, function(f_type){
                    _.each(formulier_type, function(f_type_in){
                        if (parseInt(f_type_in.getAttribute('data-id')) == f_type){
                            $(f_type_in).addClass('active');
                        }
                    })
                })
            }

            _.each(type_option, function(t_option){
                    t_option.checked = false;
            })
            if (data.type_option){
                _.each(data.type_option, function(value,name){
                    _.each(type_option, function(t_option){
                        if (parseInt(t_option.value) == value && t_option.name == name){
                            t_option.checked = true;
                        }
                    })
                })
            }

            _.each(type_install, function(t_install){
                t_install.checked = false;
            })
            if (data.type_install){
                _.each(data.type_install, function(value,name){
                    _.each(type_install, function(t_install){
                        if (value.includes(parseInt(t_install.value)) && t_install.name == name){
                            t_install.checked = true;
                        }
                    })
                })
            }
        }
        function search_customer(flag) {
            var email = $("input[name='email_input']")
            var mailformat = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if (email.val().match(mailformat)){
                ajax.jsonRpc("/search_customer", 'call', {
                            'email': email.val(),
                }).then(function(data) {
                    filled_product_info(data);
                    $("#email_show").hide();
                    var title = $("select[name='title']");
                    var filled_email = $("input[name='filled_email']");
                    var first_name = $("input[name='first_name']");
                    var last_name = $("input[name='last_name']");
                    var phone = $("input[name='phone']");
                    var zip = $("input[name='zip']");
                    var street_number = $("input[name='street_number']");
                    var street_name = $("input[name='street_name']");
                    var city = $("input[name='city']");
                    var street_number2 = $("input[name='street_number2']");
                    filled_email[0].value = email.val();
                    _.each(title[0].options, function(op) {
                        if (op.getAttribute('value') == data.title){
                            title[0].selectedIndex = op.index;
                        }
                    });
                    if (data.name){
                        first_name[0].value = data.first_name || '';
                        last_name[0].value = data.last_name || '';
                        phone[0].value = data.phone || '';
                        zip[0].value = data.zip || '';
                        street_number[0].value = data.street_number || '';
                        street_name[0].value = data.street_name || '';
                        city[0].value = data.city || '';
                        $("#found_data").show();
                        $("#telephone_button").show();
                        $("#address_button").show();

                        title.attr("disabled",true);
                        first_name.attr("readonly",true);
                        last_name.attr("readonly",true);
                        phone.attr("readonly",true);
                        zip.attr("readonly",true);
                        street_number.attr("readonly",true);
                        street_name.attr("readonly",true);
                        city.attr("readonly",true);
                        street_number2.attr("readonly",true);
                    }
                    else{
                        first_name[0].value = '';
                        last_name[0].value = '';
                        phone[0].value = '';
                        zip[0].value = '';
                        street_number[0].value = '';
                        street_name[0].value = '';
                        city[0].value = '';
                        $("#found_data").hide();
                        $("#telephone_button").hide();
                        $("#address_button").hide();

                        title.attr("disabled",false);
                        first_name.attr("readonly",false);
                        last_name.attr("readonly",false);
                        phone.attr("readonly",false);
                        zip.attr("readonly",false);
                        street_number.attr("readonly",false);
                        street_name.attr("readonly",false);
                        city.attr("readonly",false);
                        street_number2.attr("readonly",false);
                    }
                    flag = 1
                });
            }
            else{
                $("#email_show").show();
                flag = 0
            }
            return flag
        }

        $(".btn-lead-create").on('click',function(e){
            var data = {
                'filled_email': $("input[name='filled_email']").val()
            }
            ajax.jsonRpc("/create_new_lead", 'call', {
                        'data': data,
            }).then(function(data) {
                window.open(data.url, '_self');
            })
        });


        $(".btn-oppo-next").on('click',function(e){
            var flag = 1;
            var tab_id = $('#'+e.currentTarget.getAttribute('data-id'));
            var prev_tab = $(tab_id[0].previousElementSibling);
            if (prev_tab[0].id == 'email_tab'){
                var flag = search_customer(flag);
            }
            if (prev_tab[0].id == 'customer_form_tab'){
                $("input[required='1']").each(function() {
                    if ($(this).val() === '' ){
                        $(this)[0].style = $(this)[0].style.cssText+'border-color: red';
                        flag = 0;
                    }
                    else{
                        $(this)[0].style = $(this)[0].style.cssText+'border-color: none';
                    }
                  });
            }
            if (flag == 1){
                var next_tab = $('#'+e.currentTarget.getAttribute('data-id'))[0].firstElementChild.click();
                tab_id.addClass('active');
                if (prev_tab.hasClass("customer_tabs_li")){
                    prev_tab.addClass("filled");
                    prev_tab.removeClass("active");
                }
                $('body,html').animate({scrollTop: 0}, 200);
            }
        });
        $(".btn-oppo-privoius").on('click',function(e){
            $('#'+e.currentTarget.getAttribute('data-id')).find('a').trigger('click');
            var tab_id = $('#'+e.currentTarget.getAttribute('data-id'));
            var prev_tab = $(tab_id[0].nextElementSibling)
            prev_tab.removeClass("active");
            tab_id.addClass('active');
            if (tab_id.hasClass("filled")){
                tab_id.removeClass("filled");
            }
            $('body,html').animate({scrollTop: 0}, 200);
        });
    });

});

