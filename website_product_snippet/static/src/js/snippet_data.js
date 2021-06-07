function product_snippet(){
    var curr_page = $(document);
    url = curr_page.attr('location').pathname;
    if (url.indexOf('/shop/') == 0){
        var product_name = url.split('/')[2];
        var product = product_name.split('-');
        var product_id = product[product.length - 1];
        $.ajax({
            url: "/product/snippet/dynamic_value",
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'product_id': parseInt(product_id)} }),
            async: false,
            success: function (result) {
                var record = result.result;
                // if($('#aa_wb_logo').length && record.aa_wb_logo != false){
                //     $('#aa_wb_logo')[0].src='/web/image/product.template/'+ record.product_id +'/aa_wb_logo';
                // }
                // if($('#aa_wb_product_image').length && record.aa_wb_product_image != false){
                //     $('#aa_wb_product_image')[0].src='/web/image/product.template/'+ record.product_id +'/aa_wb_product_image';
                // }
                // if($('#aa_wb_title').length && record.aa_wb_title != false){
                //     $('#aa_wb_title').replaceWith('<h3>'+ record.aa_wb_title +'</h3>');
                // }
                // if($('#aa_wb_text').length && record.aa_wb_text != false){
                //     $('#aa_wb_text').replaceWith('<p>'+ record.aa_wb_text +'</p>');
                // }
                if($('#aa_sp_logo').length && record.aa_sp_logo != false){
                    $('#aa_sp_logo')[0].src='/web/image/product.template/'+ record.product_id +'/aa_sp_logo';
                }
                if($('#aa_sp_product_image').length && record.aa_sp_product_image != false){
                    $('#aa_sp_product_image')[0].src='/web/image/product.template/'+ record.product_id +'/aa_sp_product_image';
                }
                if($('#aa_sp_name').length && record.aa_sp_name != false){
                    $('#aa_sp_name').replaceWith('<p style="font-size: 20px;"><b>'+ record.aa_sp_name +'</b></p>');
                }
                if($('#aa_point1_icon').length && record.aa_point1_icon != false){
                    $('#aa_point1_icon')[0].src='/web/image/product.template/'+ record.product_id +'/aa_point1_icon';
                }
                if($('#aa_point1_title').length && record.aa_point1_title != false){
                    $('#aa_point1_title').replaceWith('<p style="margin: auto; font-size: 16px;"><b>'+ record.aa_point1_title +'</b></p>');
                }
                if($('#aa_point1_desc').length && record.aa_point1_desc != false){
                    $('#aa_point1_desc').replaceWith('<p style="font-size: 14px;">'+ record.aa_point1_desc +'</p>');
                }
                if($('#aa_point2_icon').length && record.aa_point2_icon != false){
                    $('#aa_point2_icon')[0].src='/web/image/product.template/'+ record.product_id +'/aa_point2_icon';
                }
                if($('#aa_point2_title').length && record.aa_point2_title != false){
                    $('#aa_point2_title').replaceWith('<p style="margin: auto; font-size: 16px;"><b>'+ record.aa_point2_title +'</b></p>');
                }
                if($('#aa_point2_desc').length && record.aa_point2_desc != false){
                    $('#aa_point2_desc').replaceWith('<p style="font-size: 14px;">'+ record.aa_point2_desc +'</p>');
                }
                if($('#aa_point3_icon').length && record.aa_point3_icon != false){
                    $('#aa_point3_icon')[0].src='/web/image/product.template/'+ record.product_id +'/aa_point3_icon';
                }
                if($('#aa_point3_title').length && record.aa_point3_title != false){
                    $('#aa_point3_title').replaceWith('<p style="margin: auto; font-size: 16px;"><b>'+ record.aa_point3_title +'</b></p>');
                }
                if($('#aa_point3_desc').length && record.aa_point3_desc != false){
                    $('#aa_point3_desc').replaceWith('<p style="font-size: 14px;">'+ record.aa_point3_desc +'</p>');
                }
                if($('#aa_point4_icon').length && record.aa_point4_icon != false){
                    $('#aa_point4_icon')[0].src='/web/image/product.template/'+ record.product_id +'/aa_point4_icon';
                }
                if($('#aa_point4_title').length && record.aa_point4_title != false){
                    $('#aa_point4_title').replaceWith('<p style="margin: auto; font-size: 16px;"><b>'+ record.aa_point4_title +'</b></p>');
                }
                if($('#aa_point4_desc').length && record.aa_point4_desc != false){
                    $('#aa_point4_desc').replaceWith('<p style="font-size: 14px;">'+ record.aa_point4_desc +'</p>');
                }
                if($('#aa_point5_icon').length && record.aa_point5_icon != false){
                    $('#aa_point5_icon')[0].src='/web/image/product.template/'+ record.product_id +'/aa_point5_icon';
                }
                if($('#aa_point5_title').length && record.aa_point5_title != false){
                    $('#aa_point5_title').replaceWith('<p style="margin: auto; font-size: 16px;"><b>'+ record.aa_point5_title +'</b></p>');
                }
                if($('#aa_point5_desc').length && record.aa_point5_desc != false){
                    $('#aa_point5_desc').replaceWith('<p style="font-size: 14px;">'+ record.aa_point5_desc +'</p>');
                }
                if(!record.aa_point4_icon && !record.aa_point4_title && !record.aa_point4_desc){
                    $('#aa_point4_icon').remove();
                    $('#aa_point4_title').remove();
                    $('#aa_point4_desc').remove();
                }
                if(!record.aa_point5_icon && !record.aa_point5_title && !record.aa_point5_desc){
                    $('#aa_point5_icon').remove();
                    $('#aa_point5_title').remove();
                    $('#aa_point5_desc').remove();
                }
            }
        });
    }
}
