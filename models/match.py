from odoo import models, fields

class match(models.Model):
    _name = 'game.match'
    _description = 'Partida'

    lista_equipos = fields.Char()
    lista_jugadores = fields.Many2many('game.model_player')  # Muchos jugadores en muchas partidas.
    lista_personajes_jugador = fields.Many2many('game.characters')  # Muchas listas a personajes.
    ganador = fields.Char()
    data_inicio = fields.Datetime()
    tiempo = fields.Integer()
    puntos = fields.Integer()