odoo.define('formulier_type_4.solar_panel_calculation', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;

    $( document ).ready(function() {

        $("select[name='xaa_aa_solar_color_one']").on('change', function (e) {
            var solar_color = $("select[name='xaa_aa_solar_color_one']");
            ajax.jsonRpc("/formulier/pv_quote_infos", 'call', {'solar_color': solar_color.val()}).then(
                function(data) {
                    var solarProduct = $("select[name='xaa_aa_solar_product_one']");
                    solarProduct.html('');
                    if (data.solar_products.length) {
                        _.each(data.solar_products, function(x) {
                            var opt = $('<option>').text(x[1])
                                .attr('value', x[0]);
                            solarProduct.append(opt);
                        });
                    }
                })
        });
    });
});
