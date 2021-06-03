odoo.define('customer_project_formulier.email_validation', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function() {

        $("#email").on('keydown',function(e){
            if (e.keyCode == 32) {
                return false;
            }
        });
        

        // var email = jQuery('#email');
        // var hint = jQuery("#hint");
        // email.on('blur',function() {
        //     hint.css('display', 'none').empty(); // hide hint initially
        //     jQuery(this).mailcheck({
        //         suggested: function(element, suggestion) {
        //             if(!hint.html()) {
        //                 // misspell - display hint element
        //                  var suggestion = "Did you mean <span class='suggestion'>" +
        //                     "<span class='address'>" + suggestion.address + "</span>"
        //                     + "@<a href='#' class='domain'>" + suggestion.domain +
        //                     "</a></span>?";
     
        //                 hint.html(suggestion).fadeIn(150);
        //             } else {
        //                 // Subsequent errors
        //                 jQuery(".address").html(suggestion.address);
        //                 jQuery(".domain").html(suggestion.domain);
        //             }
        //         }
        //     });
        // });
     
        // hint.on('click', '.domain', function() {
        //     // Display with the suggestion and remove the hint
        //     email.val(jQuery(".suggestion").text());
        //     hint.fadeOut(200, function() {
        //         jQuery(this).empty();
        //     });
        //     return false;
        // });
    });

});

