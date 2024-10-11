
from odoo import models, fields, api  # Aquí se importa 'models'

class forja(models.Model):
    _name = 'game.game'
    _description = 'game.game'

    name = fields.Char()
    description = fields.Text()
