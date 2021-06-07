odoo.define('project_formulier.image_customization', function (require) {
'use strict';

    var rpc = require('web.rpc');

    $(document).ready(function () {

        // edit images field on project-formulier/id/pf_access
        $('.edit_button').on('click', function (e) {
            var file_input = $('input[name="'+e.currentTarget.nextElementSibling.id+'"]')
            file_input.click();
            e.preventDefault();
            file_input.on('change', function(e){
                var file = this.files[0];
                var currentImg = $('img[id="'+e.currentTarget.name+'"]');
                currentImg.after($('<span class="text-success">Uploading....</span>'))
                var reader = new FileReader();
                reader.onloadend = function() {
                    var data=(reader.result).split(',')[1];
                    var write_values = {};
                    write_values[e.currentTarget.name] = data;
                    currentImg[0].src=reader.result;
                    console.log(write_values);
                    rpc.query({
                        model: 'question.formulier',
                        method: 'write',
                        args: [[parseInt($("#formulier_id").val())],
                                    write_values],
                     }).then(function (data) {
                        currentImg.next()[0].replaceWith($('<span class="text-success">Image uploaded successfully</span>')[0]);
                    });
                }
                reader.readAsDataURL(file);
            });
        });

         $(".project_formulier_form img").on('click mouseenter',function(e){
            var curr_img = e.currentTarget;
            curr_img.style="opacity:0.4";
            var search_icon = $('<span class="fa fa-search image_zoom"></span>')[0];
            curr_img.after(search_icon);
            $(curr_img).on('click',function(event){
                $(event.currentTarget).addClass('img_zoom');
                event.currentTarget.style="opacity:1";
                search_icon.remove();
            });
         });
         $(".project_formulier_form img").on('mouseleave',function(e){
            var curr_img = e.currentTarget;
            curr_img.style="opacity:1";
            if (curr_img.nextElementSibling.className.includes('image_zoom')){
                curr_img.nextElementSibling.remove();
            }
            $(curr_img).removeClass('img_zoom');
         });
    });
});