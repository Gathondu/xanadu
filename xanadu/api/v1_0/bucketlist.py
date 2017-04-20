"""
Api endpoint for the bucketlist
"""
from flask import current_app, g, jsonify, request, url_for

from xanadu.api.v1_0 import api
from xanadu import db
from xanadu.models.user import User
from xanadu.models.bucketlist import BucketList


@api.route('/bucketlist/', methods=['GET', 'POST'])
def get_lists():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', current_app.config['LIST_PER_PAGE'], type=int)
        search = request.args.get('q', None, type=str)
        if limit > 100:
            limit = current_app.config['MAX_RESULTS']
        user = User.query.filter_by(id=g.current_user.id).first()
        if search:
            paginate = BucketList.query.search(search).filter_by(author=user).paginate(
                page, limit, error_out=False)
        else:
            paginate = BucketList.query.filter_by(author=user).paginate(
                page, limit, error_out=False)
        bucketlists = paginate.items
        previous = None
        if paginate.has_prev:
            previous = url_for('api.get_lists', page=page-1, limit=limit, _external=True)
        next = None
        if paginate.has_next:
            next = url_for('api.get_lists', page=page+1, limit=limit, _external=True)
        return jsonify({
            'bucketlists': [bucket.read() for bucket in bucketlists],
            'previous': previous,
            'next': next,
            'count': paginate.total
            })
    if request.method == 'POST':
        bucketlist = BucketList.create(request.json, g.current_user)
        db.session.add(bucketlist)
        db.session.commit()
        return jsonify({'title': bucketlist.title,
                        'location': url_for(
                                    'api.get_one_list', id=bucketlist.id, _external=True)}), 201


@api.route('/bucketlist/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_one_list(id):
    bucketlist = BucketList.query.filter_by(id=id).first()
    if request.method == 'GET':
        return jsonify(bucketlist.read())
    if request.method == 'PUT':
        bucketlist = bucketlist.update(request.json)
        db.session.add(bucketlist)
        db.session.commit()
        return jsonify(bucketlist.read())
    if request.method == 'DELETE':
        db.session.delete(bucketlist)
        db.session.commit()
        return jsonify({'message': 'bucketlist deleted'})

