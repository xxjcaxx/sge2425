# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dragon_type(models.Model):
    _name = 'game.dragon_type'
    _description = 'game.dragon_type'

    name = fields.Selection(string='Name')
    type = fields.Selection([
        ('1', 'Mushu'),
        ('2', 'Toothless'),
        ('3', 'EnderDragon'),
        ('4', 'Charizard'),
        ('5', 'Shenlong'),
        ('6', 'Polunga'),
        ('7', 'Smaug'),
        ('8', 'Ryūjin')],string='Type')
    timeout = fields.Integer(string='Timeout')
    expGained = fields.Integer(string='Experience Gained')
    avatar = fields.Image(max_width = 200, max_height = 200,string='Avatar')
