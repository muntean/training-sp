# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class CustomerRentalWizard(models.TransientModel):
    _name = 'library.customer.rental.wizard'
    _description = 'Wizard: See the books rented by the customer'

    customer_id = fields.Many2one('res.partner', string='Customer')
    book_ids = fields.Many2many('library.book.copy')

    def get_customer_rentals(self):
        books_rented = self.env['library.rental'].search([('customer_id', '=', self.customer_id.id)])
        if bool(books_rented):
            self.book_ids = [(6, 0, books_rented.mapped('book_id').ids)]
        else:
            self.book_ids = [(5, 0, 0)]
        return {
            'name': _("Show the rented books"),
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': False,
            'res_model': self._name,
            'res_id': self.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'domain': '[]',
            'context': {},
        }
