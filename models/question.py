#!/usr/bin/python3
"""
Question class for the Quiz App
"""
from models.base_model import BaseModel, db

class Question(BaseModel):
    """
    Question class that inherits from base_model
    """
    __tablename__ = 'questions'