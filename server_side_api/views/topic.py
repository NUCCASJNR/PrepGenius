#!/usr/bin/env python3

"""
Handles All ReSTFul APIs for topics
"""
from typing import Tuple

from flask import abort, jsonify, Response
from models.topic import Topic
from server_side_api.views import api


@api.route('/topics', methods=['GET'], strict_slases=False)
def get_topics() -> Response:
    """
    Returns all the topics
    """
    topics = Topic.all()
    topics_list = []
    for topic in topics:
        topic_data = topic.to_dict()
        topics_list.append(topic_data)
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
