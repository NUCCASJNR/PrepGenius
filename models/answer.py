#!/usr/bin/python3
"""
Answer class
"""
from models.base_model import BaseModel, db
from models.user import User
from models.question  import  Question
from models.option import Option

class Answer(BaseModel):
    __tablename__ = 'answers'
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.String(128), db.ForeignKey('questions.id'), nullable=False)
    selected_option_id = db.Column(db.String(128), db.ForeignKey('options.id'), nullable=False)
    is_correct = db.Column(db.Boolean)
    
    question = db.relationship('Question', uselist=False)
    selected_option = db.relationship('Option', uselist=False)