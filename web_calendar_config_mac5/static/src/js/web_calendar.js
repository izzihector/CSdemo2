odoo.define('web_calendar_config_mac5.web_calendar_config_mac5', function (require) {
"use strict";

var CalendarModel = require('web.CalendarModel');
var CalendarView = require('web.CalendarView');


CalendarModel.include({
    toHHMMSS: function (sec_num) {
        var hours   = Math.floor(sec_num / 3600);
        var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
        var seconds = sec_num - (hours * 3600) - (minutes * 60);

        if (hours   < 10) {hours   = "0"+hours;}
        if (minutes < 10) {minutes = "0"+minutes;}
        if (seconds < 10) {seconds = "0"+seconds;}
        return hours+':'+minutes+':'+seconds;
    },

    _getFullCalendarOptions: function () {
        var result = this._super()
        if (!_.isEmpty(this.mapping.company_data)) {
            result['weekends'] = this.mapping.company_data.calendar_weekends;
            result['weekNumbers'] = this.mapping.company_data.calendar_weeknumber;
            result['firstDay'] = parseInt(this.mapping.company_data.calendar_weekday);
            result['slotEventOverlap'] = this.mapping.company_data.calendar_allow_overlap;
            result['eventStartEditable'] = !this.mapping.company_data.calendar_disable_dragging;
            result['eventDurationEditable'] = !this.mapping.company_data.calendar_disable_resizing;
            result['snapDuration'] = this.toHHMMSS(parseInt(this.mapping.company_data.calendar_snap_minutes) * 60);
            result['slotDuration'] = this.toHHMMSS(parseInt(this.mapping.company_data.calendar_slot_minutes) * 60);
            result['minTime'] = this.toHHMMSS(parseFloat(this.mapping.company_data.calendar_min_time) * 3600.0);
            result['maxTime'] = this.toHHMMSS(parseFloat(this.mapping.company_data.calendar_max_time) * 3600.0);
            result['scrollTime'] = this.toHHMMSS(parseFloat(this.mapping.company_data.calendar_start_time) * 3600.0);
        }
        return result;
    },
});

CalendarView.include({
    init: function (viewInfo, params) {
        this._super.apply(this, arguments);
        var attrs = this.arch.attrs;
        this.controllerParams.mapping['company_data'] = JSON.parse(attrs['company_data']);
        this.loadParams.mapping['company_data'] = JSON.parse(attrs['company_data']);
    },
});

});
