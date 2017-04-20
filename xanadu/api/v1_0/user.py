"""
API endpoints for the user
"""
from flask import jsonify, request, g

from xanadu import db
from xanadu.api.v1_0 import api
from xanadu.models.user import User


@api.route('/user/', methods=['GET', 'PUT'])
def get_user():
    user = User.query.get_or_404(g.current_user.id)
    if request.method == 'GET':
        return jsonify(user.read())
    if request.method == 'PUT':
        user = user.update(request.json)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.read())
