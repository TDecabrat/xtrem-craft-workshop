"""The tests for the money"""
from ..src.currency import Currency
from ..src.money import Money
from ..src.money_calculator import MoneyCalculator

class TestMoneyCalculator:
    """The tests for the money"""

    def test_add_in_usd_returns_value(self):
        """the test to add money from a different currency"""
        #Arrange
        amount : Money = Money(5.0, Currency.USD)
        amount2 : Money = Money(10.0, Currency.USD)

        #Act
        res = MoneyCalculator.add(amount, amount2)

        #Assert
        assert res is not None
        assert isinstance(res, float)
        assert res == 15

    def test_multiply_in_euros_returns_positive_number(self):
        """the test for checking that multipling money works"""
        #Arrange
        amount : Money = Money(5.0, Currency.EUR)
        amount2 : int = 2

        #Act
        res = MoneyCalculator.times(amount, amount2)

        #assert
        assert res == 10

    def test_divide_in_korean_won_returns_float(self):
        """the test for checking that dividing money works"""
        #Arrange

        amount : Money = Money(4002.0, Currency.KRW)
        amount2 : int = 4

        #Act
        res = MoneyCalculator.divide(amount, amount2)

        #assert
        assert res == 1000.5
