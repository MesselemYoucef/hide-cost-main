from odoo import api, fields, models


class ProductCostHide(models.Model):
    _inherit = "product.template"

    # Get Hide Cost authorization property from the user groups
    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege")

    # Create a boolean field to check if the product is powermax or other type
    is_powermax_product = fields.Boolean(String="Is Powermmax Product")

    # Check if the user has the previlige to get the cost or not
    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")
