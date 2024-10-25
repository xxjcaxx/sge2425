# -*- coding: utf-8 -*-

from odoo import models, fields, api


class characters(models.Model):
    _name = 'game.characters'
    _description = 'game.characters'

    player = fields.Many2one('game.model_player', string='Players')
    characterType = fields.Many2one('game.type_character',
                                    string='Character Type')
    name = fields.Char()
    level = fields.Integer()
    exp = fields.Integer()
    stats = fields.Char()
    objects = fields.One2many('game.object', 'character',
                              string='Objects')
    picture = fields.Image(max_width=200, max_height=200)
