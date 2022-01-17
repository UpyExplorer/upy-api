# coding=utf-8

"""
Module URL
"""

from flask import Blueprint
from app.api.decorators import system, validate_token
from modules.system.ads_link.controller import AdsLinkControler

mod_ads_link = Blueprint('ads_links', __name__, url_prefix='/ads_links')


class AdsLinkUrl():
    """Base AdsLink
    """

    @mod_ads_link.route('/', methods=['GET'])
    @validate_token
    @system
    def get_all(user, data):
        return AdsLinkControler(data=data).get_all()

    @mod_ads_link.route('/', methods=['POST'])
    @validate_token
    @system
    def post(user, data):
        return AdsLinkControler(data=data).post()

    @mod_ads_link.route('/<id>', methods=['GET'])
    @validate_token
    @system
    def get(user, data, id):
        return AdsLinkControler(data=data).get(model_id=id)

    @mod_ads_link.route('/<id>', methods=['PUT'])
    @validate_token
    @system
    def put(user, data, id):
        return AdsLinkControler(data=data).put(model_id=id)
