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
        self.client = self.app.test_client(use_cookies=True)
        db.create_all()
        self.user = User(
            first_name='denis',
            last_name='gathondu',
            nickname='dng',
            email='thundoss@gmail.com',
            password='denno'
        )
        self.user2 = User(
            first_name='denis',
            last_name='gathondu',
            nickname='dngathondu',
            email='thundos@yahoo.com',
            password='denno'
        )
        self.item = Item(
            title='my first vacation',
            body='visit paris and get to learn about their cuisine.',
            created_at=datetime.utcnow(),
            author=self.user
        )
        self.item2 = Item(
            title='my second vacation',
            body='visit oahu.',
            created_at=datetime.utcnow(),
            author=self.user
        )
        self.item3 = Item(
            title='buy a car',
            body='BMW M3 sport edition.',
            created_at=datetime.utcnow(),
            author=self.user
        )
        self.item4 = Item(
            title='visit parents',
            body='go back home to kenya and visit with my parents and family.',
            created_at=datetime.utcnow(),
            author=self.user2
        )
        self.item5 = Item(
            title='go bungee jumping',
            body="take a holiday in sagana where i'll go bungee jumping.",
            created_at=datetime.utcnow(),
            author=self.user2
        )
        db.session.add_all([
            self.user, self.user2, self.item, self.item2, self.item3,
            self.item4, self.item5])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
