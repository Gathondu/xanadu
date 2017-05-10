"""
Api endpoints for authentication
"""
import json
from flask import jsonify, g, url_for, request
from flask_httpauth import HTTPTokenAuth
from datetime import datetime

from xanadu import db
from xanadu.api.v1_0 import api
from xanadu.api.v1_0.errors import unauthorized, validation_error
from xanadu.exceptions import ValidationError
from xanadu.auth import auth
from xanadu.models.user import User

token_auth = HTTPTokenAuth(scheme='Token')


@auth.route('/verify', methods=['POST'])
def verify():
    token = json.loads(request.data).get('token')
    g.current_user = User.verify_auth_token(token)
    return jsonify(g.current_user is not None)


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.verify_auth_token(token)
    return g.current_user is not None


@token_auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.before_request
@token_auth.login_required
def before_request():
    pass


@auth.route('/login', methods=['POST'])
def login():
    """controller for login"""
    if request.method == 'POST':
        try:
            username = json.loads(request.data).get('username')
            password = json.loads(request.data).get('password')
            user = User.query.filter_by(email=username).first()
            if not user:
                return validation_error(ValidationError("User doesn't exist"))
            if not user.verify_password(password):
                return unauthorized('Invalid credentials')
            token = user.generate_auth_token()
            g.current_user = user
            return jsonify({'username': g.current_user.nickname,
                            'member_since': str(datetime.utcnow() - g.current_user.created_at),
                            'Location':
                            url_for(
                                'api.get_user',
                                id=g.current_user.id, _external=True),
                                'token': token.decode('ascii'),
                                'expiration': 3600})
        except ValidationError as e:
            return validation_error(e)


@auth.route('/register', methods=['POST'])
def register():
    """controller for registering new users"""
    if request.method == 'POST':
        try:
            user = User.create(json.loads(request.data))
            db.session.add(user)
            db.session.commit()
            return jsonify({'username': user.nickname,
                            'Location': url_for(
                                'api.get_user',
                                id=user.id, _external=True)}), 201
        except ValidationError as e:
            return validation_error(e)
