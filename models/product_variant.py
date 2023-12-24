from odoo import api, fields, models


class ProductVariantCostHide(models.Model):
    _inherit = "product.product"

    hide_cost = fields.Boolean(string="Cost Should Be Hidden", compute="_check_user_cost_privilege")
    # product_template_id = fields.Many2one('product.template', required=True, string="Product Template ID")
    # is_powermax_product = fields.Boolean(string='Is Powermax Product', related='product_template_id.is_powermax_product')

    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = record.env.user.has_group("hide-cost-main.group_see_cost_user")
