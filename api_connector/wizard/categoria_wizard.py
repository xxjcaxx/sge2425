from odoo import models, fields, api, exceptions

class CategoriaWizard(models.TransientModel):
    _name = 'recuperacion.categoria.wizard'
    _description = 'Wizard para Crear Categorías'

    name = fields.Char(string="Nombre", required=True)
    min_age = fields.Integer(string="Edad Mínima", required=True)
    max_age = fields.Integer(string="Edad Máxima", required=True)

    def action_create_categoria(self):
        if self.min_age > self.max_age:
            raise exceptions.ValidationError("La edad mínima no puede ser mayor que la edad máxima.")

        overlapping_categories = self.env['recuperacion.categoria'].search([
            ('max_age', '>=', self.min_age),
            ('min_age', '<=', self.max_age)
        ])
        if overlapping_categories:
            raise exceptions.ValidationError("Las categorías tienen edades solapadas.")

        self.env['recuperacion.categoria'].create({
            'name': self.name,
            'min_age': self.min_age,
            'max_age': self.max_age,
        })
