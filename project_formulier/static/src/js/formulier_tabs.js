odoo.define('project_formulier.formulier_tabs', function (require) {
'use strict';

    $(document).ready(function () {

        var task_op = $('#nav_tabs_task_op_form');
        var quote_op = $('#nav_tabs_quote_op_form');
        var task_op_image = $('#nav_tabs_task_op_image_form');
        var task_op_extra_image = $('#nav_tabs_task_op_extra_image_form');
        var task_op_video = $('#nav_tabs_task_op_video_form');

        if (task_op.length > 0){
            var inputs = task_op[0].querySelectorAll('input,select,textarea')
            inputs.forEach(function(element) {
                element.disabled='true';
            });
        }
        if (quote_op.length > 0){
            var inputs = quote_op[0].querySelectorAll('input,select,textarea')
            inputs.forEach(function(element) {
                element.disabled='true';
            });
        }
        if (task_op_image.length > 0){
            var inputs = task_op_image[0].querySelectorAll('input')
            inputs.forEach(function(element) {
                $('#'+element.name).prev().hide();
            });
        }
        if (task_op_extra_image.length > 0){
            var inputs = task_op_extra_image[0].querySelectorAll('button')
            var upload = task_op_extra_image[0].querySelectorAll('.custom-file-upload')
            upload[0].parentElement.hidden = true
            inputs.forEach(function(element) {
                element.hidden='true';
            });
        }
        if (task_op_video.length > 0){
            var inputs = task_op_video[0].querySelectorAll('button')
            var upload = task_op_video[0].querySelectorAll('.custom-file-upload')
            upload[0].parentElement.hidden = true
            inputs.forEach(function(element) {
                element.hidden='true';
            });
        }
    });
});