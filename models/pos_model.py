from odoo import api, fields, models

class ProductCostFormPOS(models.Model):
    _inherit = "pos.order.line"

    # Get Hide Cost authorization property from the user groups
    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege", default=True)
    product_id = fields.Many2one('product.product', string='product')
    is_powermax_product = fields.Boolean('Powermax Product', related='product_id.is_powermax_product', readonly=True)

    # Check if the user has the previlige to get the cost or not
    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")


class ProductCostTreePOS(models.Model):
    _inherit = "pos.order"

    # Get Hide Cost authorization property from the user groups
    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege", default=True)

    product_id = fields.Many2one('product.product', string='product')
    is_powermax_product = fields.Boolean('Powermax Product', related='product_id.is_powermax_product',readonly=True)

    # Check if the user has the previlige to get the cost or not
    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")



