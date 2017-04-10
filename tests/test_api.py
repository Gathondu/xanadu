'''
Test the API endpoints
'''
import json

from base64 import b64encode
from flask import url_for
from unittest import skip

from xanadu.models import User
from tests import BaseTestCase


class APITestCase(BaseTestCase):
    '''test the api endpoints'''
    def get_api_header(self, username, password):
        '''helper function to return the header that
           will be displayed with the API endpoints'''
        return {
            'Authorization':
                'Basic ' + b64encode(
                    (username +
                     ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_user_login(self):
        '''test that a user can log in'''
        user = User.query.filter_by(nickname='dng').first()
        response = self.client.post(
            url_for('api.login'),
            data={
                json.dumps({
                    'email': user.email,
                    'password': user.password_hash})})
        self.assertEqual(200, response.status_code)

    def test_no_authentication(self):
        '''test that an authenticated user is forbidden'''
        response = self.client.get(url_for('api.get_item'),
                                   content_type='application/json')
        self.assertEqual(401, response.status_code)

    def test_create_list(self):
        '''test an authenticated user can create a list item'''
        response = self.client.post(
            url_for('api.new_list'),
            headers=self.get_api_header('thundoss@gmail.com', 'denno'),
            data=json.dumps({'title': 'description of the list'})
        )
        self.assertEqual(201, response.status_code)
        url = response.headers.get('Location')
        self.assertIsNotNone(url)
        # test that the new item exists
        response = self.client.get(
            url,
            headers=self.get_api_header('thundoss@gmail.com', 'denno'))
        self.assertEqual(200, response.status_code)
        # also assert for the contents
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(url, json_response['url'])
        self.assertEqual('description of the list', json_response['body'])
        self.assertEqual(
            '<p>description of the list</p>',
            json_response['body_html'])

    def test_create_item(self):
        '''test an authenticated user can create a list item'''
        response = self.client.post(
            url_for('api.new_item'),
            headers=self.get_api_header('thundoss@gmail.com', 'denno'),
            data=json.dumps({'title of item': 'body of the item'})
        )
        self.assertEqual(201, response.status_code)
        url = response.headers.get('Location')
        self.assertIsNotNone(url)

        # test that the new item exists
        response = self.client.get(
            url,
            headers=self.get_api_header('thundoss@gmail.com', 'denno'))
        self.assertEqual(200, response.status_code)

        # also assert for the contents
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(url, json_response['url'])
        self.assertEqual('body of the item', json_response['body'])
        self.assertEqual(
            '<p>body of the item</p>',
            json_response['body_html'])
