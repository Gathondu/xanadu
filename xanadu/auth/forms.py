from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, PasswordField, SubmitField,
                     ValidationError)
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        Required(), Length(1, 64), Regexp(
            '^[A-Za-z][A-Za-z0-9_.]*$', 0,
            'Names must only have letters, numbers, dots or underscores')])
    last_name = StringField('Last Name', validators=[
        Required(), Length(1, 64), Regexp(
            '^[A-Za-z][A-Za-z0-9_.]*$', 0,
            'Names must only have letters, numbers, dots or underscores')])
    # nickname = StringField('{}'.format(first_name.value+' '+last_name),
    #                        default=first_name+' '+last_name)
    nickname = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email(),
                                             Length(1, 64)])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='passwords must match.')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Username already in use.')
