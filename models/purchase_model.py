from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductCostPurchase(models.Model):
    _inherit = "purchase.order.line"

    product_id = fields.Many2one('product.product', string='Customer')
    is_powermax_product = fields.Boolean('Powermax Product', related='product_id.is_powermax_product',readonly=True)



    # @api.constrains("price_unit")
    # def _check_if_product_powermax(self):
    #     for record in self:
    #         if record.is_powermax_product:
    #             raise ValidationError("This Product Cannot Be Bought from Baghdad")





    @api.onchange("price_unit")
    def onchange_product(self):
        for record in self:
            if record.is_powermax_product:
                record.price_unit = 0.0
                raise ValidationError("هذا المنتج غير مصرح شرائه من بغداد")
        return


