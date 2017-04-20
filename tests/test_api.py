"""
Test the API endpoints
"""
import json

from flask import url_for

from xanadu.models.bucketlist import BucketList
from tests import BaseTestCase


class APITestCase(BaseTestCase):
    """test the api endpoints"""

    def test_no_authentication(self):
        """test that an authenticated user is forbidden"""
        response = self.client.get(url_for('api.get_lists'),
                                   content_type='application/json')
        self.assertEqual(401, response.status_code)

    def test_create_list(self):
        """test an authenticated user can create a list"""
        response = self.client.post(
            url_for('api.get_lists'),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({
                                'title': 'test title',
                                'description': 'description of the list'}),
            content_type='application/json'
            )
        self.assertEqual(201, response.status_code)

    def test_read_list(self):
        """test authenticated user can read a list"""
        bucketlist = BucketList.query.filter_by(author=self.user2).first()
        response = self.client.get(
            url_for('api.get_one_list', id=bucketlist.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual(200, response.status_code)

    def test_update_list(self):
        """test authenticated user can update a list"""
        response = self.client.put(
            url_for('api.get_one_list', id=self.bucketlist2.id),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({'title': 'changed title'}),
            content_type='application/json'
            )
        self.assertEqual(200, response.status_code)

    def test_delete_list(self):
        """test authenticated user can delete a list"""
        response = self.client.delete(
            url_for('api.get_one_list', id=self.bucketlist3.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual('bucketlist deleted', json.loads(response.data)['message'])

    def test_create_item(self):
        """test an authenticated user can create a list item"""
        bucketlist = BucketList.query.filter_by(author=self.user).first()
        response = self.client.post(
            url_for('api.get_items', id=bucketlist.id),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps(
                {'title': 'item title', 'body': 'body of item'}),
            content_type='application/json'
            )
        self.assertEqual(201, response.status_code)

    def test_read_item(self):
        """test an authenticated user can read a list item"""
        response = self.client.get(
            url_for('api.get_item', id=self.item.bucketlist_id, item_id=self.item.id),
            headers=self.get_api_header(self.get_token()))
        self.assertEqual(200, response.status_code)

    def test_update_item(self):
        """test an authenticated user can update a list item"""
        response = self.client.put(
            url_for('api.get_item', id=self.item2.bucketlist_id, item_id=self.item2.id),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({'body': 'my body has been changed'}),
            content_type='application/json'
            )
        self.assertEqual(200, response.status_code)

    def test_delete_item(self):
        """test an authenticated user can delete a list item"""
        response = self.client.delete(
            url_for('api.get_item', id=self.item5.bucketlist_id, item_id=self.item5.id),
            headers=self.get_api_header(self.get_token())
            )
