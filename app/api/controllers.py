# coding=utf-8

"""
Module API
"""

from app.api.responses import BaseResponse


class BaseController(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, data=None):
        """Constructor
        Args:
            data (dict, optional): Defaults to None.
        """
        self.data = data
        self.params = {}
        self.model_class = None
        self.base_schema = None
        self.base_schemas = None
        self.response = BaseResponse()

    def get_all(self):
        """Get all registries
        Returns:
            json: Returned from data
        """
        return self.response.get(method='successfully_fetched')

    def get(self, model_id):
        """Method GET
        Args:
            model_id (int): ID of the registry
        Returns:
            json: Returned from data
        """
        return self.response.get(method='successfully_fetched')

    def put(self, model_id):
        """Method PUT
        Args:
            model_id (int): ID of the registry
            data (dict, optional): Defaults to None.
        Returns:
            json: Returned from data
        """
        return self.response.get(method='successfully_fetched')

    def post(self):
        """Method POST
        Args:
            data (dict, optional): Defaults to None.
        Returns:
            json: Returned from data
        """
        return self.response.get(method='successfully_fetched')

    def delete(self, model_id):
        """Method DELETE
        Args:
            model_id (int): ID of the registry
        Returns:
            json: Returned from data
        """
        return self.response.get(method='method_not_allowed')
