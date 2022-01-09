# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
from app.base import BaseModel


class ApplicationLink(BaseModel):

    __tablename__ = 'application_link'

    base_application_id = db.Column(db.Integer, nullable=True)
    company_data_id = db.Column(db.Integer, nullable=True)
    creation_time = db.Column(db.DateTime, nullable=True)

    def __init__(
        self,
        base_application_id,
        company_data_id,
        creation_time=None):

        self.base_application_id = base_application_id
        self.company_data_id = company_data_id
        self.creation_time = creation_time

    def __repr__(self):
        return '<id %r>' % (self.id)

class ApplicationLinkSchema(ma.Schema):
    base_application_id = fields.Integer()
    company_data_id = fields.Integer()
    creation_time = fields.DateTime()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'base_application_id',
            'company_data_id',
            'creation_time'
        )

base_schema = ApplicationLinkSchema()
base_schemas = ApplicationLinkSchema(many=True)