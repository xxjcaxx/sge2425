# -*- coding: utf-8 -*-

from odoo import models, fields, api


class teams(models.Model):
    _name = 'game.teams'
    _description = 'Equipos.'

    name = fields.Char()
    level = fields.Integer()
    player_list = fields.One2many('game.model_player', 'equipo')
