# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
    "name": "Instagram Snippet",
    "summary": "Instagram gallery snippet in website",
    "category": "Website/Website",
    "version": "15.0.1.0.0",
    "sequence": 1,
    "author": "Webkul Software Pvt. Ltd.",
    "license": "Other proprietary",
    "website": "https://store.webkul.com",
    "description": """
Instagram Basic Display API
====================
This module adds Instagram gallery building block to the website builder, 
so that you can display Instagram feed on any page of your website.
    """,
    "live_test_url": "http://odoodemo.webkul.com/?module=wk_instagram_snippet",
    "depends": ['website'],
    "data": [
        'data/refresh_token_cron.xml',
        'views/res_config_settings_views.xml',
        'views/s_instagram_gallery.xml',
        'views/snippets.xml',
    ],
    'external_dependencies': {
        'python': ['instagram-basic-display'],
    },
    'assets': {
        'web.assets_frontend': [
            'wk_instagram_snippet/static/src/css/owl.carousel.css',
            'wk_instagram_snippet/static/src/css/owl.theme.default.css',
            'wk_instagram_snippet/static/src/js/owl.carousel.min.js',
            'wk_instagram_snippet/static/src/css/csspin.css',
            'wk_instagram_snippet/static/src/scss/instagram.scss',
            'wk_instagram_snippet/static/src/js/instagram.animation.js',
            '/wk_instagram_snippet/static/src/xml/instagram.xml',
        ],
        'website.assets_editor': [
            'wk_instagram_snippet/static/src/js/instagram.editor.js',
        ],
    },
    "images": ['static/description/Banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price": 59,
    "currency": "USD",
    "pre_init_hook": "pre_init_check",
}
