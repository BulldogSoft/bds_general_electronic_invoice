# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#################################################################################

import logging
from odoo import _
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class Instagram(http.Controller):

    @http.route(['/wk_instagram_snippet/get_insta_post'], type='json', auth="public", website=True)
    def get_insta_post(self):
        has_instagram = request.website.has_instagram
        debug = request.env['res.users'].has_group('website.group_website_publisher')
        if not has_instagram:
            if debug:
                return {
                    "error": _("Please enable Instagram option in the Website Settings."),
                    "msg": _("Siguenos en Instagram")
                }
            return {
                "not_enabled": True,
                "msg": _("Siguenos en Instagram")
            }

        insta_basic_display = request.website._getInstagramBasicDisplay()
        insta_user_id = request.website.insta_user_id
        insta_post_count = request.website.insta_post_count
        user_media = insta_basic_display.get_user_media(user_id=insta_user_id, limit=insta_post_count)
        if not user_media["data"]:
            return {
                "no_post": _("There is no post on Instagram account."),
                "msg": _("Siguenos en Instagram")
            }

        return {
            'user_media': user_media,
            'social_instagram': request.website.social_instagram,
            "msg": _("Siguenos en Instagram")
        }
