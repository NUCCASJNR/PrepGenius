#!/usr/bin/python3
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


user = getenv("prep_user")
pwd = getenv("prep_pwd")
db_name = getenv("prep_db")
host = getenv("prep_host")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{pwd}@{host}/{db_name}'
db = SQLAlchemy(app)
