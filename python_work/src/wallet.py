from typing import List
from .currency import Currency
from .bank import Bank
from .money import Money
from .missing_exchange_rate_error import MissingExchangeRateError

class Wallet:
    """The wallet"""

    def __init__(self, bank : Bank) -> None:
        """The initial function"""
        self._moneys: List[Money] = []
        for curr in Currency:
            self._moneys.append(Money(0, curr))

        self.linked_bank: Bank = bank

    def add_money(self, currency : Currency, val : float) -> None:
        """Adds money in the wallet from a certain currency"""

        money : Money = self.get_amount_for_currency(currency)
        if money is None:
            self._moneys.append(Money(val, currency))
        else:
            money.add_money(val)

    def get_amount_for_currency(self, currency : Currency) -> Money:
        """Gives the amount of money stored for a currency"""
        for money in self._moneys:
            if money.currency == currency:
                return money
        return None

    def get_sums_in_currency(self, target_currency : Currency) -> float:
        """Gets the sum"""
        sum_currencies : float = 0
        if target_currency in Currency:
            for money in self._moneys.copy():
                try:
                    if money.currency != target_currency :
                        sum_currencies += self.linked_bank.convert(money.amount,
                                                                money.currency, target_currency)
                    else :
                        sum_currencies += money.amount
                except MissingExchangeRateError:
                    print(f"We couldn't convert the amount of money from {money.currency} " /
                          f"to {target_currency}, and thus ignored it.")
        else:
            print("Currency given was not found.")
            sum_currencies = None
        return sum_currencies
