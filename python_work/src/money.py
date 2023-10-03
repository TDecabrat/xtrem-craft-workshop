"""The money"""
from .currency import Currency

class Money:
    """ the money class """

    def __init__(self, amount: float, currency: Currency) -> None:
        """
        The initial function

        :param exchange_rate: the exchange rate
        """
        self.currency: Currency = currency
        if amount >= 0 :
            self.amount: float = amount
        else:
            self.amount: float = 0

    def add_money(self, amount : float) -> bool:
        """
        Adds money

        :param amount: the amount of money to add
        """
        new_amount : float = self.amount + amount
        check : bool = True
        if new_amount >= 0:
            self.amount = new_amount
        else:
            print("The amount of money is below 0, having clients in debt"\
                   "isn't part of our policy.")
            check = False
        return check

    def change_currency(self, new_currency : Currency, rate : float) -> None:
        """
        Converts the money to another currency
        """
        self.currency = new_currency
        self.amount *= rate

    def add_mix_money(self, money : "Money") -> bool:
        """
        Adds money

        :param money: the money to add
        """
        check : bool = True
        if self.currency == money.currency:
            new_amount : float = self.amount + money.amount
            if new_amount >= 0:
                self.amount = new_amount
                money.amount = 0
            else:
                print("The amount of money is below 0, having clients in debt"\
                    "isn't part of our policy.")
                check = False
        else:
            print("The different moneys aren't of the same currency. Please change one.")
            check = False
        return check

    def show_money(self) -> None:
        """
        Shows the amount of money
        """
        print(f"{self.amount} {self.currency}")

    def __eq__(self, obj):
        return (isinstance(obj, Money) and
                obj.amount == self.amount and
                obj.currency == self.currency)
