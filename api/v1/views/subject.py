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
    subs = Subject.all()
    subs_list = []
    for sub in subs:
        sub_data = sub.to_dict()
        subs_list.append(sub_data)
    return jsonify(subs_list)

@api.route('/subjects/<sub_id>', methods=['GET'], strict_slashes=False)
def get_one_subject(sub_id):
    """
    Retrieve one subject from the database using the
    provided subject_id
    """
    sub = Subject.get(sub_id)
    if sub:
        return jsonify(sub.to_dict())
    abort(404)

# @api.route('/subjects/<sub_id>', methods=['DELETE'], strict_slashes=False)
