from datetime import datetime
from flask import url_for

from xanadu import db
from xanadu.exceptions import ValidationError


class Item(db.Model):
    """item model"""
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True, nullable=False)
    body = db.Column(db.Text())
    accomplished = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', back_populates='items')
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlist.id'))
    bucketlist = db.relationship('BucketList', back_populates='items')

    def __repr__(self):
        return '<ListItem {}>'.format(self.title)

    @staticmethod
    def create(item_json, author, bucketlist):
        """save the json object from save into the models"""
        title = item_json.get('title')
        body = item_json.get('body')
        if not title or not body:
            raise ValidationError('item details cannot be empty')
        item = Item(
            author=author,
            bucketlist=bucketlist,
            title=title,
            body=body,
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow()
            )
        return item

    def read(self):
        """convert list item to json serializable dictionary"""
        json_item = {
            'id': self.id,
            'location': url_for(
                'api.get_item', id=self.bucketlist_id,
                item_id=self.id, _external=True),
            'title': self.title,
            'accomplished': self.accomplished,
            'date_created': str(self.created_at),
            'date_modified': str(self.modified_at),
            'done': self.accomplished
            }
        return json_item

    def update(self, item_json):
        for key in dict(item_json).keys():
            if key == 'title':
                self.title = dict(item_json)[key]
            if key == 'body':
                self.body = dict(item_json)[key]
        self.modified_at = datetime.utcnow()
        return self
