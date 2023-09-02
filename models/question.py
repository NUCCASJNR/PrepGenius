#!/usr/bin/python3
"""
Question class for the Practice App
"""
from models.base_model import BaseModel, db


class Question(BaseModel):
    """
    Question class that inherits from base_model
    """
    __tablename__ = 'questions'
    subject_id = db.Column(db.String(126), db.ForeignKey('subjects.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    topic_id = db.Column(db.String(126), db.ForeignKey('topics.id'), nullable=False)
    explanation = db.Column(db.Text)
    correct_option_id = db.Column(db.String(126), db.ForeignKey('options.id',
                                                                name='fk_question_correct_option_id'), nullable=False)
