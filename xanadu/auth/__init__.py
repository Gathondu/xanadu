"""
Authentication blueprint
"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from xanadu.auth import authentication
