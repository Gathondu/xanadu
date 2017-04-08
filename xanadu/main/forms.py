from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)
