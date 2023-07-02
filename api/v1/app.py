#!/usr/bin/python3

from os import getenv

from flasgger import Swagger
from flask import Blueprint, Flask, jsonify, make_response, render_template
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from api.v1.views import api
from models.base_model import BaseModel, db


user = getenv("prep_user")
db_name = getenv("prep_db")
host = getenv("prep_host")
pwd = getenv("prep_pwd")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
      f'mysql+mysqldb://{user}:{pwd}@{host}/{db_name}'
db.init_app(app)
app.register_blueprint(api)
migrate = Migrate(app, db) 
# manager.add_command('db', MigrateCommand)
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
