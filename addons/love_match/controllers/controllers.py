# -*- coding: utf-8 -*-
# from odoo import http


# class LoveMatch(http.Controller):
#     @http.route('/love_match/love_match/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/love_match/love_match/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('love_match.listing', {
#             'root': '/love_match/love_match',
#             'objects': http.request.env['love_match.love_match'].search([]),
#         })

#     @http.route('/love_match/love_match/objects/<model("love_match.love_match"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('love_match.object', {
#             'object': obj
#         })
