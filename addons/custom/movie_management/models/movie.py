# -*- coding: utf-8 -*-

from odoo import models, fields


class Movie(models.Model):
    _name = 'movie.movie'
    _description = 'Movie'
    
    name = fields.Char(string='Title', required=True)
    ranking = fields.Integer(string='Ranking')