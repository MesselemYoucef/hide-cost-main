from odoo import api, fields, models


class ProductVariantCostHide(models.Model):
    _inherit = "product.product"

    # Variable to check if the user has the previlige to see the product cost or not
    hide_cost = fields.Boolean(string="Cost Should Be Hidden", compute="_check_user_cost_privilege")

    # function to calculate if the user has the previlige to see the product cost or not
    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")
