# -*- coding: utf-8 -*-
# from odoo import http


# class Recuperacion(http.Controller):
#     @http.route('/recuperacion/recuperacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recuperacion/recuperacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('recuperacion.listing', {
#             'root': '/recuperacion/recuperacion',
#             'objects': http.request.env['recuperacion.recuperacion'].search([]),
#         })

#     @http.route('/recuperacion/recuperacion/objects/<model("recuperacion.recuperacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recuperacion.object', {
#             'object': obj
#         })

