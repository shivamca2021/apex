from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command
from odoo.exceptions import UserError, ValidationError


class Users(models.Model):
    _inherit = "res.users"

    @api.onchange('company_ids')
    def company_ids_onchange(self):
        if self.company_ids:
            bnd_ids = self.env['brand.master'].search([('company_id', '=', self.company_ids.ids)]).ids
            if bnd_ids:
                return {'domain': {'allowed_brand': [('id', 'in', bnd_ids)]}}

    @api.onchange('allowed_brand')
    def allowed_brand_onchange(self):
        if self.allowed_brand:
            shop_ids = self.env['shop.master'].search([('brand_id', '=', self.allowed_brand.ids)]).ids
            if shop_ids:
                return {'domain': {'allowed_shop': [('id', 'in', shop_ids)]}}

    @api.constrains('default_brand_id', 'allowed_brand', 'active')
    def _check_brand(self):
        for user in self.filtered(lambda u: u.active):
            if user.default_brand_id not in user.allowed_brand:
                raise ValidationError(
                    _('Brand %(brand_name)s is not in the allowed brands for user %(user_name)s (%(brand_allowed)s).',
                      brand_name=user.default_brand_id.name,
                      user_name=user.name,
                      brand_allowed=', '.join(user.mapped('allowed_brand.name')))
                )

    @api.constrains('default_shop_id', 'allowed_shop', 'active')
    def _check_dhop(self):
        for user in self.filtered(lambda u: u.active):
            if user.default_shop_id not in user.allowed_shop:
                raise ValidationError(
                    _('Shop %(shop_name)s is not in the allowed shops for user %(user_name)s (%(shop_allowed)s).',
                      shop_name=user.default_shop_id.name,
                      user_name=user.name,
                      shop_allowed=', '.join(user.mapped('allowed_shop.name')))
                )
    
    allowed_brand = fields.Many2many('brand.master', 'res_brand_users_rel', 'brand_user_id', 'brand_id',
                                      string='Allowed Brand')
    default_brand_id = fields.Many2one('brand.master', string='Default Brand',
                                       domain="[('id', 'in', allowed_brand)]")
    allowed_shop = fields.Many2many('shop.master', 'res_shop_users_rel', 'user_id', 'shop_id',
                                      string='Allowed shop')
    default_shop_id = fields.Many2one('shop.master', string='Default Shop',
                                      domain="[('id', 'in', allowed_shop)]")





