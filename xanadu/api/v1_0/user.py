'''
API endpoints for the user
'''
from flask import jsonify, g

from . import api
from ...models import User, BucketList, Item


@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/users/', methods=['GET'])
def get_users():
    result = []
    for user in User.query.all():
        result.append(user.to_json())
    return jsonify(result)
