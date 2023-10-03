"""The currency"""
from enum import Enum

class Currency(Enum):
    """
    The different currencies
    """
    USD = "USD"
    EUR = "EUR"
    KRW = "KRW"

    def __eq__(self, other):
        """The equal function"""
        return self.value == other.value
