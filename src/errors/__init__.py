import traceback

from flask import jsonify
from http import HTTPStatus

from src.errors.errors import APIError


def register_error_handlers(app):
    @app.errorhandler(APIError)
    def handle_exception(err):
        """Return custom JSON when APIError or its children are raised"""
        response = {
            "code": err.status_code,
            "message": err.message,
            "payload": err.payload if app.config["DEBUG"] else "",
            "stack_trace": err.traceback if app.config["DEBUG"] else "",
        }

        return jsonify(response), err.status_code

    @app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
    @app.errorhandler(Exception)
    def handle_exception(err):
        """Return custom JSON when Exception or its children are raised"""
        response = {
            "error": f"{str(err)}",
            "traceback": traceback.format_exc() if app.config["DEBUG"] else "",
        }

        return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def handle_exception(err):
        """Return custom JSON when Exception or its children are raised"""
        response = {"error": f"{str(err)}"}
        return jsonify(response), HTTPStatus.NOT_FOUND
