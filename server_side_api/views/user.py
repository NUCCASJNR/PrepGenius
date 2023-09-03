#!/usr/bin/python3

from flask import abort, jsonify, make_response, request
from server_side_api.views import api
from models.user import User


@api.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves all users from the database
    """
    users = User.all()
    user_list = [user.to_dict() for user in users]
    return jsonify(user_list)


@api.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_one_user(user_id):
    """
    Retrieve one user from the database using
    the provided user_id
    """
    user = User.get(user_id)
    if user:
        user_data = user.to_dict()
        return jsonify(user_data)
    abort(404)


@api.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    Delete one user from the database using
    the provided user_id
    """
    user = User.get(user_id)
    if user:
        user_data = user.to_dict()
        user.delete()
        return jsonify({"Status": "OK"})
    abort(404)


@api.route('/users', methods=['POST'], strict_slashes=False)
def post_new_user():
    """
    posts a new user to the database
    """
    form = request.get_json()
    if not form:
        return jsonify({"error": "Not a JSON"})
    if "email" not in form:
        return jsonify({"error": "Missing email"})
    if "username" not in form:
        return jsonify({"error": "Missing Username"})
    if "last_name" not in form:
        return jsonify({"error": "Missing Lastname"})
    if "first_name" not in form:
        return jsonify({"error": "Missing Firstname"})
    user = User()
    for key, value in form.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 201


@api.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    Updates the details of an existing user in the users table
    """
    form = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    if not form:
        return jsonify({"error": "Not a JSON"})
    user = User.get(user_id)
    if not user:
        abort(404)
    for key, value, in form.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
