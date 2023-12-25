from odoo import api, fields, models


class ProductCostTree(models.Model):
    _inherit = "sale.order.line"

    # Variable to check if the user has the previlige to see the product cost or not
    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege", default=True)

    # get the property ispowermax_product from the product.product model
    product_id = fields.Many2one('product.product', string='Customer')
    is_powermax_product = fields.Boolean('Powermax Product', related='product_id.is_powermax_product',readonly=True)

    # function to calculate if the user has the previlige to see the product cost or not
    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")


class ProductCostForm(models.Model):
    _inherit = "sale.order"

    # Variable to check if the user has the previlige to see the product cost or not
    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege", default=True)

    # function to calculate if the user has the previlige to see the product cost or not
    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")
