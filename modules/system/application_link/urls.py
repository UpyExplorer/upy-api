# coding=utf-8

"""
Module URL
"""

from flask import Blueprint
from app.api.decorators import system, validate_token
from modules.system.application_link.controller import ApplicationLinkControler

mod_application_link = Blueprint('applications', __name__, url_prefix='/applications')


class ApplicationLinkUrl():
    """Base ApplicationLink
    """

    @mod_application_link.route('/', methods=['GET'])
    @validate_token
    @system
    def get_all(user, data):
        return ApplicationLinkControler(data=data).get_all()

    @mod_application_link.route('/', methods=['POST'])
    @validate_token
    @system
    def post(user, data):
        return ApplicationLinkControler(data=data).post()

    @mod_application_link.route('/<id>', methods=['GET'])
    @validate_token
    @system
    def get(user, data, id):
        return ApplicationLinkControler(data=data).get(model_id=id)

    @mod_application_link.route('/<id>', methods=['PUT'])
    @validate_token
    @system
    def put(user, data, id):
        return ApplicationLinkControler(data=data).put(model_id=id)
