from odoo import models, fields

class Partner(models.Model):
    _inherit = "res.partner"

    pets_id = fields.One2many('res.partner', 'partner_id', string='Pet')