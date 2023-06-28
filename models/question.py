#!/usr/bin/python3
"""
Question class for the Quiz App
"""
from models.base_model import BaseModel, db
from models.quiz import Quiz

class Question(BaseModel):
    """
    Question class that inherits from base_model
    """
    __tablename__ = 'questions'
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'), nullable=False)
    