odoo.define('mail_composer_on_send_message/static/src/components/chatter_topbar/chatter_topbar.js', function (require) {
'use strict';

    const components = {Composer: require('mail/static/src/components/chatter_topbar/chatter_topbar.js')};
    const { patch } = require('web.utils');

    patch(components.Composer, 'mail_composer_on_send_message/static/src/components/chatter_topbar/chatter_topbar.js', {
        /**
        * Overwrite to always launch full composer instead of quick messages
        */
        _onClickSendMessage(ev) {
            this._super.apply(this, arguments);
            if (this.chatter.composer && this.chatter.isComposerVisible && !this.chatter.composer.isLog) {
                this.chatter.update({ isComposerVisible: false });
                this.chatter.composer.openFullComposer();
            };
        },
    });

});
 