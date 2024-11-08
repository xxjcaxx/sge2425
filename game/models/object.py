# -*- coding: utf-8 -*-

from odoo import models, fields, api


class object(models.Model):
    _name = 'game.object'
    _description = 'game.object'
    character = fields.Many2one('game.characters', string='Character objects')
    objectType = fields.Many2one('game.object_type', string='Object Type')
    nombre = fields.Text()
    precio = fields.Text()
    activa = fields.Text()
    tipo = fields.Many2one('game.object_type')
    imagen = fields.Image(related='tipo.imagen')
