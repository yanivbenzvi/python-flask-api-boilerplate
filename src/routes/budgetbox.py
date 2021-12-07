from flask import Blueprint, request, jsonify

from src.controller.budgetbox import get_all_budget_box, create_budget_box, get_budget_box_by_id, \
    delete_budget_box_by_id, update_budget_box_by_id

budget_box_blueprint = Blueprint('budget_box', __name__)


@budget_box_blueprint.route('/budget-box', methods=['GET'])
def get_all_id():
    return jsonify(get_all_budget_box())


@budget_box_blueprint.route('/budget-box/<budget_box_id>', methods=['GET'])
def get_by_id(budget_box_id):
    return get_budget_box_by_id(budget_box_id)


@budget_box_blueprint.route('/budget-box', methods=['POST'])
def create():
    req = request.get_json()

    return create_budget_box(req)


@budget_box_blueprint.route('/budget-box/<budget_box_id>', methods=['DELETE'])
def delete_user(budget_box_id):
    req = request.get_json()
    return delete_budget_box_by_id(budget_box_id, req)


@budget_box_blueprint.route('/budget-box/<budget_box_id>', methods=['PUT'])
def update_budget_box(budget_box_id):
    req = request.get_json()
    return update_budget_box_by_id(budget_box_id, req)
