# -*- coding: utf-8 -*-

from odoo.addons.base_rest.controllers import main


class MoviePublicApiController(main.RestController):
    _root_path = "/api"
    _collection_name = "movie.api.services"
    _default_auth = "public"
