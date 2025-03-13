# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class recuperacion(models.Model):
#     _name = 'recuperacion.recuperacion'
#     _description = 'recuperacion.recuperacion'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

