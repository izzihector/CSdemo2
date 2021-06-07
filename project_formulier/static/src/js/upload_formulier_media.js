odoo.define('project_formulier.upload_formulier_media', function (require) {
'use strict';

    var rpc = require('web.rpc');

    $(document).ready(function () {

        // extra images add in order.image from /project-formulier/id/pf_access
        $("input[name='formulier_image_upload_input'],input[name='task_image_upload_input'] ").on('change',function(e) {
            var formulier_id = $("#formulier_id").val();
            if (e.currentTarget.id == 'task_image_upload_input'){
                var is_task = true;
                var append_block = $('#TaskDiv');
            }
            else{
                var is_task = false;
                var append_block = $('#myDiv');
            }
            var file_input = document.getElementById(e.currentTarget.id);
            var files = file_input.files;
            var r = new FileReader();
            r.onload = (function(theFile) {
                return function(e) {
                    var img = e.target.result.split(',')[1];
                    var file_type = theFile.type;
                    setTimeout(function() {
                        $.ajax({
                            url: "/formulier/form/image/upload",
                            type: 'POST',
                            dataType: 'json',
                            contentType: 'application/json',
                            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'image': img, 'fileName': theFile.name, 'file_type': file_type, 'formulier_id': formulier_id, 'is_task': is_task} }),
                            async: false,
                            success: function (result) {
                                append_block.append('<div class="col-lg-3 col-md-3 col-sm-3"><button type="button" class="close close_button pull-right" aria-label="close" id="'+result.result+'">×</button><img class="img img-fluid custom-image-size extra_image" src="/web/image/order.image/'+result.result+'/xaa_aa_image"/></div>');
                            },
                        });
                    }, 0);
                };
            })(files[0]);
            r.readAsDataURL(files[0]);
        });

        // video upload code
        $("input[name='formulier_video_upload_input'],input[name='task_video_upload_input']").on('change',function(e) {
            var formulier_id = $("#formulier_id").val();
            if (e.currentTarget.id == 'task_video_upload_input'){
                var is_task = true;
                var append_block = $('#TaskVideo');
            }
            else{
                var is_task = false;
                var append_block = $('#myVideo');
            }
            var file_input = document.getElementById(e.currentTarget.id);
            var files = file_input.files;
            var r = new FileReader();
            r.onload = (function(theFile) {
                return function(e) {
                    var video = e.target.result.split(',')[1];
                    var file_type = theFile.type;
                    setTimeout(function() {
                        $.ajax({
                            url: "/formulier/form/video/upload",
                            type: 'POST',
                            dataType: 'json',
                            contentType: 'application/json',
                            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'video': video,'fileName': theFile.name, 'file_type': file_type, 'formulier_id': formulier_id, 'is_task': is_task }}),
                            async: false,
                            success: function (result) {
                                append_block.append('<div class="col-lg-4 col-md-4 col-sm-4 mb4 mt4 no-padding"><video class="col-lg-12 col-md-12 col-sm-12" src="/web/video/'+result.result+'" controls=""/></div>');
                            },
                        });
                    }, 0);
                };
            })(files[0]);
            r.readAsDataURL(files[0]);
        });

        // extra Documents add in order.document from /project-formulier/id/pf_access
        $("input[name='formulier_document_upload_input'],input[name='task_document_upload_input']").on('change',function(e) {
            var formulier_id = $("#formulier_id").val();
            if (e.currentTarget.id == 'task_document_upload_input'){
                var append_block = $('#TaskDocuments');
            }
            else{
                var append_block = $('#myDocuments');
            }
            var file_input = document.getElementById(e.currentTarget.id);
            var files = file_input.files;
            var r = new FileReader();
            r.onload = (function(theFile) {
                return function(e) {
                    var docum = e.target.result.split(',')[1];
                    var file_type = theFile.type;
                    setTimeout(function() {
                        $.ajax({
                            url: "/formulier/form/document/upload",
                            type: 'POST',
                            dataType: 'json',
                            contentType: 'application/json',
                            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'document': docum, 'fileName': theFile.name, 'file_type': file_type, 'formulier_id': formulier_id}}),
                            async: false,
                            success: function (result) {
                                append_block.append('<div class="col-lg-2 col-md-3 col-sm-3"><button type="button" class="close close_button pull-right" aria-label="close" id="'+result.result[0]+'">×</button><a href="/web/content?model=order.document&amp;field=file&amp;id='+result.result[0]+'&amp;filename='+result.result[1]+'&amp;download=true" class="col-lg-12 col-md-12 col-sm-12" target="_blank"><span class="fa fa-file" style="font-size:80px;"/><span style="word-wrap: break-word;">'+result.result[1]+'</span></a></div>');
                            },
                        });
                    }, 0);
                };
            })(files[0]);
            r.readAsDataURL(files[0]);
        });

        // close button work for extra images, videos, documents
       $('.close_button').on('click',function(e) {
            rpc.query({
                model: e.currentTarget.getAttribute('model'),
                method: 'unlink',
                args: [e.currentTarget.id],
             }).then(function (data) {
                e.currentTarget.parentElement.remove();
            });
       });

        $("#collapsed li a").click(function() { 
            $('#collapsed li').removeClass('active');
            $(this).addClass('active');
        });
    });
});