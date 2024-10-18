# -*- coding: utf-8 -*-

from odoo import models, fields, api


class object(models.Model):
    _name = 'game.object'
    _description = 'game.object'



 

    nombre = fields.Text()
    precio = fields.Text()
    activa = fields.Text()
    tipo = fields.Many2one('game.object_type')
    imagen = fields.Image(related = 'tipo.imagen')