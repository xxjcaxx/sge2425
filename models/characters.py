# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Characters(models.Model):
    _name = 'game.characters'
    _description = 'Game Characters'

    player = fields.Many2one('game.model_player', string='Players')  # Eliminado ondelete
    characterType = fields.Many2one('game.type_character', string='Character Type')
    name = fields.Char()
    type = fields.Many2one('game.type_character', string="Character Type")
    level = fields.Integer()
    ps = fields.Integer(string="PS", related='type.ps', store=True)
    speed = fields.Integer(string="Speed", related='type.speed', store=True)
    attackF = fields.Integer(string="Physical Attack", related='type.attackF', store=True)
    attackM = fields.Integer(string="Magic Attack", related='type.attackM', store=True)
    resistenceF = fields.Integer(string="Physical Resistance", related='type.resistenceF', store=True)
    resistenceM = fields.Integer(string="Magic Resistance", related='type.resistenceM', store=True)
    exp = fields.Integer()
    stats = fields.Char()
    objects = fields.One2many('game.object', 'character', string='Objects')
    picture = fields.Image(max_width=200, max_height=200)