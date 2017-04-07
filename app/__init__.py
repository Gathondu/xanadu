from flask import Flask

app = Flask(__name__)

# import views here to avoid circular references.
# views needs to import our app
from app import views
