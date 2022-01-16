# coding=utf-8

"""
Model Config
"""

from app import db, ma
from datetime import datetime
from marshmallow import fields, EXCLUDE
from app.base import BaseModel


class AdsLink(BaseModel):

    __tablename__ = 'ads_link'

    product_id = db.Column(db.Integer, nullable=True)
    application_link_id = db.Column(db.Integer, nullable=True)
    company_data_id = db.Column(db.Integer, nullable=True)
    creation_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    status = db.Column(db.Boolean, nullable=True)
    external_id = db.Column(db.String(50), nullable=False)

    def __init__(
        self,
        product_id,
        application_link_id,
        company_data_id,
        creation_time,
        status,
        external_id):

        self.product_id = product_id
        self.application_link_id = application_link_id
        self.company_data_id = company_data_id
        self.creation_time = creation_time
        self.status = status
        self.external_id = external_id

    def __repr__(self):
        return '<id %r>' % (self.id)

class AdsLinkSchema(ma.Schema):
    product_id = fields.Integer()
    application_link_id = fields.Integer()
    company_data_id = fields.Integer()
    creation_time = fields.DateTime()
    status = fields.Integer()
    external_id = fields.Integer()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'product_id',
            'application_link_id',
            'company_data_id',
            'creation_time',
            'status',
            'external_id'
        )

base_schema = AdsLinkSchema()
base_schemas = AdsLinkSchema(many=True)