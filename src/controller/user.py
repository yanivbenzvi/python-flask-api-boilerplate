from http import HTTPStatus

from src import APIError
from src.models.user import User


def create_user(req):
    try:
        user = User(**req)
        user.save()
        return user.to_json(), HTTPStatus.CREATED
    except Exception as e:
        return e


def get_user_by_id(user_id):
    try:
        user = User.get(user_id)
        if user:
            return user.to_json()
        raise APIError('User not found', HTTPStatus.NOT_FOUND)
    except Exception as e:
        raise e


def delete_user_by_id(user_id):
    try:
        user = User.get(user_id)
        if user:
            user.delete()
            return user.to_json(), HTTPStatus.OK
        raise APIError('User not found', HTTPStatus.NO_CONTENT)
    except Exception as e:
        raise e


def get_all_user():
    user_list = User.get_all()
    user_dict = [user.to_json() for user in user_list]

    return user_dict if user_dict else []


def update_user_by_id(user_id, req):
    try:
        user = User.get(user_id)
        if user:
            user.update(**req)
            return user.to_json()
        raise APIError('User not found', HTTPStatus.NO_CONTENT)
    except Exception as e:
        raise e
