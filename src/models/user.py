import uuid
from uuid import UUID

from src.models.entity import EntityModel


class User(EntityModel):
    """
    User class
    """

    def __init__(self, username: str, budget_id: UUID = None):
        """
        Initializes a user
        :param username: str
        :param budget_id: UUID
        """
        super().__init__()
        self.username = username
        self.budget_id = None

    def __str__(self) -> str:
        """
        Returns a string representation of the user
        :return: str
        """
        return f"User Information: \n" \
               f"\tUsername: {self.username}\n" \
               f"\tID: {self.id}\n" \
               f"\tBudget_id: {self.budget_id}\n"

    def set_budget_box_id(self, budget_id: UUID):
        """
        Sets the budget box id of the user
        :param budget_id: str
        """
        self.budget_id = budget_id

    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the user
        :return: dict
        """
        return {
            **super().to_json(),
            "username": self.username,
            "budget_id": str(self.budget_id)
        }

    def update(self, username: str):
        """
        Updates a user's username and budget amount
        :param username: str
        """
        self.username = username
