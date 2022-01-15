# coding=utf-8

"""
Module API
"""

from flask import jsonify


class BaseResponse():
    """Base View to Response common to all Webservices.
    """

    def __init__(self):
        """Constructor
        """

        self.data_return = {
            "successfully_fetched": {
                "status": 200,
                "status_message": "success",
                "message": "Successful Fetched"
                },
            "successfully_created": {
                "status": 201,
                "status_message": "success",
                "message": "Successful Created"
                },
            "server_error": {
                "status": 500,
                "status_message": "fail",
                "message": "Internal Server Error"
                },
            "user_dont_exist": {
                "status": 404,
                "status_message": "fail",
                "message": "User Don't Exist"
                },
            "company_data_is_missing": {
                "status": 401,
                "status_message": "fail",
                "message": "BaseCustomer is Missing"
                },
            "token_is_missing": {
                "status": 401,
                "status_message": "fail",
                "message": "Token is Missing"
                },
            "token_is_invalid": {
                "status": 401,
                "status_message": "fail",
                "message": "Token is Invalid"
                },
            "permission_denied": {
                "status": 401,
                "status_message": "fail",
                "message": "Permission Denied"
                },
            "invalid_data": {
                "status": 422,
                "status_message": "fail",
                "message": "Unprocessable Entity"
                },
            "data_not_found": {
                "status": 404,
                "status_message": "fail",
                "message": "Not Found"
                },
            "method_not_allowed": {
                "status": 405,
                "status_message": "fail",
                "message": "Method Not Allowed"
                },
            "method": {
                "status": 200,
                "status_message": "ok",
                "message": "Method"
                },
        }

    def get(self, method, limit=None, total=None, result=None):
        """API response
        Args:
            method (str): Method Name.
            limit (int, optional): Defaults to None.
            quantity (int, optional): Defaults to None.
            result (dict, optional): Defaults to None.
        Returns:
            [jsonify]: Data
        """
        return jsonify(
            {
                "data": {
                    "status_message": self.data_return[method]['status_message'],
                    "message": self.data_return[method]['message'],
                    "limit": limit,
                    "total": total
                },
                "result": result
            }
        ), self.data_return[method]['status']
