import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = os.getenv('SECRET_KEY', None)


# if you prefer to use sqlite alchemy no need to create xanadu's database
# before hand. This will be used
sqlite_database = 'sqlite:///' + os.path.join(BASE_DIR, 'xanadu.db')

SQLALCHEMY_DATABASE_URI = os.getenv('XANADU_DATABASE_URL', sqlite_database)
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')
SQLALCHEMY_TRACK_MODIFICATIONS = True
