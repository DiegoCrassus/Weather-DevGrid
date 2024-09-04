import logging.config
import warnings
import os

from loguru import logger
from flask import Flask, Blueprint
from flask_cors import CORS
from unittest.mock import MagicMock
from src.api.settings import envs
from src.api.project.api.health import ns as health_operation
from src.api.project.api.user import ns as user_operation
from src.api.project.api.weather import ns as weather_operation
from src.api.project.restx import api
from src.api.extensions import db

app = Flask(__name__)
logger.add(envs.PATH_LOG, rotation="1 week")


def configure_app(flask_app):
    flask_app.config["SERVER_NAME"] = envs.FLASK_SERVER_NAME
    flask_app.config["SWAGGER_UI_DOC_EXPANSION"] = envs.RESTX_SWAGGER_UI_DOC_EXPANSION
    flask_app.config["RESTX_VALIDATE"] = envs.RESTX_VALIDATE
    flask_app.config["RESTX_MASK_SWAGGER"] = envs.RESTX_MASK_SWAGGER
    flask_app.config["ERROR_404_HELP"] = envs.RESTX_ERROR_404_HELP
    flask_app.config["CORS_HEADERS"] = "Content-Type"
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = envs.DATABASE_URL
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def initialize_app(flask_app):
    configure_app(flask_app)
    CORS(
        flask_app,
        allow_headers=["access-control-allow-origin", "Content-Type"],
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=True,
    )

    blueprint = Blueprint("api", __name__, url_prefix=envs.FLASK_URL_FIX)
    api.init_app(blueprint)
    api.add_namespace(health_operation)
    api.add_namespace(user_operation)
    api.add_namespace(weather_operation)
    flask_app.register_blueprint(blueprint)

    if not flask_app.testing:
        db.init_app(flask_app)

def main(flask_app):
    warnings.filterwarnings("ignore")
    initialize_app(flask_app)
    return flask_app


app = main(app)
