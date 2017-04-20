"""
customize the errors displayed
"""
from flask import jsonify

from xanadu.api.v1_0 import api
from xanadu.exceptions import ValidationError


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def not_found(message):
    response = jsonify({'error': 'resource not found', 'message': message})
    response.status_code = 404
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
