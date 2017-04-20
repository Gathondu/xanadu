"""
Create a blueprint for this version of api endpoint to be consumed by
the factory function
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from xanadu.api.v1_0 import item, user, bucketlist
