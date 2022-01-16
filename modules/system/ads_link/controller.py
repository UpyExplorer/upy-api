# coding=utf-8

"""
Module Controller
"""

from app.api.controllers import BaseController
from app.api.responses import BaseResponse
from app.models.ads_link import AdsLink, base_schema, base_schemas


class AdsLinkControler(BaseController):
    """
    """
    def __init__(self, data=None):
        super().__init__(data)

        self.model_class = AdsLink
        self.base_schema = base_schema
        self.base_schemas = base_schemas
        self.response = BaseResponse()
