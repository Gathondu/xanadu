'''
Initialize the application dynamically to allow for different instances
e.g test and development versions
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from settings import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    '''
    Initialize app with the desired settings
    '''
    xanadu = Flask(__name__)
    xanadu.config.from_object(config[config_name])
    config[config_name].init_app(xanadu)

    bootstrap.init_app(xanadu)
    db.init_app(xanadu)

    from .main import main as main_blueprint
    xanadu.register_blueprint(main_blueprint)  # register blueprint to our app

    return xanadu

