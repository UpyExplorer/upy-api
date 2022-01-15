# coding=utf-8

"""
Module API
"""

from upy_error import format_exception
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
        return self.response.get(method='method_not_allowed')

    def get(self, model_id):
        """Method GET
        Args:
            model_id (int): ID of the registry
        Returns:
            json: Returned from data
        """
        try:
            query = self.model_class.query.filter(self.model_class.id == model_id).first()
            if query:
                result = self.base_schema.dump(query)
                return self.response.get(method='successfully_fetched', result=result, limit=1, total=1)
        except Exception as error:
            print(format_exception(error))
            return self.response.get(method='server_error')

        return self.response.get(method='successfully_fetched', limit=1, total=0)

    def put(self, model_id):
        """Method PUT
        Args:
            model_id (int): ID of the registry
            data (dict, optional): Defaults to None.
        Returns:
            json: Returned from data
        """
        return self.response.get(method='method_not_allowed')

    def post(self):
        """Method POST
        Args:
            data (dict, optional): Defaults to None.
        Returns:
            json: Returned from data
        """
        return self.response.get(method='method_not_allowed')

    def delete(self, model_id):
        """Method DELETE
        Args:
            model_id (int): ID of the registry
        Returns:
            json: Returned from data
        """
        return self.response.get(method='method_not_allowed')
