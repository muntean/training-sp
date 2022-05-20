# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BookCopy(models.Model):
    _name = 'library.book.copy'
    _description = 'Book Copy'

    _inherits = {
        'library.book': 'book_id',
    }
    book_id = fields.Many2one(comodel_name='library.book',
                              required=True,
                              ondelete='cascade')

    reference = fields.Char(string='Internal Reference')

    rental_ids = fields.One2many(comodel_name='library.rental',
                                 inverse_name='book_id',
                                 string='Rentals')

    _sql_constraints = [
        ('reference_unique', 'UNIQUE(reference)', 'Each book reference must be unique.'),
    ]
