from odoo import api, fields, models


class ProductCostTree(models.Model):
    _inherit = "sale.order.line"

    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege", default=True)

    product_id = fields.Many2one('product.product', string='Customer')
    is_powermax_product = fields.Boolean('Powermax Product', related='product_id.is_powermax_product',readonly=True)

    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")


class ProductCostForm(models.Model):
    _inherit = "sale.order"

    hide_cost = fields.Boolean(string="Cost Hidden", compute="_check_user_cost_privilege", default=True)

    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")
