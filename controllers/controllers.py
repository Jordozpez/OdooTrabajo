# -*- coding: utf-8 -*-
# from odoo import http


# class ListaTarea(http.Controller):
#     @http.route('/lista_tarea/lista_tarea', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lista_tarea/lista_tarea/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lista_tarea.listing', {
#             'root': '/lista_tarea/lista_tarea',
#             'objects': http.request.env['lista_tarea.lista_tarea'].search([]),
#         })

#     @http.route('/lista_tarea/lista_tarea/objects/<model("lista_tarea.lista_tarea"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lista_tarea.object', {
#             'object': obj
#         })

