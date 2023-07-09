#!/usr/bin/python3
"""
This script is used to insert into the database 
aside using the API
"""

from sys import argv
from models.user import User
from models.base_model import app, db

with app.app_context():
    user = User(
        username=argv[1],
        first_name=argv[2],
        last_name=argv[3],
        email=argv[4],
        password=argv[5]
    )
    user.save()