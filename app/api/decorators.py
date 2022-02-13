# coding=utf-8

"""
Module API
"""

import os
import json
from os.path import dirname

from flask import request
from functools import wraps

from app.api.responses import BaseResponse

BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))


def system(f):
    """Format the data
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        request_body = request.data.decode("UTF-8")
        request_params = request.args.to_dict(flat=False)

        if request_body:
            request_body = json.loads(request_body)
        else:
            request_body = {}

        data = {
            "body": request_body,
            "params": request_params,
            "args": request.view_args,
            "method": request.method,
            "request": request
        }
        
        return f(data, *args, **kwargs)
    
    return decorated

def validate_token(f):
    """Validate Token
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        header_token = request.headers.get('access_token')
        token = os.getenv("SECRET_KEY")
        
        if header_token == token:
            return f(True, *args, **kwargs)

        return BaseResponse().get(method='permission_denied')
    
    return decorated
