odoo.define('formulier_type_3.customer_quote_review', function (require) {
    "use strict";

    $( document ).ready(function() {
        $('input[name="xaa_aa_quote_type_of_roof"]').on('click',function(e){
            if (e.currentTarget.value == 'schuin'){
                $('.schuin_block')[0].style='display: block;';
                $('.plat_block')[0].style='display: none;';
            }
            else if (e.currentTarget.value == 'plat'){
                $('.schuin_block')[0].style='display: none;';
                $('.plat_block')[0].style='display: block;';
            }
            else if (e.currentTarget.value == 'beide'){
                $('.schuin_block')[0].style='display: block;';
                $('.plat_block')[0].style='display: block;';
            }
            else{
                $('.schuin_block')[0].style='display: none;';
                $('.plat_block')[0].style='display: none;';
            }
        })
        $('input[name="xaa_aa_quote_entrepreneur"]').on('click',function(e){
            if (e.currentTarget.value == 'Ik ben ondernemer maar mijn partner niet.'){
                $('.quote_entrepreneur_block')[0].style='display: flex;';
            }
            else{
                $('.quote_entrepreneur_block')[0].style='display: none;';
            }
        })
        $("input[name='xaa_aa_quote_final_approval']").on('click', function(e){
            if (e.currentTarget.value == 'Ik word graag gebeld om de offerte door te nemen van de spouwmuurisolatie en de woning wellicht binnen 5 werkdagen te hebben geisoleerd.'){
                $('.quote_final_approval_date')[0].style='display:block';
            }
            else if (e.currentTarget.value == 'Ik word graag gebeld voor meer informatie over de spouwmuurisolatie.'){
                $('.quote_final_approval_date')[0].style='display:block';
            }
            else{
                $('.quote_final_approval_date')[0].style='display:none';
            }
        })

        $("#quote_conclusion_photos_id").on('click',function(e){
            var date = $("input[name='xaa_aa_quote_final_approval_date']");
            if (date.data('value')){
                date[0].value = date.data('value').replace(' ', 'T');
            }
        })
    });
});
