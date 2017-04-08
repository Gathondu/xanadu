'''
views for the authentication system
'''
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import LoginForm
from ..models import User, Item

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''controller for login view'''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    '''controller for logging user out'''
    logout_user()
    flash('You have Been Logged out.')
    return redirect(url_for('main.index'))
