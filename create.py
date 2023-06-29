#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.user import User
user = getenv("prep_user")
db = getenv("prep_db")
host = getenv("prep_host")
pwd = getenv("prep_pwd")

# Create the database engine
engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}")


Base.metadata.bind = engine

# Create the tables
Base.metadata.create_all(engine)
# Create a session
Session = sessionmaker(bind=engine)
session = Session()
# Close the session
session.close()
