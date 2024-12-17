from odoo import models, fields, api

class model_player(models.Model):
    _name = 'game.model_player'
    _description = 'Perfil de usuario..'

    nom_usuario = fields.Char(string="Nombre de usuario")
    estado = fields.Char()
    correo = fields.Char()
    contra = fields.Char(string="Contraseña")  # Añadir widget para contraseña cifrada.
    nivel = fields.Integer()

    icono = fields.Image()
    equipo = fields.Many2one('game.teams')  # Eliminado ondelete

    personajes = fields.One2many('game.characters', 'player', 'Personajes')  # Enlazar personajes con usuario.

    @api.onchange('estado')
    def _onchange_estado(self):
        if self.estado:
            self.estado = self.estado.capitalize()