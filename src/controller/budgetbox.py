from http import HTTPStatus

from src import APIError
from src.models.user import User
from src.models.budgetbox import BudgetBox


def create_budget_box(req):
    try:
        user_id = req.get('user_id')
        user = User.get(user_id)
        if not user:
            raise APIError('User not found', HTTPStatus.BAD_REQUEST)

        del req['user_id']
        budget_box = BudgetBox(**req)
        budget_box.save()

        user.set_budget_box_id(budget_box.id)
        user.save()
        return budget_box.to_json(), HTTPStatus.CREATED
    except Exception as e:
        raise e


def get_budget_box_by_id(user_id):
    try:
        budget_box = BudgetBox.get(user_id)
        if budget_box:
            return budget_box.to_json()
        raise APIError('BudgetBox not found', HTTPStatus.NOT_FOUND)
    except Exception as e:
        raise e


def delete_budget_box_by_id(budget_box_id, req):
    try:
        user_id = req.get('user_id', None)
        user = User.get(budget_box_id)
        budget_box = BudgetBox.get(budget_box_id)
        budget_category_list = budget_box.get_budget_categories_list()

        if not user:
            raise APIError('User not found', HTTPStatus.BAD_REQUEST)
        if not budget_box:
            raise APIError('BudgetBox not found', HTTPStatus.NO_CONTENT)

        [budget_category.delete() for budget_category in budget_category_list]
        budget_box.delete()
        user.set_budget_box_id(None)
        user.save()

        return budget_box.to_json(), HTTPStatus.OK
    except Exception as e:
        raise e


def get_all_budget_box():
    budget_box_list = BudgetBox.get_all()
    budget_box_dict = [budget_box.to_json() for budget_box in budget_box_list]

    return budget_box_dict if budget_box_dict else []


def update_budget_box_by_id(user_id, req):
    try:
        user = User.get(user_id)
        if user:
            user.update(**req)
            return user.to_json()
        raise APIError('User not found', HTTPStatus.NO_CONTENT)
    except Exception as e:
        raise e
