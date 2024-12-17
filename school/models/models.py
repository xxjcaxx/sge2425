# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class student(models.Model):
    _name = 'school.student'
    _description = 'Students of school'

    name = fields.Char()
    year = fields.Integer()
    surname = fields.Char(
        string="Surnames",  # Optional label of the field
        required=True,  # Mandatory field
        help='blabla',  # Help tooltip text
    )

    # funciones lambda son de una línea
    # valores default
    signup_date = fields.Datetime(default=fields.Datetime.now)
    signup_date = fields.Datetime(default=lambda self: fields.Datetime.now())

    photo = fields.Image(max_width=200, max_height=200)
    type = fields.Selection([
        ('1', 'Basic'),
        ('2', 'Intermediate'),
        ('3', 'Completed')])


# restricciones CONSTRAINS
# esta funcion se ejecutara cuando intente cambiar el level
#@api.constrains('level')
#def _check_level(self):
 #   for 0 in self:
  #      if o.level > 10:
   #        raise ValidationError("Tu nivel no es válido: %s " % o.level)

class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teachers of school'

    name = fields.Char()
    dni = fields.Char()
