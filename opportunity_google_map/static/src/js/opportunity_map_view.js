odoo.define('opportunity_google_map.opportunity_map_view', function (require) {
    "use strict";

    const MapView = require('web_map.MapView');
    const MapViewController = require('web_map.MapController');

    MapView.include({
        init: function (viewInfo, params) {
            this._super.apply(this, arguments);

            if (params.modelName == 'crm.lead' && params.context.is_hide_pager == true) {
                this.loadParams.limit = this.arch.attrs.limit ?
                    parseInt(this.arch.attrs.limit, 10) :
                    params.limit || 0;
            } else {
                this.loadParams.limit = this.arch.attrs.limit ?
                    parseInt(this.arch.attrs.limit, 10) :
                    params.limit || 80;
            }
        },
    });

    MapViewController.include({
        _onOpenClicked: function (ev) {
            if (ev.data.ids.length > 1) {
                this.do_action({
                    type: 'ir.actions.act_window',
                    name: this.actionName,
                    views: [[false, 'list'], [false, 'form']],
                    res_model: this.modelName,
                    domain: [['id', 'in', ev.data.ids]],
                    target: '_blank',
                });
            } else {
                if (this.modelName.includes('crm.lead')){
                    this.do_action({
                        type: 'ir.actions.act_window',
                        views: [[false, 'form']],
                        res_model: this.modelName,
                        res_id: ev.data.ids[0],
                        target: 'new',
                    });
                }
                else{
                    this.trigger_up('switch_view', {
                        view_type: 'form',
                        res_id: ev.data.ids[0],
                        mode: 'readonly',
                        model: this.modelName,
                    });
                }
            }
        },
    });

});
