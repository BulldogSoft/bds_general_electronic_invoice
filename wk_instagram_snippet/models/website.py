# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################

import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)

try:
    from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
except ImportError:
    InstagramBasicDisplay = None
    _logger.warning('Instagram Basic Display Python API library not found, please install the Instagram Basic Display Python API library from https://pypi.org/project/instagram-basic-display/')


class Website(models.Model):
    _inherit = 'website'

    has_instagram = fields.Boolean(string='Instagram')
    insta_access_token = fields.Char(string='Access Token')
    insta_user_id = fields.Char(string='User ID')
    insta_post_count = fields.Integer(string='Count')

    def _getInstagramBasicDisplay(self):
        insta_basic_display = InstagramBasicDisplay(
            app_id=None,
            app_secret=None,
            redirect_url=None
        )
        insta_basic_display.set_access_token(self.insta_access_token)
        return insta_basic_display

    def fetch_profile(self):
        insta_basic_display = self._getInstagramBasicDisplay()
        return insta_basic_display.get_user_profile()

    def _cron_refresh_token(self):
        for record in self.env['website'].search([]):
            if record.insta_access_token:
                insta_basic_display = record._getInstagramBasicDisplay()
                refresh_token = insta_basic_display.refresh_token(record.insta_access_token)
                if 'access_token' in refresh_token:
                    record.write({'insta_access_token': refresh_token['access_token']})
