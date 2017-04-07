from flask import render_template, flash, redirect

from app import xanadu
from .forms import LoginForm


@xanadu.route('/')
@xanadu.route('/index')
def index():
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


@xanadu.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID={}, remember_me={}'.format(
            form.openid.data, str(form.remember_me.data)
        ))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form,
                           providers=xanadu.config['OPENID_PROVIDERS'])
