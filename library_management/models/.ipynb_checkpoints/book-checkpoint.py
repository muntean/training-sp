# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Book(models.Model):

    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    editor = fields.Char(string='Editor')
    publisher = fields.Char(string='Publisher')
    edition_year = fields.Integer(string='Year of edition')
    isbn = fields.Char(string='ISBN', default="AAA1234567890")
    genre = fields.Selection(string='Genre',
                             selection=[('mystery', 'Mystery'),
                                        ('historical', 'Historical'),
                                        ('romance', 'Romance'),
                                        ('sci_fi', 'Science Fiction')])
    in_stock = fields.Boolean(default=True)
    notes = fields.Text()
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if len(self.isbn) != 13:
            raise ValidationError('The ISBN must be 13 characters long. Currently is: %s' % len(self.isbn))
