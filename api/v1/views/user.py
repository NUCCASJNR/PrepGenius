#!/usr/bin/python3

from flask import abort, jsonify, make_response, request

from api.v1.views import api
from models.base_model import BaseModel, db
from models.user import User

@api.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users = User.query.all()

    user_list = []
    for user in users:
        user_data = user.to_dict()
        user_list.append(user_data)
    return jsonify(user_list)