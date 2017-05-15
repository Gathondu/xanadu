"""
Initialize the application dynamically to allow for different instances
e.g test and development versions
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import config

db = SQLAlchemy()


def create_app(config_name):
    """
    Factory function to create the xanadu
    """
    xanadu = Flask(__name__)
    xanadu.config.from_object(config[config_name])
    config[config_name].init_app(xanadu)
    db.init_app(xanadu)

    from xanadu.auth import auth
    xanadu.register_blueprint(auth, url_prefix='/auth')
    from xanadu.api.v1_0 import api as api_v1_0_blueprint
    xanadu.register_blueprint(api_v1_0_blueprint, url_prefix='/api/v1.0')

    return xanadu
