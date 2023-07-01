#!/usr/bin/python3

"""
BaseModel class for other classes to inherit from
"""

import uuid
from datetime import datetime
from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool
from flask_migrate import Migrate

user = getenv("prep_user")
db_name = getenv("prep_db")
host = getenv("prep_host")
pwd = getenv("prep_pwd")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+mysqldb://{user}:{pwd}@{host}/{db_name}'
db = SQLAlchemy(app)
# db.init_app(app)

class BaseModel(db.Model):
    """
    BaseModel class
    Args:
        id: Random id for each table
        created_at: Represents the time each class was created
        updated_at: Represents the time each class was updated
    """
    __abstract__ = True
    id = db.Column(db.String(126), primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())

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
    
    @classmethod
    def all(cls):
        """
        Retrieves all objects of the current model
        """
        return cls.query.all()
    
    @classmethod
    def get(cls, id):
        """
        Retrieve an object by its id.
        Returns the object if found, None otherwise.
        """
        if id:
            return cls.query.get(id)
        return None