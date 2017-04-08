'''
Initialize the application dynamically to allow for different instances
e.g test and development versions
'''

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from settings import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'  # can also be set to none or basic
# set endpoint for the login page and
# because the login route is inside a blueprint,
# it needs to be prefixed with the blueprint name
login_manager.login_view = 'auth.login'


def create_app(config_name):
    '''
    Factory function to create the app
    '''
    xanadu = Flask(__name__)
    xanadu.config.from_object(config[config_name])
    config[config_name].init_app(xanadu)
    bootstrap.init_app(xanadu)
    db.init_app(xanadu)
    login_manager.init_app(xanadu)

    # register blueprints to our app
    from .main import main as main_blueprint
    xanadu.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    xanadu.register_blueprint(auth_blueprint, url_prefix='/auth')

    return xanadu

