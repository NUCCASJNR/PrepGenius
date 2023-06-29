#!/usr/bin/python3
"""
This script is used to insert into the database 
aside using the API
"""

from models.subject import Subject
from models.base_model import app, db

with app.app_context():
    subject = Subject(
        name='physics'
    )
    subject.save()
