# coding=utf-8

"""
Module Controller
"""

from app.api.controllers import BaseController
from app.api.responses import BaseResponse
from app.models.base_application import BaseApplication, base_schema, base_schemas


class BaseApplicationControler(BaseController):
    """
    """
    def __init__(self, data=None):
        super().__init__(data)

        self.model_class = BaseApplication
        self.base_schema = base_schema
        self.base_schemas = base_schemas
        self.response = BaseResponse()
