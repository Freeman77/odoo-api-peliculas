# -*- coding: utf-8 -*-
{
    'name': "Movie Sync",

    'summary': """
        Obtiene información de películas desde el servicio externo [Random Data API - Películas]
    """,

    'description': """
    
        - Obtiene información de películas desde el servicio externo [Random Data API - Películas]
        (https://random-data-api.com/api/v3/projects/a2bebcc5-69e3-4b4e-b8c0-4a2f4306f0da), cada 1 minuto (requiere API key).
        
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
        'movie_management',
    ],

    # always loaded
    'data': [
        'data/movie_sync_data.xml',
    ],
    'license': 'AGPL-3',
}