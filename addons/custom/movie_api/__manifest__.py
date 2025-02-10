# -*- coding: utf-8 -*-
{
    'name': "Movie API REST",

    'summary': """
        Expone un endpoint REST '/api/top-movies' que entrega un Top 10 de películas
        
    """,

    'description': """
    
        - Expone un endpoint REST '/api/top_movies' que entrega un Top 10 de películas.
        - Basado en el módulo [Base Rest](https://github.com/OCA/rest-framework/tree/16.0/base_rest) de la OCA.
        
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
        'component',
        'base_rest',
        'movie_management',
    ],

    # always loaded
    'data': [
        #'data/data.xml',
    ],
    'license': 'AGPL-3',
}