'''
Tests the models
'''
from sqlalchemy import exc

from tests import BaseTestCase
from xanadu import db
from xanadu.models import User, Item


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

    def test_a_list_item_has_only_one_author(self):
        item = Item.query.filter_by(title='my first vacation').all()
        self.assertEqual(1, len(item))
