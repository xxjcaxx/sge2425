# -*- coding: utf-8 -*-

from odoo import models, fields, api


class type_character(models.Model):
    _name = 'game.type_character'
    _description = 'Type Character of game'

    name = fields.Char(
        string="Name",   # Optional label of the field
        required = True  # Mandatory field
    )
    character = fields.One2many('game.characters', 'characterType',
                                string='Character')

    photo = fields.Image(
        string="Photo",  # Optional label of the field
        max_width = 200, 
        max_height = 200
    )

    #Características
    ps = fields.Integer(
        string="PS",     # Optional label of the field
        required = True  # Mandatory field
    )
    speed = fields.Integer(
        string="Speed",  # Optional label of the field
        required = True  # Mandatory field
    )
    attackF = fields.Integer(
        string="Physical Attack",  # Optional label of the field
        required = True            # Mandatory field
    )
    attackM = fields.Integer(
        string="Magic Attack",  # Optional label of the field
        required = True         # Mandatory field
    )
    resistenceF = fields.Integer(
        string="Physical Resistence",  # Optional label of the field
        required = True                # Mandatory field
    )
    resistenceM = fields.Integer(
        string="Magic Resistence",  # Optional label of the field
        required = True             # Mandatory field
    )

    #Tipo de personaje
    characterType = fields.Selection([
        ('1', 'Top'),
        ('2', 'Jungle'),
        ('3', 'Mid'),
        ('4', 'ADC'),
        ('5', 'Support'),
    ])
