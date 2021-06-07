odoo.define('formulier_type_2.customer_quote_formulier', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    $( document ).ready(function() {
        $('input[name="xaa_aa_quote_construction_year"]').on('click',function(e){
            if (e.currentTarget.value == 'tussen 1935 en 1975'){
                $('.house_insulated')[0].style='display: block;';
            }
            else{
                $('.house_insulated')[0].style='display: none;';
            }
            if (e.currentTarget.value == 'voor 1935'){
                $('.construction_year_next')[0].style='display: none;';
                $('.construction_year_next_text')[0].style='display: flex;';
            }
            else{
                $('.construction_year_next')[0].style='display: block;';
                $('.construction_year_next_text')[0].style='display: none;';
            }
        })
        $('input[name="xaa_aa_quote_house_insulated"]').on('click',function(e){
            if (e.currentTarget.value == 'Energie Foam wit isolatieschuim'){
                $('.construction_year_1975')[0].style='display: flex;';
            }
            else{
                $('.construction_year_1975')[0].style='display: none;';
            }
        })

        $('.house_info_li').on('click', function(e){
            var house_options = $('.house_info_li');
            _.each(house_options, function(house){
                $(house).removeClass('selected');
            })
            $(e.currentTarget).addClass('selected');
        });

        $("#extension_tab").on("click",function(e){
            var formulier_id = parseInt($(".btn_iso_quote").val());
            var allData = {
                "xaa_aa_quote_construction_year": false,
                "xaa_aa_quote_house_insulated" : false,
                "xaa_aa_quote_cavity_thickness_home" : false,
                "xaa_aa_quote_type_of_house_id" : parseInt($(".house_info_li.selected").attr('data-id')) || false,
                "xaa_aa_quote_type_of_house_name" : $(".house_info_li.selected").attr('data-name') || '',
                "xaa_aa_quote_need_insulated" : false,
                "xaa_aa_quote_many_extension" : parseInt($("input[name='xaa_aa_quote_many_extension']").val()) || 0,
                "xaa_aa_qupte_do_crawl_space": false,
                "xaa_aa_quote_ventilation_qty": 0,
                "xaa_aa_quote_cavity_qty": 0,
            }
            var quote_construction_year = $("input[name='xaa_aa_quote_construction_year']");
            var quote_house_insulated = $("input[name='xaa_aa_quote_house_insulated']");
            var quote_cavity_thickness_home = $("input[name='xaa_aa_quote_cavity_thickness_home']");
            var quote_need_insulated = $("input[name='xaa_aa_quote_need_insulated']");
            var qupte_do_crawl_space = $("input[name='xaa_aa_qupte_do_crawl_space']");
            _.forEach(qupte_do_crawl_space,function(re){
                if (re.checked){
                    allData['xaa_aa_qupte_do_crawl_space'] = re.value;
                }
            });
            _.forEach(quote_construction_year,function(re){
                if (re.checked){
                    allData['xaa_aa_quote_construction_year'] = re.value;
                }
            });
            _.forEach(quote_house_insulated,function(re){
                if (re.checked){
                    allData['xaa_aa_quote_house_insulated'] = re.value;
                }
            });
            _.forEach(quote_cavity_thickness_home,function(re){
                if (re.checked){
                    allData['xaa_aa_quote_cavity_thickness_home'] = re.value;
                }
            });
            _.forEach(quote_need_insulated,function(re){
                if (re.checked){
                    allData['xaa_aa_quote_need_insulated'] = re.value;
                }
            });
            if (allData['xaa_aa_quote_type_of_house_name'] && allData['xaa_aa_quote_need_insulated'] == 'ja'){
                if(allData['xaa_aa_quote_type_of_house_name'] == 'vrijstaand'){
                    allData['xaa_aa_quote_many_extension'] = 135;
                    allData['xaa_aa_quote_ventilation_qty'] = 6;
                    allData['xaa_aa_quote_cavity_qty'] = 0;
                }
                else if(allData['xaa_aa_quote_type_of_house_name'] == 'twee-onder-een-kap'){
                    allData['xaa_aa_quote_many_extension'] = 100;
                    allData['xaa_aa_quote_ventilation_qty'] = 6;
                    allData['xaa_aa_quote_cavity_qty'] = 12;
                }
                else if(allData['xaa_aa_quote_type_of_house_name'] == 'tussenwoning'){
                    allData['xaa_aa_quote_many_extension'] = 50;
                    allData['xaa_aa_quote_ventilation_qty'] = 4;
                    allData['xaa_aa_quote_cavity_qty'] = 20;
                }
            }
            if (allData['xaa_aa_quote_type_of_house_name'] && allData['xaa_aa_quote_need_insulated'] == 'nee'){
                if(allData['xaa_aa_quote_type_of_house_name'] == 'vrijstaand'){
                    allData['xaa_aa_quote_many_extension'] = 125;
                    allData['xaa_aa_quote_ventilation_qty'] = 6;
                    allData['xaa_aa_quote_cavity_qty'] = 0;
                }
                else if(allData['xaa_aa_quote_type_of_house_name'] == 'twee-onder-een-kap'){
                    allData['xaa_aa_quote_many_extension'] = 90;
                    allData['xaa_aa_quote_ventilation_qty'] = 6;
                    allData['xaa_aa_quote_cavity_qty'] = 12;
                }
                else if(allData['xaa_aa_quote_type_of_house_name'] == 'tussenwoning'){
                    allData['xaa_aa_quote_many_extension'] = 40;
                    allData['xaa_aa_quote_ventilation_qty'] = 4;
                    allData['xaa_aa_quote_cavity_qty'] = 20;
                }
            }
            $("input[name='xaa_aa_quote_many_extension']")[0].value = allData['xaa_aa_quote_many_extension'];

            // Save PF
            $('#loading').show();
            ajax.jsonRpc("/customer/iso/quote/submit", 'call', {
                        'quoteData': allData,
                        'formulier_id': formulier_id,
            }).then(function(data) {
                $('#loading').hide();
            });

            $(".btn_iso_quote").on("click",function(e){
                allData["xaa_aa_quote_many_extension"] = parseInt($("input[name='xaa_aa_quote_many_extension']").val()) || 0,
                $('#loading').show();
                ajax.jsonRpc("/customer/iso/quote/create", 'call', {
                            'quoteData': allData,
                            'formulier_id': formulier_id,
                }).then(function(data) {
                    $('#loading').hide();
                    window.open(data.url, '_self');
                });
            });
        });
    });
});
