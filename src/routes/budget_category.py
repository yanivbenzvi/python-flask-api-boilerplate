from flask import Blueprint, request, jsonify

from src.controller.budget_category import get_all_budget_category, get_budget_category_by_id, create_budget_category, \
    delete_budget_category_by_id

budget_category_blueprint = Blueprint('budget_category', __name__)


@budget_category_blueprint.route('/budget-category', methods=['GET'])
def get_all_id():
    return jsonify(get_all_budget_category())


@budget_category_blueprint.route('/budget-category/<budget_box_id>', methods=['GET'])
def get_by_id(budget_box_id):
    return get_budget_category_by_id(budget_box_id)


@budget_category_blueprint.route('/budget-category', methods=['POST'])
def create():
    req = request.get_json()

    return create_budget_category(req)


@budget_category_blueprint.route('/budget-category/<budget_box_id>', methods=['DELETE'])
def delete_user(budget_box_id):
    req = request.get_json()
    return delete_budget_category_by_id(budget_box_id, req)

# TODO: Add PUT
# @budget_category_blueprint.route('/budget-category/<budget_box_id>', methods=['PUT'])
# def update_budget_box(budget_box_id):
#     req = request.get_json()
#     return update_budget_box_by_id(budget_box_id, req)
