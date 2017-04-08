from flask_login import UserMixin
from xanadu import db
from werkzeug.security import generate_password_hash, check_password_hash

from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    nickname = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    items = db.relationship('Item', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.nickname)

    @property
    def password(self):
        raise AttributeError('password contains invalid characters')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    '''user loader callback function'''
    return User.query.get(int(user_id))


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    body = db.Column(db.String(200))
    accomplished = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<ListItem {}>'.format(self.title)
