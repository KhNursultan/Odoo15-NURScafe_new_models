# -*- coding: utf-8 -*-
from odoo import http

# class ModuloVacio(http.Controller):
#     @http.route('/modulo_vacio/modulo_vacio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_vacio/modulo_vacio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_vacio.listing', {
#             'root': '/modulo_vacio/modulo_vacio',
#             'objects': http.request.env['modulo_vacio.modulo_vacio'].search([]),
#         })

#     @http.route('/modulo_vacio/modulo_vacio/objects/<model("modulo_vacio.modulo_vacio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_vacio.object', {
#             'object': obj
#         })