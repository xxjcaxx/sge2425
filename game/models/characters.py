# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Characters(models.Model):
    _name = 'game.characters'
    _description = 'Game Characters'

    name = fields.Char()
    type = fields.Many2one('game.type_character')
    level = fields.Integer()
    # Características
    ps = fields.Integer(string="PS", related='type.ps', store=True)
    speed = fields.Integer(string="Speed", related='type.speed', store=True)
    attackF = fields.Integer(string="Physical Attack", related='type.attackF', store=True)
    attackM = fields.Integer(string="Magic Attack", related='type.attackM', store=True)
    resistenceF = fields.Integer(string="Physical Resistance", related='type.resistenceF', store=True)
    resistenceM = fields.Integer(string="Magic Resistance", related='type.resistenceM', store=True)
    exp = fields.Integer()
    objects = fields.Char()
    picture = fields.Image(max_width=200, max_height=200)




