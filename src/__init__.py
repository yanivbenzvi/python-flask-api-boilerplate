import json

import config
from flask import Flask, Blueprint, jsonify
from werkzeug.exceptions import HTTPException, InternalServerError

from src.errors import APIError, register_error_handlers


def create_app():
    # app initialization
    app = Flask(__name__)

    # app configuration
    app.config.from_object(config.exportConfig)

    # register error handlers
    register_error_handlers(app)

    # blueprints registering
    from src import routes
    blueprints_candidate = vars(routes).values()
    blueprints_list = list(filter(lambda blueprint: isinstance(blueprint, Blueprint), blueprints_candidate))
    [app.register_blueprint(blueprint) for blueprint in blueprints_list]

    return app
