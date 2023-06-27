#!/usr/bin/python3
"""
User class for the quiz app
"""
from models.base_model import BaseModel, db

class User(BaseModel):
    """
    User class that inherits from base_model
    Arg:
        username: string
        email: String
        first_name: string
        last_name: String
        password: String
    """
    __tablename__ = 'users'
    username = db.Column(db.string(60), unique=True, nullable=False)
    email = db.Column(db.string(256), unique=True, nullable=False)
    first_name = db.Column(db.string(60), nullable=False)
    last_name = db.Column(db.string(60), nullable=False)
    password = db.Column(db.string(60), nullable=False)
    