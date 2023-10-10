"""Tests for the bank"""
import pytest

from ..src.bank import Bank
from ..src.currency import Currency
from ..src.missing_exchange_rate_error import MissingExchangeRateError
from .bank_data_builder import BankDataBuilder


class TestBank:
    """Tests for the bank"""
    def test_convert_euro_to_usd_returns_correct_amount_regarding_rate(self):
        """
        Tests for convertions : check correct amount
        """
        #Arrange
        rate : float = 1.2
        curr : Currency = Currency.EUR
        curr2 : Currency = Currency.USD
        amount : int = 10
        bank : Bank = (BankDataBuilder()
                      .with_rates_for_currencies(curr, curr2, rate)
                      .build())

        #Act
        res = bank.convert(amount, curr, curr2)

        #Assert
        assert res == 12

    def test_convert_euro_to_usd_returns_same_value(self):
        """Tests for convertions of the same currency"""
        #Arrange
        rate : float = 1.2
        curr : Currency = Currency.EUR
        curr2 : Currency = Currency.USD
        amount : int = 10
        bank : Bank = (BankDataBuilder()
                      .with_rates_for_currencies(curr, curr2, rate)
                      .build())

        #Act
        res = bank.convert(amount, curr, curr)

        #Assert
        assert res == 10

    def test_convert_with_missing_exchange_rate_throws_exception(self):
        """Tests for convertions error"""
        #Arrange
        rate : float = 1.2
        curr : Currency = Currency.EUR
        curr2 : Currency = Currency.USD
        curr3 : Currency = Currency.KRW
        amount : int = 10
        bank : Bank = (BankDataBuilder()
                      .with_rates_for_currencies(curr, curr2, rate)
                      .build())

        #Act
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(amount, curr, curr3)

        #Assert
        assert str(error.value) == "EUR->KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self):
        """
        Tests the conversion between two exchange rates
        """
        #Arrange
        eur: Currency = Currency.EUR
        usd: Currency = Currency.USD
        rate: float = 1.2
        money : int = 10
        bank: Bank = (BankDataBuilder()
                      .with_rates_for_currencies(eur, usd, rate)
                      .build())

        #Act
        res = bank.convert(money, eur, usd)

        #Assert
        assert res == 12

        #Arrange
        new_rate: float = 1.3

        #Act
        bank.add_exchange_rate(eur, usd, new_rate)
        res2 = bank.convert(money, eur, usd)

        #Assert
        assert res2 == 13

    def test_convert_back(self):
        """
        Tests if converting back and forth gives the correct amount of money
        """
        #Arrange
        rate_eur_usd : float = 1.2
        rate_usd_krw : float = 1100
        curr : Currency = Currency.EUR
        curr2 : Currency = Currency.USD
        curr3 : Currency = Currency.KRW
        amount : int = 10
        bank : Bank = (BankDataBuilder()
                       .with_pivot_currency(curr2)
                       .with_rates_for_currencies(curr, curr2, rate_eur_usd)
                       .with_rates_for_currencies(curr2, curr3, rate_usd_krw)
                       .build())

        #Act
        res = bank.convert(amount, curr, curr2)
        res = bank.convert(res, curr2, curr)

        res2 = bank.convert(amount, curr, curr3)
        res2 = bank.convert(res2, curr3, curr)

        #Assert
        assert res == amount
        assert res2 == amount
