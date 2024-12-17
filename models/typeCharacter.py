# -*- coding: utf-8 -*-

from odoo import models, fields, api


class type_character(models.Model):
    _name = 'game.type_character'
    _description = 'Type Character of game'

    name = fields.Char(string="Name", required=True)
    character = fields.One2many('game.characters', 'characterType', string='Character')
    photo = fields.Image(max_width=200, max_height=200, string="Photo")
    ps = fields.Integer(string="PS", required=True)
    speed = fields.Integer(string="Speed", required=True)
    attackF = fields.Integer(string="Physical Attack", required=True)
    attackM = fields.Integer(string="Magic Attack", required=True)
    resistenceF = fields.Integer(string="Physical Resistence", required=True)
    resistenceM = fields.Integer(string="Magic Resistence", required=True)
    characterType = fields.Selection([
        ('1', 'Top'),
        ('2', 'Jungle'),
        ('3', 'Mid'),
        ('4', 'ADC'),
        ('5', 'Support'),
    ])
