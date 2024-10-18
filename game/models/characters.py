# -*- coding: utf-8 -*-

from odoo import models, fields, api


class characters(models.Model):
    _name = 'game.characters'
    _description = 'game.characters'

    player = fields.Many2one('game.model_player', string='Players')
    name = fields.Char()
    level = fields.Integer()
    exp = fields.Integer()
    stats = fields.Char()
    objects = fields.Char()
    picture = fields.Image(max_width=200, max_height=200)


