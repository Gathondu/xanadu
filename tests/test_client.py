'''
Tests for the client
'''
import re

from datetime import datetime
from flask import url_for
from unittest import skip

from xanadu.models import User
from tests import BaseTestCase


@skip('WIP')
class ClientTestCase(BaseTestCase):
    '''Test the client instance'''
    def test_app_client(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Stranger' in response.get_data(as_text=True))

    def test_register(self):
        '''test the registration of a new user'''
        response = self.client.post(url_for('auth.register'), data={
            'first_name': 'danson',
            'last_name': 'miti',
            'nickname': 'miti',
            'email': 'example@gmail.com',
            'password': 'dan'
        }, follow_redirects=True)
        self.assertEqual(302, response.status_code)

    def test_login(self):
        '''test the loggin in of a registered user'''
        response = self.client.post(url_for('auth.login'), data={
            'email': 'example@gmail.com',
            'password': 'dan'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue(re.search(r'Hello,\s+miti!', data))

    def test_confirmation_token(self):
        '''test that a confirmation token is sent to the user'''
        user = User.query.filter_by(email='example@gmail.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get(url_for('auth.confirm', token=token),
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('You have confirmed your account', data)

    def test_logout(self):
        '''test user is logged out'''
        response = self.client.get(url_for('auth.logout'),
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('You have been logged out', data)
