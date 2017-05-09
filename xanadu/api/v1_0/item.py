"""
API endpoint for the item
"""
from flask import current_app, jsonify, request, g, url_for

from xanadu.api.v1_0 import api
from xanadu.api.v1_0.errors import not_found, forbidden
from xanadu import db
from xanadu.models.item import Item
from xanadu.models.bucketlist import BucketList


@api.route('/bucketlist/<int:id>/items/', methods=['GET', 'POST'])
def get_items(id):
    bucketlist = BucketList.query.filter_by(id=id).first()
    if not bucketlist:
        return not_found('user id {} does not exist'.format(id))
    elif request.method == 'GET':
        if not bucketlist.authenticate_user(g.current_user.id):
            return forbidden('resource does not belong to user with id {}'.format(g.current_user.id))
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', current_app.config['ITEMS_PER_LIST'], type=int)
        search = request.args.get('q', None, type=str)
        if limit > 100:
            limit = current_app.config['MAX_RESULTS']
        if search:
            paginate = Item.query.search(search).filter_by(bucketlist_id=id).paginate(
                page, limit, error_out=False
                )
        else:
            paginate = Item.query.filter_by(bucketlist_id=id).paginate(
                page, limit, error_out=False
                )
        items = paginate.items
        previous = None
        if paginate.has_prev:
            previous = url_for('api.get_items', id=id, page=page-1, limit=limit, _external=True)
        next = None
        if paginate.has_next:
            next  = url_for('api.get_items', id=id, page=page+1, limit=limit, _external=True)
        return jsonify({
            'items': [item.read() for item in items],
            'previous': previous,
            'next': next,
            'count': paginate.total,
            'bucketlist_title': bucketlist.title,
            'bucketlist_created': bucketlist.created_at,
            'bucketlist_modified': bucketlist.modified_at,
            'bucketlist_description': bucketlist.description
            })
    elif request.method == 'POST':
        item = Item.create(request.json, g.current_user, bucketlist)
        db.session.add(item)
        db.session.commit()
        return jsonify(item.read()), 201


@api.route('/bucketlist/<int:id>/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def get_item(id, item_id):
    item = Item.query.get_or_404(item_id)
    if not item.authenticate_user(g.current_user.id):
        return forbidden('resource does not belong to user with id {}'.format(g.current_user.id))
    elif request.method == 'GET':
        return jsonify(item.read())
    elif request.method == 'PUT':
        item = item.update(request.json)
        db.session.add(item)
        db.session.commit()
        return jsonify(item.read()), 201
    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify(), 204
