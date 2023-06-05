from flask import Blueprint, request, jsonify

service_health = Blueprint('service_health', __name__)


@service_health.route('/status', methods=["GET"])
def get_service_status():
    return {
        "status": "ok"
    }
