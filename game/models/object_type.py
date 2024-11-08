from odoo import models, fields

class object_type(models.Model):
    _name = 'game.object_type'
    _description = 'Descripción de los tipos de objetos.'

    name = fields.Char()
    clase = fields.Selection([
          ('1','Tanque'),
          ('2','Support'),
          ('3','Mago'),
          ('4','ADC')])
    pasiva = fields.Text()
    calidad = fields.Selection([
          ('1','Básico'),
          ('2','Épico'),
          ('3','Legendario'),
          ('4','Mítico')])
    imagen = fields.Image(max_width = 200, max_height = 200)
