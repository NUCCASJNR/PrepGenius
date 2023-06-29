#!/usr/bin/python3
"""
User class for the practice app
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
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
