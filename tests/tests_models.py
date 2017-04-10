'''
Tests the models
'''
from datetime import datetime
from sqlalchemy import exc

from tests import BaseTestCase
from xanadu import db
from xanadu.models import User, BucketList, Item


class UserTestCase(BaseTestCase):
    '''
    Test the user model
    '''
    def test_user_must_have_details(self):
        test_user = User()
        db.session.add(test_user)
        with self.assertRaises(exc.IntegrityError):
            db.session.commit()

    def test_user_is_saved(self):
        self.assertIsNotNone(User.query.filter_by(nickname='dng').first())

    def test_user_cannot_be_duplicated(self):
        db.session.add(self.user)
        db.session.commit()
        self.assertEqual(2, len(User.query.all()))

    def test_password_setter(self):
        self.assertIsNotNone(self.user.password_hash)

    def test_no_password_getter(self):
        with self.assertRaises(AttributeError):
            self.user.password

    def test_password_verification(self):
        self.assertTrue(self.user.verify_password('denno'))
        self.assertFalse(self.user.verify_password('password'))

    def test_passwords_are_random(self):
        self.assertNotEqual(self.user.password_hash, self.user2.password_hash)

    def test_user_has_items_in_list(self):
        self.assertIsNotNone(Item.query.filter_by(author=self.user).all())

    def test_user_creates_correctly(self):
        user = User(
            first_name='dan',
            last_name='miti',
            nickname='miti',
            email='example@gmail.com',
            password='password',
            created_at=datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(nickname='miti').first()
        self.assertIsNotNone(user)


class BucketListTestCase(BaseTestCase):
    '''Test the bucketlist model'''
    def test_list_saved(self):
        self.assertIsNotNone(BucketList.query.all())

    def test_list_must_have_title(self):
        bucketlist = BucketList()
        db.session.add(bucketlist)
        with self.assertRaises(exc.IntegrityError):
            db.session.commit()

    def test_a_list_has_an_author(self):
        bucketlist = BucketList.query.filter_by(title='places').first()
        self.assertIsNotNone(bucketlist.author)


class ItemTestCase(BaseTestCase):
    '''
    Test the list items
    '''
    def test_item_is_saved(self):
        self.assertIsNotNone(Item.query.all())

    def test_item_must_have_an_title(self):
        item = Item()
        db.session.add(item)
        with self.assertRaises(exc.IntegrityError):
            db.session.commit()

    def test_item_has_an_author(self):
        item = Item.query.filter_by(title='my first vacation').first()
        self.assertIsNotNone(item.author)

    def test_item_belongs_to_a_bucketlist(self):
        item = Item.query.filter_by(title='my first vacation').first()
        self.assertIsNotNone(item.bucketlist)
