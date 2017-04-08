'''
Create a blueprint for the app so as to register its routes in the
dynamically created app
'''
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors  # imported here to avoid circular dependencies
