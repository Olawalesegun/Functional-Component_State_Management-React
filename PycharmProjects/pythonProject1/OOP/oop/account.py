from decimal import Decimal


class Account:
    bonus = 40

    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative..")
        self.__balance = amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.name} {self.balance}"

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            self.__balance -= amount

    @classmethod
    def torin(cls, amount):
        cls.bonus = 100


account1 = Account("mariam", Decimal(100.000))
Account.bonus = 70
print(account1)
print(account1.bonus)
