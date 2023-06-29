#!/usr/bin/python3
"""
Options class to hanlde correct option of a question
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
    question_id = db.Column(db.String(128), db.ForeignKey('questions.id'),
                            nullable=False)
    option_text = db.Column(db.Text, nullable=False)
