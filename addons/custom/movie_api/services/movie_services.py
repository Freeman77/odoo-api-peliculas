# -*- coding: utf-8 -*-

from odoo.addons.base_rest import restapi
from odoo.addons.component.core import Component


class MovieService(Component):
    _inherit = "base.rest.service"
    _name = "movie.service"
    _usage = "top_movies"
    _collection = "movie.api.services"
    _description = "Movie Service"


    @restapi.method([(["/"], "GET")], auth="public")
    def get(self):
        # get top 10 movies sorted by ranking
        movies = self.env["movie.movie"].sudo().search(
            [], order='ranking desc', limit=10
        )
        # return a list of movies in json format
        rows = []
        for movie in movies:
            rows.append(self._to_json(movie))
        return rows
    
    def _to_json(self, movie):
        return {
            "id": movie.id,
            "title": movie.name,
            "ranking": movie.ranking,
        }