'''
API endpoint for the item
'''
from flask import jsonify, request, g, url_for

from . import api
from ... import db
from ...models import Item, BucketList


@api.route('/bucketlist/<int:id>/items/', methods=['GET', 'POST'])
def get_items(id):
    bucketlist = BucketList.query.get_or_404(id)
    if request.method == 'GET':
        items = bucketlist.items
        return jsonify([item.to_json() for item in items])
    if request.method == 'POST':
        item = Item.from_json(request.json)
        item.author = g.current_user
        item.bucketlist = bucketlist
        db.session.add(item)
        db.session.commit()
        return jsonify({'title': item.title}, 201, {
            'Location': url_for('api.get_item', id=item.id, _external=True)})


@api.route('/bucketlist/<int:id>/items/<int:item_id>',
           methods=['GET', 'PUT', 'DELETE'])
def get_item(id, item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'GET':
        return jsonify(item.to_json())
    if request.method == 'PUT':
        for key in dict(request.json).keys():
            if key == 'title':
                item.title = dict(request.json)[key]
            if key == 'body':
                item.body = dict(request.json)[key]
        db.session.add(item)
        db.session.commit()
        return jsonify({'title': item.title}, 200, {
            'Location': request.url})
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'item deleted'}, 200)
