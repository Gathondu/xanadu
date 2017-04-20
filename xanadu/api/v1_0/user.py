"""
API endpoints for the user
"""
from flask import jsonify, request, g

from xanadu import db
from xanadu.api.v1_0 import api
from xanadu.models.user import User


@api.route('/user/', methods=['GET', 'PUT'])
def get_user():
    user = User.query.filter_by(id=g.current_user.id).first()
    if request.method == 'GET':
        return jsonify(user.read())
    elif request.method == 'PUT':
        user = user.update(request.json)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.read())
