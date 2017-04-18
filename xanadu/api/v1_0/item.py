"""
API endpoint for the item
"""
from flask import current_app, jsonify, request, g, url_for

from xanadu.api.v1_0 import api
from xanadu import db
from xanadu.models.item import Item
from xanadu.models.bucketlist import BucketList


@api.route('/bucketlist/<int:id>/items/', methods=['GET', 'POST'])
def get_items(id):
    page = request.args.get('page', 1, type=int)
    bucketlist = BucketList.query.get_or_404(id)
    if request.method == 'GET':
        paginate = Item.query.filter_by(bucketlist_id=id).paginate(
            page, current_app.config['ITEMS_PER_LIST'], error_out=False
            )
        items = paginate.items
        previous = None
        if paginate.has_prev:
            previous = url_for('api.get_items', id=id, page=page-1, _external=True)
        next = None
        if paginate.has_next:
            next  = url_for('api.get_items', id=id, page=page+1, _external=True)
        return jsonify({
            'items': [item.read() for item in items],
            'previous': previous,
            'next': next,
            'count': paginate.total
            })
    if request.method == 'POST':
        item = Item.create(request.json, g.current_user, bucketlist)
        db.session.add(item)
        db.session.commit()
        return jsonify({'title': item.title,
                        'location': url_for('api.get_item', id=item.bucketlist_id,
                                            item_id=item.id, _external=True)}), 201


@api.route('/bucketlist/<int:id>/items/<int:item_id>',
           methods=['GET', 'PUT', 'DELETE'])
def get_item(id, item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'GET':
        return jsonify(item.read())
    if request.method == 'PUT':
        item = item.update(request.json)
        db.session.add(item)
        db.session.commit()
        return jsonify({'title': item.title,
                        'location': request.url})
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'item deleted'})
