"""The bank"""
from typing import Dict
from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    """The bank"""
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate = {}) -> None:
        """
        The initial function

        :param exchange_rate: the exchange rate
        """
        self._exchange_rate = exchange_rate

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

    def convert(self, amount: float, currency1: Currency, currency2: Currency) -> float:
        """
        Converts a certain amount of money from one currency to another.

        :param amount: the amount of money to convert
        :param currency1: the initial currency
        :param currency2: the currency to convert into
        """
        if not (currency1.value == currency2.value or
                f'{currency1.value}->{currency2.value}' in self._exchange_rate):
            raise MissingExchangeRateError(currency1, currency2)

        if currency1.value == currency2.value:
            return amount
        else:
            return amount * self._exchange_rate[f'{currency1.value}->{currency2.value}']
