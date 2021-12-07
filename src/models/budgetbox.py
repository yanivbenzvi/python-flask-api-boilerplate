from typing import List

from src.models.budget_category import BudgetCategory
from src.models.entity import EntityModel


class BudgetBox(EntityModel):
    """
    Class for a budget box.
    """

    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        self.categories_id_list = []

    def get_total_amount(self) -> float:
        """
        Returns the total amount of the budget box.
        :return:
        """
        total = 0
        categories_object = self.get_categories_object()

        for category in categories_object:
            total += category.budget
        return total

    def add_category(self, budget_category_object: BudgetCategory):
        """
        Adds a category to the budget box.
        :param budget_category_object: BudgetCategory
        :raise Exception: if there is no budget left
        """
        if self.get_total_amount() + budget_category_object.amount > self.amount:
            raise Exception("Budget is over")
        self.categories_id_list.append(str(budget_category_object.id))

    def remove_category(self, budget_category):
        """
        Removes the given category from the budget box.
        :param budget_category: BudgetCategory
        :raise Exception: if category does not exist
        """
        category_id = str(budget_category.id)
        self.categories_id_list.remove(category_id)

    def get_categories_object(self):
        return [self.get(category_id) for category_id in self.categories_id_list]

    def get_categories_name(self) -> List[str]:
        """
        Returns a list of the names of the categories.
        :return: list[str]
        """
        return [category.name for category in self.get_categories_object()]

    def withdraw_from_category(self, category_name, amount):
        """
        Withdraws the given amount from the given category.
        :param category_name: str
        :param amount: float
        :raise Exception: if category does not exist or if there is no budget left
        """
        categories_object = [self.get(category_id) for category_id in self.categories_id_list]

        category_object = list(filter(lambda x: x.name == category_name, self.get_categories_object()))
        category_object = category_object[0] if len(category_object) else None

        if not category_object:
            raise Exception("Category not found")
        if self.amount - amount < 0:
            raise Exception("there is not enough money")

        self.amount -= amount
        category_object.withdraw(amount)

    def deposit_to_category(self, category_name, amount):
        """
        Deposits the given amount to the given category.
        :param category_name: str
        :param amount: float
        :raise Exception: if category does not exist or if there is no budget left
        """
        category_object = list(filter(lambda x: x.name == category_name, self.get_categories_object()))
        category_object = category_object[0] if len(category_object) else None

        if not category_object:
            raise Exception("Category not found")
        if self.amount + amount > self.amount:
            raise Exception("Budget is over")

        self.amount -= amount
        category_object.deposite(amount)

    def __str__(self):
        """
        Returns a string representation of the object.
        :return: string representation of the object
        :return: str
        """
        if len(self.categories) == 0:
            categories_string = "No categories"
        else:
            categories_string = ''.join([str(category) for category in self.get_categories_object()])

        return f"\tBudgetBox: {self.amount}\n" \
               f"\t\tCategories: {categories_string}"

    def to_json(self) -> dict:
        """
        Returns a json representation of the object.
        :return: json representation of the object
        :return: dict
        """
        return {
            **super().to_json(),
            "amount": self.amount,
            "categories": self.categories_id_list
        }

    def get_budget_categories_list(self) -> List[BudgetCategory]:
        return [BudgetCategory.get(category_id) for category_id in self.categories_id_list]
