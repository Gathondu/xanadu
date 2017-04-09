'''
Create a blueprint for authentication related to user authentication
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
