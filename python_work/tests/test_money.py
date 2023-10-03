""" The tests for the money module."""

from ..src.money import Money
from ..src.currency import Currency

class TestMoney:
    """ Test money """

    def test_create_money_positive(self):
        """ Money is only positive """

        # Arrange
        curr : Currency = Currency.EUR
        money : Money = Money(10, curr)
        money2 : Money = Money(-10, curr)
        # Act

        # Assert
        assert money.amount == 10
        assert money.currency == Currency.EUR
        assert money2.amount == 0
        assert money2.currency == Currency.EUR

    def test_add_money(self):
        """ test add money """

        # Arrange
        curr : Currency = Currency.EUR
        money1 : Money = Money(10, curr)
        money2 : Money = Money(20, curr)

        # Act
        money1.add_money(money2.amount)

        # Assert
        assert money1 == Money(30, curr)
