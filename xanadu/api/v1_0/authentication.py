'''
Api endpoints for authentication
'''
from flask import jsonify, g, url_for, request
from flask_httpauth import HTTPBasicAuth

from . import api
from .errors import bad_request, unauthorized, forbidden
from ... import db
from ...models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    g.current_user = None
    if not email_or_token:
        bad_request('No credentials given')
    if not password:
        g.current_user = User.verify_auth_token(email_or_token)
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.before_request
@auth.login_required
def before_request():
    pass


@api.route('/auth/token')
@auth.login_required
def get_token():
    token = g.current_user.generate_auth_token()
    return jsonify({
        'token': token.decode('ascii'),
        'expiration': 3600
    })


@api.route('/auth/login')
@auth.login_required
def login():
    '''controller for login'''
    return jsonify({'username': g.current_user.nickname}, 200,
                   {'Location':
                    url_for(
                        'api.get_user', id=g.current_user.id, _external=True)})


@api.route('/auth/register', methods=['POST'])
def register():
    '''controller for registering new users'''
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.nickname}, 201, {
        'Location': url_for('api.get_user', id=user.id, _external=True)})
