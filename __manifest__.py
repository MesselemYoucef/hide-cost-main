# -*- coding: utf-8 -*-
{
    'name': 'Hide Cost',
    'version': '1.0',
    'summary': 'Hide the product cost',
    'sequence': -103,
    'description': """Hide the product cost from the 'Product Template', 'Product Variant', 'Sales Order and Quotation'""",
    'category': 'Productivity',
    'website': 'https://github.com/MesselemYoucef',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base',
        'sale',
        'sale_margin',
        'product',
        'pos_sale',
        'point_of_sale',
    ],
    'data': [
        'security/security.xml',
        'views/product_view.xml',
        'views/product_variant_view.xml',
        'views/sale_view.xml',
        'views/pos_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}