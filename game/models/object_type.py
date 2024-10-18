from odoo import models, fields

class object_type(models.Model):
    _name = 'game.object_type'
    _description = 'Descripción de los tipos de objetos.'


    clase = fields.Selection([
          ('1','Ligera'),
          ('2','Media'),
          ('3','Pesada')])
    personaje = fields.Text(string='Personaje')
    pasiva = fields.Text()
    activa = fields.Text()
    stats = fields.Text()
    calidad = fields.Selection([
          ('1','Básico'),
          ('2','Épico'),
          ('3','Legendario'),
          ('4','Mítico')])
    imagen = fields.Image()
