# coding=utf-8

"""
Module URL
"""

from flask import Blueprint
from app.api.decorators import BaseDecorator
from modules.system.ads_link.controller import AdsLinkControler

mod_ads_link = Blueprint('ads_links', __name__, url_prefix='/ads_links')


class AdsLinkUrl():
    """Base AdsLink
    """

    @mod_ads_link.route('/', methods=['GET'])
    @BaseDecorator.system
    def get_all(data):
        return AdsLinkControler(data=data).get_all()

    @mod_ads_link.route('/', methods=['POST'])
    @BaseDecorator.system
    def post(data):
        return AdsLinkControler(data=data).post()

    @mod_ads_link.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    def get(data, id):
        return AdsLinkControler(data=data).get(model_id=id)

    @mod_ads_link.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    def put(data, id):
        return AdsLinkControler(data=data).put(model_id=id)
