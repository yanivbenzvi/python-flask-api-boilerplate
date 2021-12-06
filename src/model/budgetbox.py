from src.model.budget_categorie import BudgetCategory


class BudgetBox:
    """
    Class for a budget box.
    """

    def __init__(self, amount):
        self.amount = amount
        self.categories = []

    def get_total_amount(self) -> float:
        """
        Returns the total amount of the budget box.
        :return:
        """
        total = 0
        for category in self.categories:
            total += category.budget
        return total

    def add_category(self, category_name, amount=0):
        """
        Adds a category to the budget box.
        :param category_name: str
        :param amount: float
        :raise Exception: if there is no budget left
        """
        if self.get_total_amount() + amount > self.amount:
            raise Exception("Budget is over")
        self.categories.append(BudgetCategory(category_name, amount))

    def get_categories_name(self) -> list[str]:
        """
        Returns a list of the names of the categories.
        :return: list[str]
        """
        return [category.name for category in self.categories]

    def withdraw_from_category(self, category_name, amount):
        """
        Withdraws the given amount from the given category.
        :param category_name: str
        :param amount: float
        :raise Exception: if category does not exist or if there is no budget left
        """
        category_object = list(filter(lambda x: x.name == category_name, self.categories))
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
        category_object = list(filter(lambda x: x.name == category_name, self.categories))
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
            categories_string = ''.join([str(category) for category in self.categories])

        return f"\tBudgetBox: {self.amount}\n" \
               f"\t\tCategories: {categories_string}"
