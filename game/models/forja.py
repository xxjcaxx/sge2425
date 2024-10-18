# -*- coding: utf-8 -*-

from odoo import models, fields, api


class forja(models.Model):
    _name = 'game.game'
    _description = 'game.game'

    name = fields.Char()
    description = fields.Text()


