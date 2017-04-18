"""
Define basetest for all the tests
"""
import json
import unittest

from datetime import datetime
from flask import url_for

from xanadu import create_app, db
from xanadu.models.user import User
from xanadu.models.bucketlist import BucketList
from xanadu.models.item import Item


class BaseTestCase(unittest.TestCase):
    """
    Base test class for all tests
    """

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()
        self.user = User(
            first_name='denis',
            last_name='gathondu',
            nickname='dng',
            email='thundoss@gmail.com',
            password='denno',
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow()
            )
        self.user2 = User(
            first_name='denis',
            last_name='gathondu',
            nickname='dngathondu',
            email='thundos@yahoo.com',
            password='denno',
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow()
            )
        self.bucketlist = BucketList(
            title='places',
            description="places i'd love to visit.",
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user
            )
        self.bucketlist2 = BucketList(
            title='cars',
            description="cars i want to own.",
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user
            )
        self.bucketlist3 = BucketList(
            title='home visit',
            description="visit home",
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user2
            )
        self.item = Item(
            title='my first vacation',
            body='visit paris and get to learn about their cuisine.',
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user,
            bucketlist=self.bucketlist
            )
        self.item2 = Item(
            title='my second vacation',
            body='visit oahu.',
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user,
            bucketlist=self.bucketlist
            )
        self.item3 = Item(
            title='buy a car',
            body='BMW M3 sport edition.',
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user,
            bucketlist=self.bucketlist2
            )
        self.item4 = Item(
            title='visit parents',
            body='go back home to kenya and visit with my parents and family.',
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user2,
            bucketlist=self.bucketlist3
            )
        self.item5 = Item(
            title='go bungee jumping',
            body="take a holiday in sagana where i'll go bungee jumping.",
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow(),
            author=self.user2,
            bucketlist=self.bucketlist3
            )
        db.session.add_all([
            self.user, self.user2,
            self.bucketlist, self.bucketlist2, self.bucketlist3,
            self.item, self.item2, self.item3, self.item4, self.item5])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @staticmethod
    def get_api_header(token):
        """helper function to return the header that
           will be sent with the API endpoints"""
        return {
            'Authorization': 'Token ' + str(token)}

    def get_token(self):
        """test that a user can log in"""
        response = self.client.post(
            url_for('auth.login'),
            data=json.dumps(
                {'username': 'thundoss@gmail.com', 'password': 'denno'}),
            content_type='application/json')
        return json.loads(response.data)[1]['token']