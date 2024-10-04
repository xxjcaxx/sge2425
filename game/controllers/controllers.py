# -*- coding: utf-8 -*-
# from odoo import http


# class Game(http.Controller):
#     @http.route('/game/game', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/game/game/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('game.listing', {
#             'root': '/game/game',
#             'objects': http.request.env['game.game'].search([]),
#         })

#     @http.route('/game/game/objects/<model("game.game"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('game.object', {
#             'object': obj
#         })

