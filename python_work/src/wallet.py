from typing import Dict
from .currency import Currency
from .bank import Bank
from .missing_exchange_rate_error import MissingExchangeRateError

class Wallet:
    """The wallet"""
    _wallets: Dict[Currency, float] = {}
    linked_bank: Bank = None

    def __init__(self, bank) -> None:
        """The initial function"""
        for currency in Currency:
            self._wallets[currency] = 0

        self.linked_bank = bank

    def add_money(self, currency, val) -> None:
        """Adds money in the wallet from a certain currency"""
        if currency not in Currency:
            print("Error : This currency is not recognized by the system.")
        else:
            self._wallets[currency] += val

    def get_amount_for_currency(self, currency) -> float:
        """Gives the amount of money stored for a currency"""
        return self._wallets[currency]

    def get_sums_in_currency(self, target_currency) -> float:
        """Gets the sum"""
        if target_currency in Currency:
            sum_currencies : float = 0
            for curr_type in self._wallets.copy():
                try:
                    if curr_type != target_currency :
                        sum_currencies += self.linked_bank.convert(self._wallets[curr_type],
                                                                curr_type, target_currency)
                    else :
                        sum_currencies += self._wallets[curr_type]
                except MissingExchangeRateError:
                    print(f"We couldn't convert the amount of money from {curr_type} " /
                          f"to {target_currency}, and thus ignored it.")
            return sum_currencies
        else:
            print("Currency given was not found.")
            return None
