# coding=utf-8

"""
Module URL
"""

from flask import Blueprint
from app.api.decorators import BaseDecorator
from modules.system.application_link.controller import ApplicationLinkControler

mod_application_link = Blueprint('applications', __name__, url_prefix='/applications')


class ApplicationLinkUrl():
    """Base ApplicationLink
    """

    @mod_application_link.route('/', methods=['GET'])
    @BaseDecorator.system
    def get_all(data):
        return ApplicationLinkControler(data=data).get_all()

    @mod_application_link.route('/', methods=['POST'])
    @BaseDecorator.system
    def post(data):
        return ApplicationLinkControler(data=data).post()

    @mod_application_link.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    def get(data, id):
        return ApplicationLinkControler(data=data).get(model_id=id)

    @mod_application_link.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    def put(data, id):
        return ApplicationLinkControler(data=data).put(model_id=id)
