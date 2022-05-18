# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Book Rental History'
    
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')

    book_id = fields.Many2one(comodel_name='library.book.copy',
                              string='Book',
                              ondelete='cascade',
                              required=True)
    #name = fields.Char(comodel_name='library.book', related='book_id.name', string='Title')