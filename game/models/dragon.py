# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dragon(models.Model):
    _name = 'game.dragon'
    _description = 'game.dragon'

    name = fields.Char(string='Name')
    type = fields.Many2one('game.dragon_type', string='Type')
    timeout = fields.Integer(related='type.timeout', string='Timeout')
    expGained = fields.Integer(related='type.expGained', string='Experience Gained')
    avatar = fields.Image(related='type.avatar', string='Avatar')
