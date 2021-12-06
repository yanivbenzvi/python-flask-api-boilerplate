from src.model.budgetbox import BudgetBox
import uuid


class User:
    """
    User class
    """
    def __init__(self, username, budget_amount):
        """
        Initializes a user
        :param username: str
        :param budget_amount: float
        """
        self.id = uuid.uuid4()
        self.username = username
        self.budget = BudgetBox(budget_amount)

    def get_categories_name(self) -> list[str]:
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
