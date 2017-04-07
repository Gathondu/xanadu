from flask import Flask
from flask_sqlalchemy import SQLAlchemy

xanadu = Flask(__name__)
xanadu.config.from_object('settings')
db = SQLAlchemy(xanadu)

# import views here to avoid circular references.
# views needs to import our app (xanadu)
from app import views, models
