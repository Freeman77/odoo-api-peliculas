# -*- coding: utf-8 -*-
{
    'name': "Movie Management",

    'summary': """
        Permite gestionar películas, incluyendo su nombre y ranking.
    """,

    'description': """
    
        - Permite gestionar películas, incluyendo su nombre y ranking.
        
    """,

    'author': "Pablo Ascencio",
    'website': "https://github.com/Freeman77",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Movie Management',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/movie_views.xml',
        'views/menuitems.xml',
    ],
    'license': 'AGPL-3',
}