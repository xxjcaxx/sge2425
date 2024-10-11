<<<<<<< HEAD
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class forja(models.Model):
    _name = 'game.forja'
    _description = 'game.forja'

    name = fields.Char()
    description = fields.Text()


=======

from odoo import models, fields, api  # Aquí se importa 'models'

class forja(models.Model):
    _name = 'game.game'
    _description = 'game.game'

    name = fields.Char()
    description = fields.Text()
>>>>>>> 5e743e72fe14120bc84c3de0bb98ca2c943e323a
