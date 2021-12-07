class BudgetCategory:
    def __init__(self, name: str, amount: float):
        """
        Initialize a new budget category
        :param name: str
        :param amount: float
        """
        self.name = name
        self.amount = amount

    def withdraw(self, amount: float):
        """
        Withdraw money from the budget category
        :param amount: float
        :raise : ValueError if the amount is greater than the budget category amount
        """
        if amount > self.amount:
            raise ValueError(f"Not enough money in {self.name} category")
        self.amount -= amount

    def deposit(self, amount: float):
        """
        Deposit money to the budget category
        :param amount: str
        """
        self.amount += amount

    def __str__(self) -> str:
        """
        Return a string representation of the budget category
        :return: str
        """
        return f"\t\tCategory name: {self.name} \t Category Amount {self.amount}\n"

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "amount": self.amount
        }

