/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */

odoo.define('wk_instagram_snippet.animation', function (require) {
'use strict';

var core = require('web.core');
var publicWidget = require('web.public.widget');

var qweb = core.qweb;
var time = require('web.time');


publicWidget.registry.instagramGallery = publicWidget.Widget.extend({
    selector: '.instagram_gallery',
    // xmlDependencies: ['/wk_instagram_snippet/static/src/xml/instagram.xml'],
    disabledInEditableMode: false,

    events: {
        'click .instagram_feed_quick_view': '_onClickInstagramFeedQuickView',
    },

    start: function () {
        var self = this;
        var $instagram_feed = this.$('.instagram_feed');

        $instagram_feed.append('<center><div class="cp-spinner cp-boxes"></div></center>');
        var def = this._rpc({route: '/wk_instagram_snippet/get_insta_post'}).then(function (data) {
            $instagram_feed.empty();

            // if (_.isEmpty(data)) {
            //     return;
            // }
           
            $( document ).ready( function() {
                $('.owl-carousel').owlCarousel({
                    margin:10,
                    loop:true,
                    dots:true,
                    responsiveClass: true,
                    nav:true,
                    navText:["<b><</b>","<b>></b>"],  
                    navigation : true,
                    responsive:{
                        0:{ 
                            dotsEach: 2,
                            items:1,
                            
                        },
                        400:{
                            items:2,
                            dotsEach: 3,
                        },
                        800:{
                            items:3,
                            dotsEach: 4,
                        },
                        1000:{ items:4,
                            dotsEach: 4,
                        },
                        2000:{
                            items:4,
                            dotsEach: 5,}
                    }
                });
            });  

            if (data.not_enabled) {
                return;
            }

            if (data.error) {
                $instagram_feed.append(qweb.render('Website.Instagram.Error', {data: data}));
                return;
            }

            if (data.no_post) {
                $instagram_feed.append(qweb.render('Website.Instagram.NoPost', {data: data}));
                return;
            }
            console.log(data);
            $instagram_feed.append(qweb.render('Website.Instagram.Gallery', {data: data}));
            return;

        });
        return Promise.all([this._super.apply(this, arguments), def]);
    },

    _onClickInstagramFeedQuickView: function(ev){
        var $target = $(ev.currentTarget).parent('.img-info');
        var caption = $target.find('.caption').attr('insta-caption');
        var media_url = $target.find('.media_url').attr('insta-media_url');
        var permalink = $target.find('.permalink').attr('insta-permalink');
        var timestamp = $target.find('.timestamp').attr('insta-timestamp');
        var username = $target.find('.username').attr('insta-username');
        var $modal = $('#insta_feed_view_modal');
        $modal.modal('show').find(".modal-content").removeClass("fadeIn").find(".data_loader").show();
        $modal.find('.insta-image').attr("src", media_url);
        $modal.find('.username').text('@' + username);
        if(caption){
            $modal.find('.caption').text(caption);
        }else{
            $modal.find('.caption').text('');
        }
        $modal.find('.view-on-insta').attr("href", permalink);
        $modal.find('.insta-link').attr("href", 'https://www.instagram.com/' + username + '/');
        $modal.find('.updated_on').text(moment(timestamp).format('DD-MM-YYYY HH:MM:SS'));
        $modal.find('.modal-content').find(".data_loader").hide();
    },
});
});
