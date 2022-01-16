# coding=utf-8

"""
Module URL
"""

from flask import Blueprint
from app.api.decorators import BaseDecorator
from modules.system.base_application.controller import BaseApplicationControler

mod_base_application = Blueprint('base_applications', __name__, url_prefix='/base_applications')


class ApplicationLinkUrl():
    """Base BaseApplication
    """

    @mod_base_application.route('/', methods=['GET'])
    @BaseDecorator.system
    def get_all(data):
        return BaseApplicationControler(data=data).get_all()

    @mod_base_application.route('/', methods=['POST'])
    @BaseDecorator.system
    def post(data):
        return BaseApplicationControler(data=data).post()

    @mod_base_application.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    def get(data, id):
        return BaseApplicationControler(data=data).get(model_id=id)

    @mod_base_application.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    def put(data, id):
        return BaseApplicationControler(data=data).put(model_id=id)
