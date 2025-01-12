from odoo import  api, fields, models

class SaleOrderMartyDev(models.Model):
    _inherit = "sale.order"

    display_ITBIS = fields.Boolean(
        string='Mostrar ITBIS en PDF?',
        default= True,
    )
