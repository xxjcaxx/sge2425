from odoo import models, fields

class object_type(models.Model):
    _name = 'game.object_type'
    _description = 'Descripción de los tipos de objetos.'


    Clase = fields.Selection([
          ('1','Ligera'),
          ('2','Media'),
          ('3','Pesada')])
    Personaje = fields.Text(string='Personaje')
    Pasiva = fields.Text()
    Activa = fields.Text()
    Stats = fields.Text()
    Calidad = fields.Selection([
          ('1','Básico'),
          ('2','Épico'),
          ('3','Legendario'),
          ('4','Mítico')])
    Imagen = fields.Image()
