'''
Test the factory function
'''
from flask import url_for

from flask import current_app
from tests import BaseTestCase


class TestApp(BaseTestCase):
    '''
    Tests for the app instance
    '''
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_app_client(self):  # put this in a test client file
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Stranger' in response.get_data(as_text=True))
