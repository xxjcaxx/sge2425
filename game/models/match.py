from odoo import models, fields

class model_player(models.Model):
    _name = 'game.match'
    _description = 'Partida'

    lista_equipos = fields.Char() # Esperando a que Marc acabe los equipos.
    lista_jugadores = fields.Many2many('game.model_player') # Muchos jugadores en muchas partidas. -- A lo mejor se quita luego.
    lista_personajes_jugador = fields.Many2many('game.characters') #Muchas listas a personajes. Cada personaje tiene un jugador.
    ganador = fields.Char() # Gana un equipo -- Esperando a que Marc acabe los equipos.
    data_inicio = fields.Datetime() 
    tiempo = fields.Integer()
    puntos = fields.Integer()
