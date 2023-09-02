#!/usr/bin/python3

from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from server_side_api.views.user import *
from server_side_api.views.subject import *
