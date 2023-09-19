"""The error for a missing exchange rate"""
from .currency import Currency


class MissingExchangeRateError(Exception):
    """The error for a missing exchange rate"""
    def __init__(self, currency1: Currency, currency2: Currency) -> None:
        super().__init__(f'{currency1.value}->{currency2.value}')
