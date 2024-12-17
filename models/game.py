# -*- coding: utf-8 -*-

from odoo import models, fields, api


class game(models.Model):
    _name = 'game.game'
    _description = 'game.game'

    name = fields.Char()
    description = fields.Text()
    avatar = fields.Image(max_width = 200, max_height = 200)


