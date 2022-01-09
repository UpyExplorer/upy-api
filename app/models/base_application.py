# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
from app.base import BaseModel


class BaseApplication(BaseModel):

    __tablename__ = 'base_application'

    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(25), nullable=False) 
    key = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(100), nullable=False)
    image_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(1), nullable=False)
    Installed = db.Column(db.Integer, nullable=True)
    stars = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Boolean, nullable=True)

    def __init__(
        self,
        name,
        code,
        key,
        description,
        url,
        image_name,
        image_url,
        image,
        type,
        Installed,
        stars,
        status):

        self.name = name
        self.code = code
        self.key = key
        self.description = description
        self.url = url
        self.image_name = image_name
        self.image_url = image_url
        self.image = image
        self.type = type
        self.Installed = Installed
        self.stars = stars
        self.status = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class BaseApplicationSchema(ma.Schema):
    name = fields.Str()
    code = fields.Str()
    key = fields.Str()
    description = fields.Str()
    url = fields.Str()
    image_name = fields.Str()
    image_url = fields.Str()
    image = fields.Str()
    type = fields.Str()
    Installed = fields.Integer()
    stars = fields.Integer()
    status = fields.Boolean()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'name',
            'code',
            'key',
            'description',
            'url',
            'image_name',
            'image_url',
            'image',
            'type',
            'Installed',
            'stars',
            'status',
        )

base_schema = BaseApplicationSchema()
base_schemas = BaseApplicationSchema(many=True)