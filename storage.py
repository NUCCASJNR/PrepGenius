#!/usr/bin/python3

"""
Storage class
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import models
from models.base_model import BaseModel, Base
from models.user import User
from os import getenv

user = getenv("prep_user")
db = getenv("prep_db")
host = getenv("prep_host")
pwd = getenv("prep_pwd")

classes = {
    "user": User
}
class Storage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Init
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user,
                                             pwd,
                                             host,
                                             db))
        if getenv('BLOG_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    
    def new(self, obj):
        """
        Adds the new object to the database
        """
        self.__session.add(obj)

    def save(self):
        """
        saves to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes the current object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the current database connection
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """
        closes the current session
        """

        self.__session.remove()