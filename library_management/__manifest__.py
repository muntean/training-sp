# -*- coding: utf-8 -*-

{
    'name': 'Library Management',

    'summary': """App to manage Books and Customers""",

    'description': """
        Library Management App to organize books and rentals, and for customers to check out books.
    """,

    'author': 'Stefana Pop',

    'website': 'https://www.information-systems.ro',

    'category': 'Management',
    'version': '1.0.0',

    'depends': ['base', 'web_map'],

    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/books_views.xml',
        'views/book_copy_views.xml',
        'views/rentals_views.xml',
        'wizard/customer_rental_wizard_view.xml',
    ],

    'demo': [
        'demo/library_demo.xml',
    ],
}