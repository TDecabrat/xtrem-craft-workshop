"""Tests for the wallet"""
from copy import deepcopy
from ..src.currency import Currency
from ..src.bank import Bank
from ..src.wallet import Wallet

class TestWallet:
    """Tests for the wallet"""

    def test_add_multiple_devises(self):
        """ add multiple devises in the wallet"""
        # Arrange
        curr : Currency = Currency.EUR
        curr2 : Currency = Currency.USD
        curr3 : Currency = Currency.KRW
        amount : int = 10
        amount2 : int = 15
        amount3 : int = 5
        amount0 : int = 0
        bank : Bank = Bank()
        wallet : Wallet = Wallet(bank)

        # Act
        wallet.add_money(curr, amount)
        money_eur : float = wallet.get_amount_for_currency(curr)
        money_usd : float = wallet.get_amount_for_currency(curr2)
        money_krw : float = wallet.get_amount_for_currency(curr3)

        # Assert
        assert money_eur == 10
        assert money_usd == 0
        assert money_krw == 0

        # Act
        wallet.add_money(curr, amount2)
        wallet.add_money(curr2, amount3)
        wallet.add_money(curr3, amount0)
        money_eur = wallet.get_amount_for_currency(curr)
        money_usd = wallet.get_amount_for_currency(curr2)
        money_krw = wallet.get_amount_for_currency(curr3)

        # Assert
        assert money_eur == 25
        assert money_usd == 5
        assert money_krw == 0

    def test_evaluate_money_in_one_devise(self):
        """Checks if the evaluated money is correct"""
        # Arrange
        rate_eur_usd : float = 1.2
        rate_usd_eur : float = 1 / rate_eur_usd
        rate_usd_krw : float = 1100
        rate_krw_usd : float = 1 / rate_usd_krw
        rate_eur_krw : float = 1344
        rate_krw_eur : float = 1 / rate_eur_krw

        curr_eur : Currency = Currency.EUR
        curr_usd : Currency = Currency.USD
        curr_krw : Currency = Currency.KRW

        bank : Bank = Bank.create(curr_eur, curr_usd, rate_eur_usd) # EUR -> USD
        bank.add_echange_rate(curr_usd, curr_eur, rate_usd_eur) # USD -> EUR
        bank.add_echange_rate(curr_usd, curr_krw, rate_usd_krw) # USD -> KRW
        bank.add_echange_rate(curr_krw, curr_usd, rate_krw_usd) # KRW -> USD
        bank.add_echange_rate(curr_eur, curr_krw, rate_eur_krw) # EUR -> KRW
        bank.add_echange_rate(curr_krw, curr_eur, rate_krw_eur) # KRW -> EUR

        amount_eur : float = 10
        amount_usd : float = 9
        amount_krw : float = 7

        wallet1 : Wallet = Wallet(bank)
        wallet1.add_money(curr_eur, amount_eur)

        wallet2 : Wallet = deepcopy(wallet1)
        wallet2.add_money(curr_usd, amount_usd)

        wallet3 : Wallet = deepcopy(wallet2)
        wallet3.add_money(curr_krw, amount_krw)

        # Act
        money_eur_wal1 : float = wallet1.get_sums_in_currency(curr_eur)
        money_usd_wal1 : float = wallet1.get_sums_in_currency(curr_usd)
        money_krw_wal1 : float = wallet1.get_sums_in_currency(curr_krw)

        money_eur_wal2 : float = wallet2.get_sums_in_currency(curr_eur)
        money_usd_wal2 : float = wallet2.get_sums_in_currency(curr_usd)
        money_krw_wal2 : float = wallet2.get_sums_in_currency(curr_krw)

        money_eur_wal3 : float = wallet3.get_sums_in_currency(curr_eur)
        money_usd_wal3 : float = wallet3.get_sums_in_currency(curr_usd)
        money_krw_wal3 : float = wallet3.get_sums_in_currency(curr_krw)

        print(f"money_eur_wal1 : {money_eur_wal1}")
        print(wallet1.get_amount_for_currency(curr_eur))
        print(wallet1.get_amount_for_currency(curr_usd))
        print(wallet1.get_amount_for_currency(curr_krw))
        # Assert
        assert money_eur_wal1 == amount_eur
        assert money_usd_wal1 == bank.convert(amount_eur, curr_eur, curr_usd)
        assert money_krw_wal1 == bank.convert(amount_eur, curr_eur, curr_krw)

        assert money_eur_wal2 == amount_eur + bank.convert(amount_usd, curr_usd, curr_eur)
        assert money_usd_wal2 == amount_usd + bank.convert(amount_eur, curr_eur, curr_usd)
        assert money_krw_wal2 == (bank.convert(amount_eur, curr_eur, curr_krw)
                                  + bank.convert(amount_usd, curr_usd, curr_krw))

        assert money_eur_wal3 == (amount_eur + bank.convert(amount_usd, curr_usd, curr_eur)
                                  + bank.convert(amount_krw, curr_krw, curr_eur))
        assert money_usd_wal3 == (amount_usd + bank.convert(amount_eur, curr_eur, curr_usd)
                                  + bank.convert(amount_krw, curr_krw, curr_usd))
        assert money_krw_wal3 == (amount_krw + bank.convert(amount_eur, curr_eur, curr_krw)
                                  + bank.convert(amount_usd, curr_usd, curr_krw))
