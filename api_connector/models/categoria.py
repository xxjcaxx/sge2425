from odoo import models, fields

class RecuperacionCategoria(models.Model):
    _name = 'recuperacion.categoria'
    _description = 'Categoría de Nadadores'

    name = fields.Char(string="Nombre", required=True)
    min_age = fields.Integer(string="Edad Mínima", required=True)
    max_age = fields.Integer(string="Edad Máxima", required=True)
    nadador_ids = fields.One2many('res.partner', 'categoria_id', string="Nadadores")

    @api.constrains('min_age', 'max_age')
    def _check_age_range(self):
        for record in self:
            if record.min_age > record.max_age:
                raise exceptions.ValidationError("La edad mínima no puede ser mayor que la edad máxima.")

            overlapping_categories = self.env['recuperacion.categoria'].search([
                ('id', '!=', record.id),
                ('max_age', '>=', record.min_age),
                ('min_age', '<=', record.max_age)
            ])
            if overlapping_categories:
                raise exceptions.ValidationError("Las categorías tienen edades solapadas.")
