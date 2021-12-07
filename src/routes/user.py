import json
from flask import Blueprint, request, jsonify

from src.controller.user import create_user, get_user_by_id, delete_user_by_id, get_all_user, update_user_by_id

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user', methods=['GET'])
def get_all_id():
    return jsonify(get_all_user())


@user_blueprint.route('/user/<user_id>', methods=['GET'])
def get_by_id(user_id):
    return get_user_by_id(user_id)


@user_blueprint.route('/user', methods=['POST'])
def create():
    req = request.get_json()

    return create_user(req)


@user_blueprint.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by id and return the deleted user.
    In case of error, return a json with the error message.
    :param user_id:
    :return:
    """
    return delete_user_by_id(user_id)


@user_blueprint.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user by id and return the updated user.
    In case of error, return a json with the error message.
    :param user_id:
    :return:
    """
    req = request.get_json()
    return update_user_by_id(user_id, req)
