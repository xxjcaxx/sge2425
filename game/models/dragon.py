# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dragon(models.Model):
    _name = 'game.dragon'
    _description = 'game.dragon'

    name = fields.Char(string='Name')
    type = fields.Many2one('game.dragon_type',string='Type')
    timeout = fields.Integer(related='name.timeout',string='Timeout')
    expGained = fields.Integer(related='name.expGained',string='Experience Gained')
    avatar = fields.Image(related='name.avatar',string='Avatar')
