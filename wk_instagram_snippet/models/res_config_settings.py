# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#################################################################################

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    has_instagram = fields.Boolean(
        string="Instagram",
        related='website_id.has_instagram', readonly=False
    )
    insta_access_token = fields.Char(
        related='website_id.insta_access_token', readonly=False,
        string='Access Token'
    )
    insta_user_id = fields.Char(
        related='website_id.insta_user_id', readonly=False,
        string='User ID'
    )
    insta_post_count = fields.Integer(
        related='website_id.insta_post_count', readonly=False,
        string='Count', help='Total number of Instagram post that will be displayed in instagram snippets block.'
    )

    insta_nav = fields.Boolean(string='Slider Nav', help='By enable this Nav will see right and left side of your image')

    @api.constrains('has_instagram', 'insta_post_count')
    def _check_insta_post_count(self):
        for record in self:
            if record.has_instagram:
                if record.insta_post_count < 4:
                    raise ValidationError(_("Count should not be less than 4"))

    def _check_insta_authorization(self):
        try:
            profile = self.website_id.fetch_profile()
            if profile:
                self.insta_user_id = profile.get('id')
        except Exception as e:
            _logger.info(_('Please double-check your Instagram Basic Display API Access Token!'), exc_info=True)
            raise UserError(_('Please double-check your Instagram Basic Display API Access Token'))

    @api.model
    def create(self, vals):
        InstaConfig = super(ResConfigSettings, self).create(vals)
        if vals.get('has_instagram') and vals.get('insta_access_token'):
            InstaConfig._check_insta_authorization()
        return InstaConfig

    def write(self, vals):
        InstaConfig = super(ResConfigSettings, self).write(vals)
        if vals.get('has_instagram') and vals.get('insta_access_token'):
            InstaConfig._check_insta_authorization()
        return InstaConfig
