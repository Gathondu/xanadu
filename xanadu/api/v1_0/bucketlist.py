'''
Api endpoint for the bucketlist
'''
from flask import jsonify, request, url_for, g

from . import api
from ...models import User, BucketList


@api.route('/bucketlist/', methods=['GET'])
def get_list():
    user = User.query.filter_by(id=g.current_user.id).first()
    result = []
    for bucketlist in BucketList.query.filter_by(author=user).all():
        result.append(bucketlist.to_json)
    return jsonify(result)


