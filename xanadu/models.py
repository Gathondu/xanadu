from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from xanadu import db
from .exceptions import ValidationError


# UserMixin has implementation of is_authenticated, is_active,
# is_anonymous and get_id()
class User(db.Model):
    '''user model'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    nickname = db.Column(
        db.String(60), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    bucketlist = db.relationship('BucketList', back_populates='author')
    items = db.relationship('Item', back_populates='author')

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

    def generate_auth_token(self, expiration=600):
        '''generate a token for user authentication valid for a minute'''
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        '''confirm token provided by the user'''
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def to_json(self):
        '''convert user to json serializable dictionary'''
        json_user = {
            'url': url_for('api.get_user', id=self.id, _external=True),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.nickname,
            'member_since': str(datetime.utcnow() - self.created_at),
            'bucketlists': url_for(
                'api.get_lists'),
            'list_count': len(self.bucketlist)
        }
        return json_user

    @staticmethod
    def from_json(user_json):
        '''get details from json object'''
        first_name = user_json.get('first_name')
        last_name = user_json.get('last_name')
        nickname = user_json.get('username')
        email = user_json.get('email')
        password = user_json.get('password')
        if not first_name or not last_name or not nickname\
                or not email or not password:
            raise ValidationError('post does not have valid data')
        if User.query.filter_by(nickname=nickname).first()\
                or User.query.filter_by(email=email).first():
            raise ValidationError('username and email already exist')
        user = User(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            email=email,
            password=password,
            created_at=datetime.utcnow()
        )
        return user


class BucketList(db.Model):
    '''bucketlist model'''
    __tablename__ = 'bucketlist'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True, nullable=False)
    description = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', back_populates='bucketlist')
    items = db.relationship('Item', back_populates='bucketlist')

    def __repr__(self):
        return '<BucketList {}>'.format(self.title)

    def to_json(self):
        '''convert list to json serializable dictionary'''
        json_list = {
            'url': url_for('api.get_one_list', id=self.id),
            'title': self.title,
            'description': self.description,
            'created_at': str(self.created_at),
            'author': url_for(
                'api.get_user', id=self.user_id, _external=True),
            'items': url_for('api.get_items', id=self.id, _external=True),
            'items_count': len(self.items)
        }
        return json_list

    @staticmethod
    def from_json(list_json):
        '''get details from json object'''
        title = list_json.get('title')
        description = list_json.get('description')
        author = list_json.get('author')
        if not title or not description:
            raise ValidationError('list details must all be provided')
        bucketlist = BucketList(
            title=title,
            description=description,
            created_at=datetime.utcnow()
        )
        return bucketlist


class Item(db.Model):
    '''item model'''
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True, nullable=False)
    body = db.Column(db.String(200))
    accomplished = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', back_populates='items')
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlist.id'))
    bucketlist = db.relationship('BucketList', back_populates='items')

    def __repr__(self):
        return '<ListItem {}>'.format(self.title)

    def to_json(self):
        '''convert list item to json serializable dictionary'''
        json_item = {
            'url': url_for(
                'api.get_item', id=self.bucketlist_id,
                item_id=self.id, _external=True),
            'title': self.title,
            'body': self.body,
            'accomplished': self.accomplished,
            'created_at': str(self.created_at),
            'author': url_for('api.get_user', id=self.user_id, _external=True),
            'bucketlist': url_for(
                'api.get_one_list', id=self.bucketlist_id, _external=True)
        }
        return json_item

    @staticmethod
    def from_json(item_json):
        '''save the json object from save into the models'''
        title = item_json.get('title')
        body = item_json.get('body')
        if not title or not body:
            raise ValidationError('item details cannot be empty')
        item = Item(
            title=title,
            body=body,
            created_at=datetime.utcnow()
        )
        return item
