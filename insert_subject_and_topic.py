#!/usr/bin/python3
"""
This script inserts into the topics table in the database
"""

from sys import argv
import os
from models.base_model import app, db
from models.topic import Topic
from models.subject import Subject

with app.app_context():
    subject = Subject(
      name=argv[1]  
    )
    subject.save()
    topic = Topic(
        name=argv[2],
        subject_id = subject.id
    )
    topic.save()