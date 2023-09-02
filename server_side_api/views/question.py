#!/usr/bin/python3

"""
Hanldes all Restful APIs for questions
"""

from flask import jsonify, abort, request

from server_side_api.views import api
from models.question import Question
from models.subject import Subject
from models.option import Option
from models.topic import Topic

