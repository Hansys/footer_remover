# -*- coding: utf-8 -*-
from openerp import http

# class FooterRemover(http.Controller):
#     @http.route('/footer_remover/footer_remover/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/footer_remover/footer_remover/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('footer_remover.listing', {
#             'root': '/footer_remover/footer_remover',
#             'objects': http.request.env['footer_remover.footer_remover'].search([]),
#         })

#     @http.route('/footer_remover/footer_remover/objects/<model("footer_remover.footer_remover"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('footer_remover.object', {
#             'object': obj
#         })