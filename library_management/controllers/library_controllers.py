# -*- coding: utf-8 -*-

from odoo import http


class Library(http.Controller):
    @http.route('/library/books/', auth='public', website=True)
    def books(self, **kw):
        books = http.request.env['library.book.copy'].search([('rental_ids', '=', False)])
        return http.request.render('library_management.books_website', {
            'books': books,
        })
