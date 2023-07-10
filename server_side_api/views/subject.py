#!/usr/bin/python3
"""
Handles all Restful APIs for subjects
"""

from flask import Flask, jsonify, abort, request
from models.subject import Subject
from server_side_api.views import api

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

@api.route('/subjects/<sub_id>', methods=['DELETE'], strict_slashes=False)
def delete_one_subject(sub_id):
    """
    Deletes a subject from the database using the
    provided subject_id
    """
    sub = Subject.get(sub_id)
    if sub:
        sub.delete()
        return jsonify({}), 200
    abort(404)

@api.route('/subjects', methods=['POST'], strict_slashes=False)
def create_subject():
    """
    Creates a subject in the database
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    sub = Subject(**request.get_json())
    sub.save()
    return jsonify(sub.to_dict()), 201

@api.route('/subjects/<sub_id>', methods=['PUT'], strict_slashes=False)
def update_subject(sub_id):
    """
    Updates a subject in the subject table where the
    sub_id matches a subject_id in the table
    """
    form = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    if not form:
        return jsonify({"error": "Not a JSON"})
    
    sub = Subject.get(sub_id)
    if sub:
        for key, value in form.items():
            if key not in ignore:
                setattr(sub, key, value)
        sub.save()
        return jsonify(sub.to_dict())
    abort(404)
