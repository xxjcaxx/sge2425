# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dragon(models.Model):
    _name = 'game.dragon'
    _description = 'game.dragon'

    name = fields.Char()
    timeout = fields.Integer()
    expGained = fields.Integer()
    avatar = fields.Image(max_width = 200, max_height = 200)


