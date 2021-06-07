odoo.define('crm_lead_activity_customization.LeadMenu', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');
var QWeb = core.qweb;

const { Component } = owl;

/**
 * Menu item appended in the systray part of the navbar, redirects to the next
 * leads
 */
var LeadMenu = Widget.extend({
    name: 'lead_menu',
    template:'crm_lead_activity_customization.LeadMenu',
    events: {
        'click .o_mail_preview': '_onLeadFilterClick',
        'show.bs.dropdown': '_onLeadMenuShow',
        'hide.bs.dropdown': '_onLeadMenuHide',
    },
    start: function () {
        this._$leadsPreview = this.$('.o_mail_systray_dropdown_items');
        Component.env.bus.on('activity_updated', this, this._updateCounter);
        this._updateCounter();
        this._updateLeadPreview();
        return this._super();
    },
    //--------------------------------------------------
    // Private
    //--------------------------------------------------
    /**
     * Make RPC and get current user's lead details
     * @private
     */
    _getLeadData: function () {
        var self = this;

        return self._rpc({
            model: 'res.users',
            method: 'systray_get_leads',
            args: [],
            kwargs: {context: session.user_context},
        }).then(function (data) {
            self._leads = data;
            self.leadCounter = _.reduce(data, function (total_count, p_data) { return total_count + p_data.total_count || 0; }, 0);
            self.$('.o_notification_counter').text(self.leadCounter);
            self.$el.toggleClass('o_no_notification', !self.leadCounter);
        });
    },
    _updateLeadPreview: function () {
        var self = this;
        self._getLeadData().then(function (){
            self._$leadsPreview.html(QWeb.render('crm_lead_activity_customization.LeadMenu.Previews', {
                widget: self
            }));
        });
    },
    /**
     * update counter based on activity status(created or Done)
     * @private
     * @param {Object} [data] key, value to decide activity created or deleted
     * @param {String} [data.type] notification type
     * @param {Boolean} [data.activity_deleted] when activity deleted
     * @param {Boolean} [data.activity_created] when activity created
     */
    _updateCounter: function (data) {
        if (data) {
            if (data.activity_created) {
                this.leadCounter ++;
            }
            if (data.activity_deleted && this.leadCounter > 0) {
                this.leadCounter --;
            }
            this.$('.o_notification_counter').text(this.leadCounter);
            this.$el.toggleClass('o_no_notification', !this.leadCounter);
        }
    },

    //------------------------------------------------------------
    // Handlers
    //------------------------------------------------------------

    /**
     * Redirect to particular model view
     * @private
     * @param {MouseEvent} event
     */
    _onLeadFilterClick: function (event) {
        // fetch the data from the button otherwise fetch the ones from the parent (.o_mail_preview).
        var data = _.extend({}, $(event.currentTarget).data(), $(event.target).data());
        if (data.res_model === "crm.lead") {
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: data.res_model,
                res_id: data.id,
                views: [[false, 'form']],
                target: 'current',
                clear_breadcrumbs: true,
            });
        } else {
            this._super.apply(this, arguments);
        }
    },
    /**
     * @private
     */
    _onLeadMenuShow: function () {
        document.body.classList.add('modal-open');
         this._updateLeadPreview();
    },
    /**
     * @private
     */
    _onLeadMenuHide: function () {
        document.body.classList.remove('modal-open');
    },
});

SystrayMenu.Items.push(LeadMenu);

return LeadMenu;

});
