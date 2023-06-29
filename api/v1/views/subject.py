#!/usr/bin/python3
"""
Handles all Restful APIs for subjects
"""

from flask import Flask, jsonify, abort, request
from models.subject import Subject
from api.v1.views import api


@api.route('/subjects', methods=['GET'], strict_slashes=False)
def get_subjects():
    """
    Retrieves all the subjects from the database
    """
    subs = Subject.query.all()
    subs_list = []
    for sub in subs:
        sub_data = sub.to_dict()
        subs_list.append(sub_data)
    return jsonify(subs_list)
