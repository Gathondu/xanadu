import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Settings for the app
    """
    DEBUG = True
    ITEMS_PER_LIST = 10
    LIST_PER_PAGE = 20
    MAX_RESULTS = 100
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        """Initialize the app"""
        pass


class DevelopmentConfig(Config):
    """
    Development settings
    """
    # if you prefer to use sqlite alchemy no need to create xanadu's database
    # before hand. This will be used
    sqlite_database = 'sqlite:///' + os.path.join(BASE_DIR, 'xanadu.sqlite')
    SQLALCHEMY_DATABASE_URI = os.getenv('XANADU_DATABASE_URL', sqlite_database)


class TestingConfig(Config):
    """
    Testing settings
    """
    TESTING = True
    test_database = 'sqlite:///' + os.path.join(BASE_DIR, 'xanadu-test.sqlite')
    SQLALCHEMY_DATABASE_URI = os.getenv('XANADU_TEST_DATABASE_URL',
                                        test_database)


class ProductionConfig(Config):
    """
    Production settings
    """
    DEBUG = False
    database = 'sqlite:///' + os.path.join(BASE_DIR, 'xanadu.sqlite')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', database)


class HerokuConfig(ProductionConfig):
    """Heroku settings"""
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
    }
