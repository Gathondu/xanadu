'''
Define basetest for all the tests
'''
import os
import unittest

from datetime import datetime
from xanadu import create_app, db
from xanadu.models import User, Item


class BaseTestCase(unittest.TestCase):
    '''
    Base test class for all tests
    '''
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User(
            first_name='denis',
            last_name='gathondu',
            nickname='dng',
            email='thundoss@gmail.com',
            password='denno',
            created_at=datetime.utcnow()
        )
        self.item = Item(
            title='my first vacation',
            body='visit paris and get to learn about their cuisine.',
            created_at=datetime.utcnow(),
            author=self.user
        )

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
