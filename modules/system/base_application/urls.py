# coding=utf-8

"""
Module URL
"""

from flask import Blueprint
from app.api.decorators import system, validate_token
from modules.system.base_application.controller import BaseApplicationControler

mod_base_application = Blueprint('base_applications', __name__, url_prefix='/base_applications')


class ApplicationLinkUrl():
    """Base BaseApplication
    """

    @mod_base_application.route('/', methods=['GET'])
    @validate_token
    @system
    def get_all(user, data):
        return BaseApplicationControler(data=data).get_all()

    @mod_base_application.route('/', methods=['POST'])
    @validate_token
    @system
    def post(user, data):
        return BaseApplicationControler(data=data).post()

    @mod_base_application.route('/<id>', methods=['GET'])
    @validate_token
    @system
    def get(user, data, id):
        return BaseApplicationControler(data=data).get(model_id=id)

    @mod_base_application.route('/<id>', methods=['PUT'])
    @validate_token
    @system
    def put(user, data, id):
        return BaseApplicationControler(data=data).put(model_id=id)
