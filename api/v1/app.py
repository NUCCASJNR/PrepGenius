#!/usr/bin/python3

from flask import Blueprint, Flask, jsonify

from api.v1.views import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)