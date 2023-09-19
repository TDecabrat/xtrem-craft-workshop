"""The money calculator"""
from .currency import Currency


class MoneyCalculator:
    """The money calculator"""
    @staticmethod
    def add(amount: float, currency: Currency, amount2: float) -> float:
        """
        Adds two currencies together

        :param amount: First value to add
        :param currency: Currency that we will be working with
        :param amount2: Second value to add

        :return Sum of amount and amount2
        """
        return float(amount + amount2)

    @staticmethod
    def times(amount: float, currency: Currency, amount2: int) -> float:
        """
        Multiplies two currencies together

        :param amount: First value to multiply with
        :param currency: Currency that we will be working with
        :param amount2: Second value to multiply with

        :return Product of amount and multiply with
        """
        return amount * amount2

    @staticmethod
    def divide(amount: float, currency: Currency, amount2: int) -> float:
        """
        Divides two currencies together

        :param amount: First value to divide by
        :param currency: Currency that we will be working with
        :param amount2: Second value to divide with

        :return 
        quotient of amount/amount2
        """
        return amount / amount2
