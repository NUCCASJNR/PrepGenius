#!/usr/bin/python3

import os
import unittest

from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError

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
        user_name = "tesing"
        self.assertEqual(user, retrieved_user)
        self.assertEqual(user.username, user_name)
        self.assertEqual(user.email, "test@eailcom")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.first_name, "Test")

    def test_wrong_data_type(self):
        """
        Test wrong data type
        """
        with self.assertRaises(TypeError):
            user = User(
                email=123,
                username="tesing",
                password="test",
                first_name="Test",
                last_name="User"
            )
            user.save()

    def test_unique_constraints(self):
        """
        Test unique constraints for username and email fields
        """
        # Create a user with a specific username and email
        user1 = User(
            email="test1@example.com",
            username="test_user_1",
            password="test",
            first_name="Test",
            last_name="User"
        )
        user1.save()
        with self.assertRaises(IntegrityError):
            user2 = User(
                email="test1@example.com",
                username="test_user_1",
                password="test",
                first_name="Test",
                last_name="User"
            )
            user2.save()
    def test_to_dict(self):
       """
       Test to_dict method on user
       """
       d_user = User(
           email="test1@example.comic",
           username="test_user1",
           password="test",
           first_name="Test",
           last_name="User"
        )
       d_user.save()
       user_dict = d_user.to_dict()
       expected_dict = {
           'id': d_user.id,
           'created_at': d_user.created_at,
           'updated_at': d_user.updated_at,
           'email': "test1@example.comic",
           'username': "test_user1",
           'password': "test",
           'first_name': "Test",
           'last_name': "User"
        }
       self.assertEqual(user_dict, expected_dict)
if __name__ == '__main__':
    unittest.main()
