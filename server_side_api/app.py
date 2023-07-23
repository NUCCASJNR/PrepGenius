#!/usr/bin/python3

from os import getenv

from flasgger import Swagger
from flask import Blueprint, Flask, jsonify, make_response, render_template
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from server_side_api.views import *
from models.base_model import BaseModel, db, app

app.register_blueprint(api)
migrate = Migrate(app, db) 
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.close()


@app.errorhandler(404)
def error(error):
    """
    Handles 404 error
    """
    return make_response(jsonify({"error": "Not found"}), 404)
app.config['SWAGGER'] = {
    'title': 'Prep API',
    'description': 'Prep API Information',
    'uiversion': 3
}
swagger = Swagger(app)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
