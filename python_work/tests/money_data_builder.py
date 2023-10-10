"""Money data builder"""
from ..src.money import Money
from ..src.currency import Currency
class MoneyBuilder:
    """Money builder"""
    _amount : int = 0
    _currency : Currency = Currency.USD

    def with_amount(self, amount : int) -> "MoneyBuilder":
        """
        Gives an amount
        
        :param amount: the amount
        """
        self._amount = amount
        return self

    def with_currency(self, curr : Currency) -> "MoneyBuilder":
        """
        Gives a currency
        
        :param curr: the currency
        """
        self._currency = curr
        return self

    def build(self) -> Money:
        """Builds"""
        return Money(self._amount, self._currency)
