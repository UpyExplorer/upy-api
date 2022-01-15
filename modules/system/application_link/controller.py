# coding=utf-8

"""
Module Controller
"""

from app.api.controllers import BaseController
from app.api.responses import BaseResponse
from app.models.application_link import ApplicationLink, base_schema, base_schemas


class ApplicationLinkControler(BaseController):
    """
    """
    def __init__(self, data=None):
        super().__init__(data)

        self.model_class = ApplicationLink
        self.base_schema = base_schema
        self.base_schemas = base_schemas
        self.response = BaseResponse()
