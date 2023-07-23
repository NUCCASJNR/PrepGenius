#!/usr/bin/python3

import os
import unittest

from flask_testing import TestCase

from database import app, db
from models.user import User

os.environ['TESTING'] = 'True'
class UserTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestUserModel(UserTest):
    def test_user_model_save_and_retrieve(self):
        """
        Test User model save and retrieve operations
        """
        user = User(
            email="test@eailcom",
            username="tesing",
            password="test",
            first_name="Test",
            last_name="User"
        )
        user.save()
        retrieved_user = User.get(user.id)
        user_name = User.query.filter_by(username=user.username).first()
        self.assertEqual(user, retrieved_user)
        self.assertEqual(user, user_name)

if __name__ == '__main__':
    unittest.main()
