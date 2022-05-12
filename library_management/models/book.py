# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):

    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    editor = fields.Char(string='Editor')
    publisher = fields.Char(string='Publisher')
    edition_year = fields.Integer(string='Year of edition')
    isbn = fields.Char(string='ISBN')
    genre = fields.Selection(string='Genre',
                             selection=[('mystery', 'Mystery'),
                                        ('historical', 'Historical'),
                                        ('romance', 'Romance'),
                                        ('sci_fi', 'Science Fiction')])
    in_stock = fields.Boolean(default=True)
    notes = fields.Text()
