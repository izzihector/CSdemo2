odoo.define('online_opportunity_form.website_opportunity', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $( document ).ready(function() {
        $(this).on('click', ".o_website_opportunity_create", function (e) {
            var allData = {
                'title': parseInt($("select[name='title']").val()),
                'xaa_aa_lead_category': parseInt($("select[name='xaa_aa_lead_category']").val()),
                'xaa_aa_formulier_type': $("select[name='xaa_aa_formulier_type']").val(),
                'xaa_aa_firstname': $("#first_name").val(),
                'xaa_aa_lastname': $("#last_name").val(),
                'street': $("#street").val(),
                'zip': $("#zip").val(),
                'city': $("#city").val(),
                'country': parseInt($("select[name='country']").val()),
                'phone': $("#phone").val(),
                'email': $("#email").val(),
                'xaa_aa_lead_lead_source': parseInt($("select[name='xaa_aa_lead_lead_source']").val()),
            }
            ajax.jsonRpc("/opportunity_form/create", 'call', {
                            'data': allData,
                }).then(
                    function(data) {
                        window.open(data.url, '_self');
                });
        });
    });
});