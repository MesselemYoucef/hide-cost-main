from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductCostPurchase(models.Model):
    _inherit = "purchase.order.line"

    # Variable to check if the user has the previlige to see the product cost or not
    product_id = fields.Many2one('product.product', string='Customer')
    is_powermax_product = fields.Boolean('Powermax Product', related='product_id.is_powermax_product',readonly=True)

    # function to calculate if the user has the previlige to see the product cost or not
    @api.onchange("price_unit")
    def onchange_product(self):
        for record in self:
            if record.is_powermax_product:
                record.price_unit = 0.0
                raise ValidationError("هذا المنتج غير مصرح بشرائه من بغداد")
        return


