odoo.define('customer_project_formulier.product_formulier_form', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function() {
        $('button[data-id="formulier_type_product_option_tab"]').on('click',function(e){
            var formulier_type = $('.formulier_type');
            var formulier_type_next = $('.formulier_type_next');
            var formulier_type_install = $('.formulier_type_install');
            _.each(formulier_type, function(f_type){
                // if (f_type.className.includes('active')){
                    _.each(formulier_type_next, function(f_type_next){
                        if (f_type.getAttribute('data-id') == f_type_next.getAttribute('data-id')){
                            var f_type_next = $(f_type_next);
                            if (f_type.className.includes('active')){
                                f_type_next.addClass('active');
                                if (f_type_next[0].nextElementSibling){
                                    f_type_next[0].nextElementSibling.style='display:block';
                                }
                            }
                            else{
                                f_type_next.removeClass('active');
                                if (f_type_next[0].nextElementSibling){
                                    f_type_next[0].nextElementSibling.style='display:none';
                                }
                            }
                        }
                    })
                    _.each(formulier_type_install, function(f_type_next){
                        if (f_type.getAttribute('data-id') == f_type_next.getAttribute('data-id')){
                            var f_type_next = $(f_type_next);
                            if (f_type.className.includes('active')){
                                f_type_next.addClass('active');
                                f_type_next[0].parentElement.style='display:block';
                                if (f_type_next[0].nextElementSibling){
                                    f_type_next[0].nextElementSibling.style='display:block';
                                }
                            }
                            else{
                                f_type_next.removeClass('active');
                                f_type_next[0].parentElement.style='display:none';
                                if (f_type_next[0].nextElementSibling){
                                    f_type_next[0].nextElementSibling.style='display:none';
                                }
                            }
                        }
                    })
                // }
            })
        })
        $('.customer_formulier_type_data').on('click',function(e){
            var formulier_type = [];
            var type_option = [];
            var filled_email = $("input[name='filled_email']").val();
            var data = {'filled_email': filled_email, 'type_option': {}, 'type_install': {}, 'formulier_type': []}

            var product_details = {};
            _.each($('.formulier_type'), function(f_type){
                if (f_type.className.includes('active')){
                    product_details[f_type.firstElementChild.innerText]='';
                }
            });
            _.each($('.formulier_type_next'), function(f_type){
                if (f_type.className.includes('active')){
                    data['formulier_type'].push(parseInt(f_type.getAttribute('data-id')));
                }
            });
            _.each($('.type_option'), function(f_type_option){
                if (f_type_option.checked){
                    data['type_option'][f_type_option.name] = parseInt(f_type_option.value);
                    product_details[f_type_option.name] = product_details[f_type_option.name] + f_type_option.nextElementSibling.textContent+', ';
                }
            });
            _.each($('.type_install'), function(f_type_install){
                if (f_type_install.checked){
                    product_details[f_type_install.name] = product_details[f_type_install.name] + f_type_install.nextElementSibling.textContent+', ';
                    if (data['type_install'].hasOwnProperty(f_type_install.name)){
                        data['type_install'][f_type_install.name].push(parseInt(f_type_install.value));
                    }
                    else{
                        data['type_install'][f_type_install.name] = [parseInt(f_type_install.value)];
                    }
                }
            });
            console.log('data........................',product_details);


            var filled_email = $(".filled_email");
            var title = $(".title");
            var first_name = $(".first_name");
            var last_name = $(".last_name");
            var phone = $(".phone");
            var zip = $(".zip");
            var street_number = $(".street_number");
            var street_number2 = $(".street_number2");
            var street_name = $(".street_name");
            var city = $(".city");
            var product_tag = $(".product_details");
            filled_email[0].textContent = $("input[name='filled_email']").val();
            title[0].textContent = $("select[name='title']").val();
            first_name[0].textContent = $("input[name='first_name']").val();
            last_name[0].textContent = $("input[name='last_name']").val();
            phone[0].textContent = $("input[name='phone']").val();
            zip[0].textContent = $("input[name='zip']").val();
            street_number[0].textContent = $("input[name='street_number']").val();
            street_number2[0].textContent = $("input[name='street_number2']").val();
            street_name[0].textContent = $("input[name='street_name']").val();
            city[0].textContent = $("input[name='city']").val();
            
            _.each(product_details,function(value,name){
                product_tag.append($('<div class="col-lg-5 col-md-5 col-sm-12 custom-text-right">'+name+':</div><div class="col-lg-7 col-md-7 col-sm-12">'+value+'</div>'));
            })





            ajax.jsonRpc("/update_contact_product_data", 'call', {
                        'data': data,
            }).then(function(data) {
                console.log('data........................');
            })
        })

    })
})