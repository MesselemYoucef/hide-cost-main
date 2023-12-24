from odoo import api, fields, models


class ProductCostHide(models.Model):
    _inherit = "product.template"

    hide_cost = fields.Boolean(string="Cost Should Be Hidden", compute="_check_user_cost_privilege")
    is_powermax_product = fields.Boolean(String="Is Powermmax Product")

    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")
