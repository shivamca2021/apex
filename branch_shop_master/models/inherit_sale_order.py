from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime, timedelta


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _default_brand(self):
        def _default_brand(self):
            return self.env.user.default_brand_id,id

    brand_id = fields.Many2one('brand.master', default=_default_brand)
    shop_id = fields.Many2one('shop.master',domain="[('brand_id','=',brand_id)]")

