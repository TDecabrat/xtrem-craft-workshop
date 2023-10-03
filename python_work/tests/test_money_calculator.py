"""The tests for the money"""
from ..src.currency import Currency
from ..src.money_calculator import MoneyCalculator

class TestMoneyCalculator:
    """The tests for the money"""

    def test_add_in_usd_returns_value(self):
        """the test to add money from a different currency"""
        #Arrange
        amount : int = 5
        curr : Currency = Currency.USD
        amount2 : int = 10

        #Act
        res = MoneyCalculator.add(amount, curr, amount2)

        #Assert
        assert res is not None
        assert isinstance(res, float)

    def test_multiply_in_euros_returns_positive_number(self):
        """the test for checking that multipling money works"""
        #Arrange
        amount : int = 10
        curr : Currency = Currency.EUR
        amount2 : int = 2

        #Act
        res = MoneyCalculator.times(amount, curr, amount2)

        #assert
        assert res > 0

    def test_divide_in_korean_won_returns_float(self):
        """the test for checking that dividing money works"""
        #Arrange
        amount : int = 4002
        curr : Currency = Currency.KRW
        amount2 : int = 4

        #Act
        res = MoneyCalculator.divide(amount, curr, amount2)

        #assert
        assert res == 1000.5
