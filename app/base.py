# coding=utf-8

"""
Model Base
"""

from app import db


class BaseModel(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
