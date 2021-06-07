odoo.define('opportunity_meeting.CalendarPopover', function (require) {
"use strict";

const CalendarPopover = require('web.CalendarPopover');
var rpc = require('web.rpc');

const OpportunityCalendarPopover = CalendarPopover.include({
    init: function () {
        var self = this;
        this._super.apply(this, arguments);
        self.xaa_aa_phone = '';
        if (this.event){
            this._rpc({
                model: 'calendar.event',
                method: 'search_read',
                domain: [['id', '=', this.event.id]],
                fields: ['xaa_aa_phone'],
                limit: 1,
            }).then(function (data) {
                if(data.length){
                    self.xaa_aa_phone = data[0].xaa_aa_phone;
                }
            });
         }
    },
});

return {
        OpportunityCalendarPopover,
    };
});
