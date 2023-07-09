#!/usr/bin/python3
"""
This script inserts into the topics table in the database
"""

from models.base_model import BaseModel, app, db
from models.topic import Topic
from sys import argv

with app.app_context():
    topic = Topic(
        name=argv[1]
    )
    topic.save()