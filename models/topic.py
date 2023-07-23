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
    subject_id = db.Column(db.String(126), db.ForeignKey('subjects.id'), nullable=False)
    num_questions = db.Column(db.Integer, default=0)

    def increment_questions(self):
        """
        Increments the questions associated with a topic by 1
        """
        self.num_questions += 1