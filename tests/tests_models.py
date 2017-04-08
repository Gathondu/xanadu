'''
Tests the models
'''
from tests import BaseTestCase
from xanadu import db
from xanadu.models import User, Item


class TestUser(BaseTestCase):
    '''
    Test the user model
    '''
    def test_user_is_saved(self):
        db.session.add(self.user)
        db.session.commit()
        self.assertIsNotNone(User.query.filter_by(nickname='dng').first())

    def test_user_cannot_be_duplicated(self):
        db.session.add(self.user)
        db.session.commit()
        db.session.add(self.user)
        db.session.commit()
        self.assertEqual(1, len(User.query.all()))

    def test_password_setter(self):
        self.assertIsNotNone(self.user.password_hash)

    def test_no_password_getter(self):
        with self.assertRaises(AttributeError):
            self.user.password

    def test_password_verification(self):
        self.assertTrue(self.user.verify_password('denno'))
        self.assertFalse(self.user.verify_password('password'))

    def test_passwords_are_random(self):
        u = User(password='denno')
        self.assertNotEqual(u.password_hash, self.user.password_hash)
