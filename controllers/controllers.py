# -*- coding: utf-8 -*-
# from odoo import http


# class Spfcourse(http.Controller):
#     @http.route('/spfcourse/spfcourse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spfcourse/spfcourse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spfcourse.listing', {
#             'root': '/spfcourse/spfcourse',
#             'objects': http.request.env['spfcourse.spfcourse'].search([]),
#         })

#     @http.route('/spfcourse/spfcourse/objects/<model("spfcourse.spfcourse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spfcourse.object', {
#             'object': obj
#         })
