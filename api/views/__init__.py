#!/usr/bin/python3

from models.base_model import db

from flask import Blueprint, Flask

api = Blueprint('api', __name__, url_prefix='/api')

from api.views.user import *
from api.views.subject import *
