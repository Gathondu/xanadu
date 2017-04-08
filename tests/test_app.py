'''
Test the application instance
'''
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
