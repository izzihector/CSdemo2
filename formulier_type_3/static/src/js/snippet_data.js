function formulier_type_three(){
    var curr_page = $(document);
    url = curr_page.attr('location').pathname
    if (url.indexOf('/my/orders/') == 0){
        sale_id = url.split('/')[3];
        $.ajax({
            url: "/order/snippet/pv_dynamic_value",
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'sale_id': parseInt(sale_id)} }),
            async: false,
            success: function (result) {
                if(result.result.formulier_id){
                    var que_id = result.result.formulier_id;
                    var record = result.result;
                    if($('#quotation_snippet_structure').find($('#photo_roof_1_img_id')) && record.xaa_aa_photo_roof_1 != false){
                        $('#photo_roof_1_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_photo_roof_1';
                    }
                    if($('#quotation_snippet_structure').find($('#photo_roof_2_img_id')) && record.xaa_aa_photo_roof_2 != false){
                        $('#photo_roof_2_img_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_photo_roof_2';
                    }
                    if($('#quotation_snippet_structure').find($('#Inverter_in_operation_id')) && record.xaa_aa_inverter_in_operation != false){
                        $('#Inverter_in_operation_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_inverter_in_operation';
                    }
                    if($('#quotation_snippet_structure').find($('#cupboard_opened_id')) && record.xaa_aa_cupboard_opened != false){
                        $('#cupboard_opened_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_cupboard_opened';
                    }
                    if($('#quotation_snippet_structure').find($('#inverter_serial_number_id')) && record.xaa_aa_inverter_serial_number != false){
                        $('#inverter_serial_number_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_inverter_serial_number';
                    }
                    if($('#quotation_snippet_structure').find($('#optimizers_serial_number_id')) && record.xaa_aa_optimizers_serial_number != false){
                        $('#optimizers_serial_number_id')[0].src='/web/image/question.formulier/'+ que_id +'/xaa_aa_optimizers_serial_number';
                    }
                }
            },
        });
    }
}
