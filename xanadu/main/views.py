from datetime import datetime
from flask import (render_template, redirect, session, url_for)

from . import main
from .forms import LoginForm
from .. import db
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


@main.route('/login', methods=['GET', 'POST'])
def login():
    '''
    render the login page as a form
    '''
    form = LoginForm()
    if form.validate_on_submit():
        # url_for uses a namespace and allows for shortcuts hence .index
        # redirects across blueprints must use full format namespace.file
        return redirect(url_for('.index'))
    return render_template('login.html', title='Sign In',
                           form=form)
