#!/usr/bin/python3
"""
BaseModel class for other classes to inherit from
"""
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.model):
    """
    BaseModel class
    Args:
        id: Random id for each tables
        created_at: Represents the time each class was created
        updated_at: REpresents the time each class was updated
    """
    id = db.Column(db.string(126), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def save(self):
        """
        Saves the current session into the database
        """
        db.session.add(self)
        db.session.commit(self)
    
    def delete(self):
        """
        Deletes the current session from the database
        """
        db.session.delete(self)
        db.session.commit(self)