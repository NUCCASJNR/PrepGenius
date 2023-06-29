#!/usr/bin/python3

from models.user import User
from models.base_model import app, db

# Create the user and insert it into the database
with app.app_context():
# Create a new user instance
    new_user = User(
        username='idan',
        email='idan@examp.com',
        first_name='AlAreef',
        last_name='Ayompo',
        password='password123'
    )

# Add the user to the session and commit the changes to the database
    new_user.save()

# Optionally, you can also fetch the inserted user from the database
#inserted_user = User.query.filter_by(username='john_doe').first()
#print(inserted_user)
