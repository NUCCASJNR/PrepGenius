#!/usr/bin/python3
"""
Quiz class for the quiz app
"""

from models.base_model import BaseModel, db
from sqlalchemy import Text

class Quiz(BaseModel):
    """
    Quiz class that also inherits from base_model
    """
    __tablename__ = 'quizes'
    title = db.Column(Text, nullable=False)
    description = db.Column(db.String(60))
    language = db.Column(db.String(60), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    