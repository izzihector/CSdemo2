odoo.define('project_formulier_quote.formulier_quote_js', function (require) {
    "use strict";

    $( document ).ready(function() {

        $('#loading').hide();
        $('.custom_progress').on('click',function(e){
            $('.percentage_div').show();
            var elem = document.getElementById("progress_percentage");
            var width = 1;
            var id = setInterval(frame, parseInt(elem.getAttribute('data-id')));
            function frame() {
                if (width >= 95) {
                  clearInterval(id);
                } else {
                  width++;
                  elem.innerText = width + '%';
                  elem.style.width = width + '%';
                }
            }
        })

        $(".nav-link").on('click',function(e){
            if (e.currentTarget.id == 'nav_tabs_iso' || e.currentTarget.id == 'nav_tabs_solar'){
                if ($('.formulier_submit').length){
                    $('.formulier_submit').hide();
                }
            }
            else{
                if ($('.formulier_submit').length){
                    $('.formulier_submit').show();
                }
            }
        })

        $(".btn-next").on('click',function(e){
            var next_tab = $('#'+e.currentTarget.getAttribute('data-id'))[0].firstElementChild.click();
            var tab_id = $('#'+e.currentTarget.getAttribute('data-id'));
            tab_id.addClass('active');
            var prev_tab = $(tab_id[0].previousElementSibling)
            if (prev_tab.hasClass("inner_li") || prev_tab.hasClass("quote_tabs_li")){
                prev_tab.addClass("filled");
                prev_tab.removeClass("active");
            }
            $('body,html').animate({scrollTop: 0}, 200);
        });
        $(".btn-privoius").on('click',function(e){
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

        //for show tooltip
        $('[data-toggle="tooltip"]').tooltip();

        // solar product quantity update
        $('.add').click(function () {
            var th = $(this).closest('.snipper_Add_Minus').find('.count');
            th.val(+th.val() + 1);
        });
        $('.sub').click(function () {
            var th = $(this).closest('.snipper_Add_Minus').find('.count');
                if (th.val() > 1) th.val(+th.val() - 1);
        });
        const checkbox = document.getElementById('checkbox');
    });
});

