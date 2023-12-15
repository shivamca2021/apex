from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime, timedelta


class BrandMaster(models.Model):
    _name = 'brand.master'

    name = fields.Char('')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    zip = fields.Char(string='Zip')
    city = fields.Char(string='City')
    state_id = fields.Many2one(
        'res.country.state', string="Fed. State", domain="[('country_id', '=?', country_id)]"
    )
    country_id = fields.Many2one('res.country', string="Country")
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    company_id = fields.Many2one('res.company', string="Company")


class ShopMaster(models.Model):
    _name = 'shop.master'

    name = fields.Char('')
    brand_id = fields.Many2one('brand.master', required=True)
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    zip = fields.Char(string='Zip')
    city = fields.Char(string='City')
    state_id = fields.Many2one(
        'res.country.state', string="Fed. State", domain="[('country_id', '=?', country_id)]"
    )
    country_id = fields.Many2one('res.country', string="Country")
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')

    