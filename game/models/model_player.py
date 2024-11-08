from odoo import models, fields

class model_player(models.Model):
    _name = 'game.model_player'
    _description = 'Perfil de usuario..'


    nom_usuario = fields.Char(string="Nombre de usuario")
    estado = fields.Char()
    correo = fields.Char()
    contra = fields.Char(string="Contraseña") # Añadir widget para contraseña cifrada.
    nivel = fields.Integer()


    icono = fields.Image()
    equipo = fields.Many2one('game.teams', ondelete='set null')

    personajes = fields.One2many('game.characters', 'player', 'Personajes') #Enlazar personajes con usuario.
    icono = fields.Image()

