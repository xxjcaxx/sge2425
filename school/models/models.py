# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
     _name = 'school.student'
     _description = 'Students of school'    sdf

     name = fields.Char()
     year = fields.Integer()
     surname = fields.Char(
          string="Surnames",  # Optional label of the field
          required = True,  # Mandatory field
          help = 'blabla',  # Help tooltip text
     )
     photo = fields.Image(max_width = 200, max_height = 200)
     type = fields.Selection([
          ('1','Basic'),
          ('2','Intermediate'),
          ('3','Completed')])


class teacher(models.Model):
     _name = 'school.teacher'
     _description = 'Teachers of school'

     name = fields.Char()
     dni = fields.Char()