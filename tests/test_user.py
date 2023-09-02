#!/usr/bin/python3

import os
import unittest

from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError

from database import app, db
from models.user import User

os.environ['TESTING'] = 'True'
# app.config.from_pyfile('config_test.py')


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
    
    def test_all(self):
        """
        Test all method on user
        """
        a_user = User(
            email='all1@gmal.com',
            username='first_user',
            password="test",
            first_name="Test",
            last_name="User"
        )
        a_user.save()
        b_user = User(
            email='all2@gmal.com',
            username='second_user',
            password="test",
            first_name="Test",
            last_name="User"
        )
        b_user.save()

        all_users = User.all()
        self.assertEqual(len(all_users), 2)
        self.assertIn(a_user, all_users)
        self.assertIn(b_user, all_users)
    

    def test_get(self):
        """
        Test the get method for the User model
        """
        # Create a user and save it to the database
        user = User(
            email="testing@example.com",
            username="testing_user",
            password="test",
            first_name="Test",
            last_name="User"
        )
        user.save()
        retrieved_user = User.get(user.id)
        self.assertEqual(retrieved_user, user)


if __name__ == '__main__':
    unittest.main()
