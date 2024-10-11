# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dragon(models.Model):
    _name = 'game.dragon'
    _description = 'game.dragon'

    name = fields.Char()
