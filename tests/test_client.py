"""
Tests for the client
"""
import json

from flask import url_for

from xanadu.exceptions import ValidationError
from tests import BaseTestCase


class ClientTestCase(BaseTestCase):
    """Test the client instance"""

    def test_register(self):
        """test the registration of a new user"""
        response = self.client.post(
            url_for('auth.register'),
            data=json.dumps({
                'first_name': 'danson',
                'last_name': 'miti',
                'username': 'miti',
                'email': 'example@gmail.com',
                'password': 'dan'
                }),
            content_type='application/json')
        self.assertEqual(201, response.status_code)

    def test_login(self):
        """test the logging in of a registered user"""
        response = self.client.post(
            url_for('auth.login'),
            data=json.dumps({
                'username': 'thundoss@gmail.com',
                'password': 'password'}),
            content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_update_user(self):
        response = self.client.put(
            url_for('api.get_user'),
            headers=self.get_api_header(self.get_token()),
            data=json.dumps({'username': 'gathondu'}),
            content_type='application/json'
            )
        self.assertEqual(200, response.status_code)

    def test_cannot_reuse_username(self):
        with self.assertRaises(ValidationError):
            response = self.client.put(
                url_for('api.get_user'),
                headers=self.get_api_header(self.get_token()),
                data=json.dumps({'username': 'dng'}),
                content_type='application/json'
                )
