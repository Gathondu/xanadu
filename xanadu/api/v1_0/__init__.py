'''
Create a blueprint for this version of api endpoint to be consumed by
the factory function
'''
from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, item, user, bucketlist
