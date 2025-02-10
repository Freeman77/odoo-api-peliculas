# -*- coding: utf-8 -*-

import json
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Movie(models.Model):
    _inherit = 'movie.movie'
    
    
    def _get_movie_sync_params(self):
        """
        Get the Random Data API URL and KEY from the system parameters
        """
        conf = self.env['ir.config_parameter'].sudo()
        params_dict = {
            'api_url': conf.get_param('movie_sync.api_url'),
            'api_key': conf.get_param('movie_sync.api_key')
        }
        if params_dict['api_key'] == 'YOUR_API_KEY_HERE':
            _logger.error('Please set your API key in the system parameters')
        return params_dict
    
    
    def _cron_sync_movies_from_rda(self):
        """
        Call the Random Data API that responds with a single movie and store it in the database
        """
        api_params = self._get_movie_sync_params()
        headers = {
            'Content-Type': 'application/json',
            'charset': 'utf-8',
        }
        movie_data = {}
        try:
            response = requests.get(
                api_params['api_url'] + '?api_key=' + api_params['api_key'],
                headers=headers
            )
            response.raise_for_status()
            movie_data = response.json()
        except HTTPError as e:
            _logger.error(f'Error calling Random Data API: {e}')
            return False
        except ConnectionError as e:
            _logger.error(f'Error connecting to Random Data API: {e}')
            return False
        except Timeout as e:
            _logger.error(f'Timeout calling Random Data API: {e}')
            return False
        
        # Validate response data
        movie_title = movie_data.get('movie_title', False)
        movie_ranking = movie_data.get('ranking_movie', False)
        if not movie_title or not movie_ranking:
            _logger.error('Discarding movie data, missing title or ranking. {}'.format(movie_data))
            return False
        
        # Create a new movie record
        new_movie = self.env['movie.movie'].create({
            'name': movie_title,
            'ranking': int(movie_ranking)
        })
        _logger.info(f"New movie added: '{new_movie.name}' with ranking {new_movie.ranking}")
        return True
    
        
        
        