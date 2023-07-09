#!/usr/bin/python3
"""
Topic
"""

from models.base_model import BaseModel, db


class Topic(BaseModel):
    """
    Topics class
    """
    __tablename__ = 'topics'
    name = db.Column(db.String(128), nullable=False)
    subject_id = db.Column(db.String(128), db.ForeignKey('subjects.id'), nullable=False)
