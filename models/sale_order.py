from odoo import  api, fields, models

class AccountMoveMartyDev(models.Model):
    _inherit = "account.move"

    display_ITBIS = fields.Boolean(
        string='Mostrar ITBIS en PDF?',
        default= True,
    )
