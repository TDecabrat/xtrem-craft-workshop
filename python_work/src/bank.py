"""The bank"""
from typing import Dict
from .currency import Currency
from .money import Money
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    """The bank"""

    def __init__(self, exchange_rate : Dict = {}) -> None:
        """
        The initial function

        :param exchange_rate: the exchange rate
        """
        self._exchange_rate : Dict[str, float] = exchange_rate
        self.pivot_curr : Currency = None

    @staticmethod
    def create(currency1: Currency, currency2: Currency, rate: float) -> "Bank":
        """
        Creates an exchange rate between two currencies

        :param currency1: the initial currency
        :param currency2: the currency to convert into
        :param rate: the rate of convertion
        """
        bank : Bank = Bank({})
        bank.add_echange_rate(currency1, currency2, rate)

        return bank

    def add_echange_rate(self, currency1: Currency, currency2: Currency, rate: float) -> None:
        """
        Adds an exchange rate between two currencies.

        :param currency1: the initial currency
        :param currency2: the currency to convert into
        :param rate: the rate of convertion
        """
        self._exchange_rate[f'{currency1.value}->{currency2.value}'] = rate
        self._exchange_rate[f'{currency2.value}->{currency1.value}'] = 1/rate

    def convert_money(self, amount: Money, currency1: Currency, currency2: Currency) -> float:
        """
        Converts a certain amount of money from one currency to another.

        :param amount: the amount of money to convert
        :param currency1: the initial currency
        :param currency2: the currency to convert into
        """
        return self.convert(amount.amount, currency1, currency2)

    def convert(self, amount: float, currency1: Currency, currency2: Currency) -> float:
        """
        Converts a certain amount of money from one currency to another.

        :param amount: the amount of money to convert
        :param currency1: the initial currency
        :param currency2: the currency to convert into
        """
        converted_amount : float = 0
        if currency1.value == currency2.value:
            converted_amount = amount
        elif f'{currency1.value}->{currency2.value}' in self._exchange_rate:
            converted_amount = (amount *
                                self._exchange_rate[f'{currency1.value}->{currency2.value}'])
        elif (self.pivot_curr and
              (f'{currency1.value}->{self.pivot_curr}' in self._exchange_rate) and
              f'{self.pivot_curr}->{currency2.value}' in self._exchange_rate):
            converted_amount = (amount *
                                self._exchange_rate[f'{currency1.value}->{self.pivot_curr}'] *
                                self._exchange_rate[f'{self.pivot_curr}->{currency2.value}'])
        else:
            raise MissingExchangeRateError(currency1, currency2)
        return converted_amount

    def add_pivot_currency(self, curr : Currency) -> bool:
        """
        Adds (or changes) the pivot currency
        """
        check : bool = False
        if curr in Currency:
            self.pivot_curr = curr
            check = True
        return check
