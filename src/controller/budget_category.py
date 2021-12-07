from http import HTTPStatus

from src import APIError
from src.models.budgetbox import BudgetBox
from src.models.user import User
from src.models.budget_category import BudgetCategory


def create_budget_category(req):
    try:
        user_id = req.get('user_id')
        user = User.get(user_id)
        if not user:
            raise APIError('User not found', HTTPStatus.BAD_REQUEST)

        budget_id = str(user.budget_id)
        budget_box = BudgetBox.get(budget_id)
        if not budget_box:
            raise APIError('BudgetBox not found', HTTPStatus.BAD_REQUEST)

        del req['user_id']
        budget_category = BudgetCategory(**req)
        budget_category.save()

        budget_box.add_category(budget_category)
        budget_box.save()

        return budget_category.to_json(), HTTPStatus.CREATED
    except Exception as e:
        raise e


def get_budget_category_by_id(user_id):
    try:
        budget_box = BudgetCategory.get(user_id)
        if budget_box:
            return budget_box.to_json()
        raise APIError('BudgetCategory not found', HTTPStatus.NOT_FOUND)
    except Exception as e:
        raise e


def delete_budget_category_by_id(budget_category_id, req):
    try:
        user_id = req.get('user_id', None)
        user = User.get(user_id)
        budget_id = str(user.budget_id)

        budget_box = BudgetCategory.get(budget_id)
        budget_category = BudgetCategory.get(budget_category_id)

        if not user:
            raise APIError('User not found', HTTPStatus.BAD_REQUEST)
        if not budget_box:
            raise APIError('BudgetBox not found', HTTPStatus.NO_CONTENT)
        if not budget_category:
            raise APIError('BudgetCategory not found', HTTPStatus.NO_CONTENT)

        budget_box.remove_category(budget_category)

        budget_category.delete()
        return budget_box.to_json(), HTTPStatus.OK
    except Exception as e:
        raise e


def get_all_budget_category():
    budget_category_list = BudgetCategory.get_all()
    budget_category_dict = [budget_box.to_json() for budget_box in budget_category_list]

    return budget_category_dict if budget_category_dict else []


def update_budget_box_by_id(user_id, req):
    try:
        user = User.get(user_id)
        if user:
            user.update(**req)
            return user.to_json()
        raise APIError('User not found', HTTPStatus.NO_CONTENT)
    except Exception as e:
        raise e
