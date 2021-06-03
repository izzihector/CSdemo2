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

        $(".roof_select_page").on('click',function(e){
            var roof_type = $(".roof_type");
            var roof_table = $('.roof_table_value');
            _.each(roof_type, function(roof){
                if (roof.value){
                    $('#'+roof.name).show();
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
