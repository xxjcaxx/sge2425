from odoo import models, fields, api

class mercat_personatge(models.Model):
    _name = 'game.mercat_personatge'
    _description = 'game.mercat_personatge'

    name = fields.Char()
    precio = fields.Integer()
    imagen = fields.Image(max_width = 200, max_height = 200)
    typePersonaje = fields.Selection([
        ('1','Top'),
        ('2','Jungle'),
        ('3','Mid'),
        ('4','Adc'),
        ('5','Support'),
    ])