"""The databuilder"""
from typing import Dict
from ..src.bank import Bank
from ..src.currency import Currency

class BankDataBuilder:
    """The bank's databuilder"""
    _exchange_rate : Dict[str, float] = {}
    _pivot_currency = Currency.EUR

    def with_rates_for_currencies(self, curr : Currency,
                                  curr2 : Currency, rate : float) -> "BankDataBuilder":
        """
        Gives exchange rates
        
        :param curr: the initial currency
        :param curr2: the currency to convert into
        :param rate: the rate of convertion
        """
        self._exchange_rate[f'{curr.value}->{curr2.value}'] = rate
        self._exchange_rate[f'{curr2.value}->{curr.value}'] = 1/rate
        return self

    def with_pivot_currency(self, curr : Currency) -> "BankDataBuilder":
        """
        Sets the pivot currency
        
        :param curr: the pivot currency
        """
        self._pivot_currency = curr
        return self

    def build(self) -> Bank:
        """Create the data build of the bank"""
        return Bank(self._exchange_rate, self._pivot_currency)
