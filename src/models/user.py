from typing import List

from src.models.budgetbox import BudgetBox
import uuid

from src.models.entity import EntityModel
from src.utility import MemoryDbStore


class User(EntityModel):
    """
    User class
    """

    def __init__(self, username: str, budget_amount: float):
        """
        Initializes a user
        :param username: str
        :param budget_amount: float
        """
        super().__init__()
        self.username = username
        self.budget = BudgetBox(budget_amount)

    def get_categories_name(self) -> List[str]:
        """
        Returns a list of all categories in the user's budget
        :return: list[str]
        """
        return self.budget.get_categories_name()

    def __str__(self) -> str:
        """
        Returns a string representation of the user
        :return: str
        """
        return f"User Information: \n" \
               f"\tUsername: {self.username}\n" \
               f"\tID: {self.id}\n" \
               f"\tBudget: {self.budget}\n"

    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the user
        :return: dict
        """
        return {
            **super().to_json(),
            "username": self.username,
            "budget": self.budget.to_json()
        }

    def update(self, username: str):
        """
        Updates a user's username and budget amount
        :param username: str
        :param budget_amount: float
        """
        self.username = username