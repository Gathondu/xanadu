from datetime import datetime
from flask import (render_template, redirect, session, url_for)

from . import main
from ..models import User, BucketList, Item


# route decorator comes from the blueprint
@main.route('/')
@main.route('/index')
def index():
    '''
    return the landing page view
    '''
    return render_template('index.html', title='Home')
