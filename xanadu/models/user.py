from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from xanadu import db
from xanadu.exceptions import ValidationError


# UserMixin has implementation of is_authenticated, is_active,
# is_anonymous and get_id()
class User(db.Model):
    """user model"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    nickname = db.Column(
        db.String(60), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)
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

    def generate_auth_token(self, expiration=3600):
        """generate a token for user authentication valid for a minute"""
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        """confirm token provided by the user"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    @staticmethod
    def create(user_json):
        """get details from json object"""
        first_name = user_json.get('first_name')
        last_name = user_json.get('last_name')
        nickname = user_json.get('username')
        email = user_json.get('email')
        password = user_json.get('password')
        if not first_name or not last_name or not nickname \
                or not email or not password:
            raise ValidationError('post does not have valid data')
        if User.query.filter_by(nickname=nickname).first() \
                or User.query.filter_by(email=email).first():
            raise ValidationError('username and email already exist')
        user = User(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            email=email,
            password=password,
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow()
            )
        return user

    def read(self):
        """convert user to json serializable dictionary"""
        json_user = {
            'location': url_for('api.get_user', id=self.id, _external=True),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.nickname,
            'member_since': str(datetime.utcnow() - self.created_at),
            'date_modified': str(self.modified_at),
            'bucketlists': url_for(
                'api.get_lists'),
            'list_count': len(self.bucketlist)
            }
        return json_user

    def update(self, user_json):
        """Update user details"""
        for key in dict(user_json).keys():
            if key == 'username':
                key = dict(user_json)[key]
                if User.query.filter_by(nickname=key).first():
                    raise ValidationError('username already exist')
                self.nickname = key
            if key == 'email':
                key = dict(user_json)[key]
                if User.query.filter_by(email=key).first():
                    raise ValidationError('email already exist')
                self.email = key
            if key == 'password':
                key = dict(user_json)[key]
                self.password = key
            if key == 'first_name':
                key = dict(user_json)[key]
                self.first_name = key
            if key == 'last_name':
                key = dict(user_json)[key]
                self.last_name = key
        self.modified_at = datetime.utcnow()
        return self
