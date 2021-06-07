function get_caculation_data(){
    var curr_page = $(document);
    url = curr_page.attr('location').pathname
    if (url.indexOf('/my/orders/') == 0){
        sale_id = url.split('/')[3];
        $.ajax({
            url: "/order/getCalculations",
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'sale_id': parseInt(sale_id)} }),
            async: false,
            success: function (result) {
                var record = result.result;
                if (record) {
                    if($('#quotation_snippet_structure').find($('#id_1'))){
                        $('#id_1').replaceWith('<td id="id_1" style="width:20%">'+ record.xaa_aa_watt_piek +'</td>');
                    }
                    if($('#quotation_snippet_structure').find($('#id_2'))){
                        $('#id_2').replaceWith('<td id="id_2" style="width:20%">'+ record.currency +
                            ' '+ record.xaa_aa_jaaropbrengst_prijs_van +'</td>');
                    }
                    if($('#quotation_snippet_structure').find($('#id_3'))){
                        $('#id_3').replaceWith('<td id="id_3" style="width:20%">'+ parseInt(
                            record.xaa_aa_jaaropbrengsten) +'</td>');
                    }
                    if($('#quotation_snippet_structure').find($('#id_4'))){
                        $('#id_4').replaceWith('<td id="id_4" style="width:20%">'+ record.xaa_aa_rendement +'%</td>');
                    }
                    if($('#quotation_snippet_structure').find($('#id_5'))){
                        $('#id_5').replaceWith('<td id="id_5" style="width:20%">'+
                            record.xaa_aa_verwachte_terugverdientijd +'</td>');
                    }
                    if($('#quotation_snippet_structure').find($('#id_6'))){
                        $('#id_6').replaceWith('<td id="id_6" style="width:20%">'+ (
                            record.xaa_aa_totale_verwachte_jaaropbrengst_van_de.toFixed(2)
                            ).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","
                            ).replace(/[.]/, ",").replace(/[,]/, ".") +'</td>');
                    }
                    if($('#quotation_snippet_structure').find($('#id_7'))){
                        $('#id_7').replaceWith('<td id="id_7" style="width:20%">'+ record.currency +
                            ' '+ record.xaa_aa_related_amount_untaxed.toString().replace(
                            /\B(?=(\d{3})+(?!\d))/g, ",").replace(/[.]/, ",").replace(
                            /[,]/, ".") +'</td>');
                    }
                }
            },
        });
    }
}