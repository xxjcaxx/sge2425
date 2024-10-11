# -*- coding: utf-8 -*-

from odoo import models, fields, api


class forja(models.Model):
    _name = 'game.forja'
    _description = 'game.forja'

    name = fields.Char()
    description = fields.Text()


