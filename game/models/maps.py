# -*- coding: utf-8 -*-

from odoo import models, fields, api


class maps(models.Model):
    _name = 'game.maps'
    _description = 'game map'

    name = fields.Char(
        string = "name",
        required = True,
    )
    mapShape = fields.Selection([
        ('1', 'The Howling Abyss'),
        ('2', 'Summoner\'s Rift'),
        ('3', 'Wild Rift'),
        ('4', 'Spirit Blossom Rift'),
    ])