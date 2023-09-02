#!/usr/bin/python3
"""
Options class to handle the correct option of a question
"""
from models.base_model import BaseModel, db


class Option(BaseModel):
    """
    Option class that inherits from base_model
    Args:
        question_id: Integer
        option_text: String
        is_correct: Boolean
    """
    __tablename__ = 'options'
    question_id = db.Column(db.String(126), db.ForeignKey('questions.id', name='fk_option_question_id'), nullable=False)
    option_text = db.Column(db.Text, nullable=False)
