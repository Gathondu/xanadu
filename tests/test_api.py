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
        """test authenticated user can read a list that belongs to them"""
        bucketlist = BucketList.query.filter_by(author=self.user).first()
        response = self.client.get(
            url_for('api.get_one_list', id=bucketlist.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual(200, response.status_code)

    def test_update_list(self):
        """test authenticated user can update a list that belongs to them"""
        response = self.client.put(
            url_for('api.get_one_list', id=self.bucketlist2.id),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({'title': 'changed title'}),
            content_type='application/json'
            )
        self.assertEqual(201, response.status_code)

    def test_delete_list(self):
        """test authenticated user can delete a list that belongs to them"""
        response = self.client.delete(
            url_for('api.get_one_list', id=self.bucketlist2.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual(204, response.status_code)

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
        """test an authenticated user can read a list item that belongs to them"""
        response = self.client.get(
            url_for('api.get_item', id=self.item.bucketlist_id, item_id=self.item.id),
            headers=self.get_api_header(self.get_token()))
        self.assertEqual(200, response.status_code)

    def test_update_item(self):
        """test an authenticated user can update a list item that belongs to them"""
        response = self.client.put(
            url_for('api.get_item', id=self.item2.bucketlist_id, item_id=self.item2.id),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({'body': 'my body has been changed'}),
            content_type='application/json'
            )
        self.assertEqual(201, response.status_code)

    def test_delete_item(self):
        """test an authenticated user can delete a list item that belongs to them"""
        response = self.client.delete(
            url_for('api.get_item', id=self.item3.bucketlist_id, item_id=self.item3.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual(204, response.status_code)

    # Edge cases
    def test_cannot_view_other_people_list(self):
        """test an authenticated user cannot view a list item that doesn't belongs to them"""
        bucketlist = BucketList.query.filter_by(author=self.user2).first()
        response = self.client.get(
            url_for('api.get_one_list', id=bucketlist.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual(403, response.status_code)

    def test_cannot_delete_other_people_list(self):
        """test an authenticated user cannot delete a list item that doesn't belongs to them"""
        response = self.client.delete(
            url_for('api.get_one_list', id=self.bucketlist3.id),
            headers=self.get_api_header(self.get_token())
            )
        self.assertEqual(403, response.status_code)

    def test_cannot_update_other_people_items(self):
        """test an authenticated user cannot update a list item that belongs to other users"""
        response = self.client.put(
            url_for('api.get_item', id=self.item4.bucketlist_id, item_id=self.item4.id),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({'body': 'my body has been changed'}),
            content_type='application/json'
            )
        self.assertEqual(403, response.status_code)

    def test_non_existent_resource(self):
        """Test that a non existent resource fails with error code 404"""
        response = self.client.get(
            url_for('api.get_item', id=self.item.bucketlist_id, item_id=40),
            headers=self.get_api_header(self.get_token()))
        self.assertEqual(404, response.status_code)

    def test_non_existent_user(self):
        """Test a non existent user"""
        response = self.client.get(
            url_for('api.get_one_list', id=50),
            headers=self.get_api_header(self.get_token()))
        self.assertEqual(404, response.status_code)
