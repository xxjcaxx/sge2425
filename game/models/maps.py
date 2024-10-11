# -*- coding: utf-8 -*-

from odoo import models, fields, api


class game(models.Model):
    _name = 'game.maps'
    _description = 'game map'

    gamemode = fields.Char()
    name = fields.Char()
    numPlayers = fields.Integer()
    characterType = fields.Selection([

        ('1','Top'),
        ('2','Jungle'),
        ('3','Mid'),
        ('4','Adc'),
        ('5','Support'),

    ])
    mapShape = fields.Selection([

        ('1', 'The Howling Abyss'),
        ('2', 'Summoner\'s Rift'),
        ('3', 'Wild Rift'),
        ('4', 'Spirit Blossom Rift'),

    ])