#!/usr/bin/python3
"""
Quiz class for the quiz app
"""

from models.base_model import BaseModel, db
from models.user import User

from sqlalchemy import Text

class Quiz(BaseModel):
    """
    Quiz class that also inherits from base_model
    Args:
        title: title of the quiz
            type: Text
        description: Description of the quiz
            type: string
        language: Since its a language quiz app, users can select their preferred quiz language
            type: string
        created_by: User who created the quiz
            type: integer
    """
    __tablename__ = 'quizes'
    title = db.Column(Text, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    language = db.Column(db.String(60), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
