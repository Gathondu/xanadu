"""
Api endpoints for authentication
"""
from flask import jsonify, g, url_for, request
from flask_httpauth import HTTPTokenAuth

from xanadu import db
from xanadu.api.v1_0 import api
from xanadu.api.v1_0.errors import unauthorized
from xanadu.auth import auth
from xanadu.models.user import User

token_auth = HTTPTokenAuth(scheme='Token')


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
        username = request.json.get('username')
        password = request.json.get('password')
        user = User.query.filter_by(email=username).first()
        expiry = None
        if not user and not user.verify_password(password):
            return unauthorized('Invalid credentials')
        if 'expiry' in dict(request.json).keys():
            expiry = dict(request.json)['expiry']
            token = user.generate_auth_token(expiration=expiry)
        token = user.generate_auth_token()
        g.current_user = user
        return jsonify({'username': g.current_user.nickname,
                       'Location':
                        url_for(
                               'api.get_user', id=g.current_user.id, _external=True)},
                       {
                           'token': token.decode('ascii'),
                           'expiration': 3600 if not expiry else expiry})


@auth.route('/register', methods=['POST'])
def register():
    """controller for registering new users"""
    if request.method == 'POST':
        user = User.create(request.json)
        db.session.add(user)
        db.session.commit()
        return jsonify({'username': user.nickname,
                        'Location': url_for('api.get_user', id=user.id, _external=True)}), 201
