# coding=utf-8

"""
Runserver
"""

__all__ = ['BaseRunserver']

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

def page_not_found(self, error):
    """
    Render 404 error page
    """
    return render_template('404.html'), 404

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from modules.system.application_link.urls import mod_application_link
from modules.system.base_application.urls import mod_base_application

app.register_error_handler(404, page_not_found)
app.register_blueprint(mod_application_link)
app.register_blueprint(mod_base_application)

db.init_app(app)
