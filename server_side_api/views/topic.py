#!/usr/bin/env python3

"""
Handles All ReSTFul APIs for topics
"""
from typing import Tuple

from flask import abort, jsonify, Response, request
from models.topic import Topic
from server_side_api.views import api
from models.subject import Subject


@api.route('/topics', methods=['GET'], strict_slashes=False)
def get_topics() -> Response:
    """
    Returns all the topics
    """
    topics = Topic.all()
    topics_list = [topic.to_dict() for topic in topics]
    return jsonify(topics_list)


@api.route('/topics/<topic_id>', methods=['GET'], strict_slashes=False)
def get_one_topic(topic_id: str) -> Response:
    """Gets a topic using the provided topic id"""
    topic: str = Topic.get(topic_id)
    if topic:
        return jsonify(topic.to_dict())
    abort(404)


@api.route('/topics/<topic_id>', methods=['DELETE'], strict_slashes=False)
def delete_one_topic(topic_id: str) -> tuple[Response, int]:
    """Deletes a topic using the provided topic_id"""
    topic: str = Topic.get(topic_id)
    if topic:
        topic.delete()
        return jsonify({}), 200
    abort(404)


@api.route('/topics/<subject_id>', methods=['POST'], strict_slashes=False)
def post_new_subject(subject_id: str) -> Response:
    """
    Posts a new Topic for a subject using the provided subject_id
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    subject = Subject.get(subject_id)
    if subject:
        if 'name' not in request.get_json():
            abort(400, "Missing name")
        if 'subject_id' not in request.get_json():
            abort(400, "Missing subject_id")
        # if 'num_questions' not in request.get_json():
        #     abort(400, "Missing number of questions")
        topic = Topic(**request.get_json())
        topic.save()
        return jsonify(topic.to_dict())
    abort(404)
