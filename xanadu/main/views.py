from datetime import datetime
from flask import (render_template, redirect, session, url_for)

from . import main
from ..models import User, Item


# route decorator comes from the blueprint
@main.route('/')
@main.route('/index')
def index():
    '''
    return the landing page view
    '''
    user = {'nickname': 'Dng'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }]
    return render_template('index.html', title='Home', user=user, posts=posts)
