#!/usr/bin/python3

from flask import Blueprint, Flask, jsonify, make_response

from api.v1.views import api
from os import getenv
from models.base_model import db, BaseModel

user = getenv("prep_user")
db_name = getenv("prep_db")
host = getenv("prep_host")
pwd = getenv("prep_pwd")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{pwd}@{host}/{db_name}'
db.init_app(app)
app.register_blueprint(api)

@app.teardown_appcontext
def close_db_connection(exception):
    """
    calls storage.close() to close the database connection
    """
    BaseModel().close()


@app.errorhandler(404)
def error(error):
    """
    Handles 404 error
    """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)