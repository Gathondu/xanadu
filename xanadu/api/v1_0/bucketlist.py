'''
Api endpoint for the bucketlist
'''
from flask import jsonify, request, url_for, g

from . import api
from ... import db
from ...models import User, BucketList, Item


@api.route('/bucketlist/', methods=['GET', 'POST'])
def get_lists():
    if request.method == 'GET':
        user = User.query.filter_by(id=g.current_user.id).first()
        result = []
        for bucketlist in BucketList.query.filter_by(author=user).all():
            result.append(bucketlist.to_json())
        return jsonify(result)
    if request.method == 'POST':
        bucketlist = BucketList.from_json(request.json)
        bucketlist.author = g.current_user
        db.session.add(bucketlist)
        db.session.commit()
        return jsonify({'title': bucketlist.title}, 201, {
            'Location': url_for(
                'api.get_one_list', id=bucketlist.id, _external=True)})


@api.route('/bucketlist/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_one_list(id):
    bucketlist = BucketList.query.filter_by(id=id).first()
    if request.method == 'GET':
        return jsonify(bucketlist.to_json())
    if request.method == 'PUT':
        for key in dict(request.json).keys():
            if key == 'title':
                bucketlist.title = dict(request.json)[key]
            if key == 'description':
                bucketlist.description = dict(request.json)[key]
        db.session.add(bucketlist)
        db.session.commit()
        return jsonify({'title': bucketlist.title}, 200, {
            'Location': request.url})
    if request.method == 'DELETE':
        db.session.delete(bucketlist)
        db.session.commit()
        return jsonify({'message': 'bucketlist deleted'}, 200)

