'''
Create a blueprint for the app so as to register its routes in the
app created by the factory function
'''
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors  # imported here to avoid circular dependencies
