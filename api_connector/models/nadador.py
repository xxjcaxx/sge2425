from odoo import models, fields

class Nadador(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date(string="Fecha de Nacimiento")
    age = fields.Integer(string="Edad", compute='_compute_age', store=True)
    categoria_id = fields.Many2one('recuperacion.categoria', string="Categoría")

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = datetime.today()
                birth_date = fields.Datetime.from_string(record.birth_date)
                record.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0

    @api.depends('age')
    def _compute_categoria(self):
        for record in self:
            categoria = self.env['recuperacion.categoria'].search([
                ('min_age', '<=', record.age),
                ('max_age', '>=', record.age)
            ], limit=1)  # Solo se asignará la primera categoría que coincida
            record.categoria_id = categoria
