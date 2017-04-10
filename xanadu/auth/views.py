'''
views for the authentication system
'''
from datetime import datetime
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User
from ..email import send_email

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


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''controller for registering new users'''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            nickname=form.nickname.data,
            email=form.email.data,
            password=form.password.data,
            created_at=datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(
            user.email, 'Confirm Your Account',
            'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

@auth.route('confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))
