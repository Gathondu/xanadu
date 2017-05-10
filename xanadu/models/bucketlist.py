from datetime import datetime
from flask import url_for
from flask_sqlalchemy import BaseQuery
from sqlalchemy_searchable import SearchQueryMixin, make_searchable
from sqlalchemy_utils import TSVectorType

from xanadu import db
from xanadu.exceptions import ValidationError

make_searchable()


class BucketListQuery(BaseQuery, SearchQueryMixin):
    pass


class BucketList(db.Model):
    """bucketlist model"""
    query_class = BucketListQuery
    __tablename__ = 'bucketlist'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(20), index=True, nullable=False)
    description = db.Column(db.Unicode(100), default='no description. add list description')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', back_populates='bucketlist')
    items = db.relationship('Item', back_populates='bucketlist')
    search_vector = db.Column(TSVectorType('title', 'description'))

    def __repr__(self):
        return '<BucketList {}>'.format(self.title)

    @staticmethod
    def create(list_json, author):
        """get details from json object"""
        title = list_json.get('title')
        description = list_json.get('description') or 'no description. add list description'
        if not title:
            raise ValidationError('list title must be provided')
        bucketlist = BucketList(
            author=author,
            title=title,
            description=description
            )
        return bucketlist

    def read(self):
        """convert list to json serializable dictionary"""
        json_list = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': url_for('api.get_one_list', id=self.id),
            'date_created': str(self.created_at),
            'date_modified': str(self.modified_at),
            'created_by': url_for(
                'api.get_user', id=self.user_id, _external=True),
            'items': url_for('api.get_items', id=self.id, _external=True),
            'items_count': len(self.items)
            }
        return json_list

    def update(self, list_json):
        for key in dict(list_json).keys():
            if key == 'title':
                self.title = dict(list_json)[key]
            if key == 'description':
                self.description = dict(list_json)[key]
        self.modified_at = datetime.utcnow()
        return self

    def authenticate_user(self, id):
        return id == self.user_id
