# -*- coding: utf-8 -*-

"""
This module define all the api endpoints
"""

from sanic_restful_api import Api


def create_api(app):
    """
    Used when creating a Flask App to register the REST API and its resource
    """
    from app import resource

    api = Api(app)
    api.add_resource(resource.SomethingResource, '/api/something')
