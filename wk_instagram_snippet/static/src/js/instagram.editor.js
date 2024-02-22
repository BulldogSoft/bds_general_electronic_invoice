/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */

odoo.define('wk_instagram_snippet.editor', function (require) {
'use strict';

var core = require('web.core');
var dom = require('web.dom');
var sOptions = require('web_editor.snippets.options');

var _t = core._t;

sOptions.registry.instagramGallery = sOptions.Class.extend({
/**
     * @override
     */
    start: function () {
        var self = this;
        return this._super.apply(this, arguments);

    },

    /**
     * @override
     */
    cleanForSave: function () {
        this.$target.find('.instagram_feed').empty();
    },

});
});
