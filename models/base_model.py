#!/usr/bin/python3

"""
BaseModel class for other classes to inherit from
"""

import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import getenv
from sqlalchemy.pool import QueuePool

user = getenv("prep_user")
db_name = getenv("prep_db")
host = getenv("prep_host")
pwd = getenv("prep_pwd")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{pwd}@{host}/{db_name}'
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'poolclass': QueuePool,
    'pool_size': 10  # Adjust the pool size as per your requirements
}
db = SQLAlchemy(app)


class BaseModel(db.Model):
    """
    BaseModel class
    Args:
        id: Random id for each table
        created_at: Represents the time each class was created
        updated_at: Represents the time each class was updated
    """
    __abstract__ = True
    id = db.Column(db.String(126), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def save(self):
        """
        Saves the current session into the database
        """
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """
        Deletes the current session from the database
        """
        db.session.delete(self)
        db.session.commit()

    def close(self):
        db.session.remove()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        attributes = {}
        for column in self.__table__.columns:
            attribute_name = column.name
            attribute_value = getattr(self, attribute_name)
            attributes[attribute_name] = attribute_value
        return attributes