"""The money calculator"""
from .money import Money


class MoneyCalculator:
    """The money calculator"""
    @staticmethod
    def add(amount: Money, amount2: Money) -> float:
        """
        Adds two currencies together

        :param amount: First value to add
        :param amount2: Second value to add

        :return Sum of amount and amount2
        """
        return amount.amount + amount2.amount

    @staticmethod
    def times(amount: Money, amount2: int) -> float:
        """
        Multiplies two currencies together

        :param amount: First value to multiply with
        :param amount2: Second value to multiply with

        :return Product of amount and multiply with
        """
        return amount.amount * amount2

    @staticmethod
    def divide(amount: Money, amount2: int) -> float:
        """
        Divides two currencies together

        :param amount: First value to divide by
        :param amount2: Second value to divide with

        :return 
        quotient of amount/amount2
        """
        return amount.amount / amount2
