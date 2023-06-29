#!/usr/bin/python3
"""
Subject class
"""

from models.base_model import BaseModel, db

class Subject(BaseModel):
    """
    Subject class 
    """
    __tablename__ = 'subjects'
    name = db.Column(db.String(128), nullable=False)
    