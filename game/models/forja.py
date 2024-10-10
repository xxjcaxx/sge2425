

from odoo import models, fields, api

class forja(models.Model):
        _name = "forja"
        _description = "roba madrid"

        name = fields.Char()
        type = fields.Char()
        level = fields.Integer()

    
    