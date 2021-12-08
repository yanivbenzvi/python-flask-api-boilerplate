from http import HTTPStatus

from src import APIError
from src.models.budget_category import BudgetCategory
from src.models.budgetbox import BudgetBox
from src.models.user import User


def create_user(req):
    user = User(**req)
    user.save()
    return user.to_json(), HTTPStatus.CREATED


def get_user_by_id(user_id):
    user = User.get(user_id)
    if user:
        return user.to_json()
    raise APIError('User not found', HTTPStatus.NOT_FOUND)


def delete_user_by_id(user_id):
    user = User.get(user_id)

    if not user:
        raise APIError('User not found', HTTPStatus.NO_CONTENT)

    budget_id = user.budget_id
    budget_box = BudgetBox.get(budget_id)
    if budget_box:
        categories_id_list = budget_box.categories_id_list
        budget_box.delete()
        categories_object_list = [BudgetCategory.get(category_id) for category_id in categories_id_list]
        [category_object.delete() for category_object in categories_object_list]

    user.delete()
    return user.to_json(), HTTPStatus.OK


def get_all_user():
    user_list = User.get_all()
    user_dict = [user.to_json() for user in user_list]

    return user_dict if user_dict else []


def update_user_by_id(user_id, req):
    user = User.get(user_id)
    if not user:
        raise APIError('User not found', HTTPStatus.NO_CONTENT)

    user.update(**req)
    user.save()

    return user.to_json()
