import pytest
from app.utils.currency import (
    convert_currency,
    ensure_dual_currencies_in_totals,
    ensure_dual_currencies_in_balance,
)
from app.schemas.transaction import CurrencyType


def test_convert_same_currency():
    amount = 1000
    result = convert_currency(amount, CurrencyType.gbp, CurrencyType.gbp)
    assert result == 1000


def test_convert_gbp_to_eur():
    amount = 1000
    result = convert_currency(amount, CurrencyType.gbp, CurrencyType.eur)
    assert result == 1150


def test_convert_eur_to_gbp():
    amount = 1150
    result = convert_currency(amount, CurrencyType.eur, CurrencyType.gbp)
    assert result == 1000


def test_convert_invalid_currency():
    class FakeCurrency(str):
        pass

    with pytest.raises(ValueError):
        convert_currency(1000, FakeCurrency("JPY"), CurrencyType.gbp)


def test_ensure_dual_currencies_in_totals_adds_missing():
    tx_totals = {
        "settled": {CurrencyType.gbp: 1000},
        "refunded": {CurrencyType.eur: 2300}
    }

    ensure_dual_currencies_in_totals(tx_totals)

    assert tx_totals["settled"][CurrencyType.eur] == 1150
    assert tx_totals["refunded"][CurrencyType.gbp] == 2000


def test_ensure_dual_currencies_in_balance_adds_missing():
    balance = {
        CurrencyType.gbp: 3000
    }

    ensure_dual_currencies_in_balance(balance)

    assert balance[CurrencyType.eur] == 3450


def test_balance_both_present_unchanged():
    balance = {
        CurrencyType.gbp: 2000,
        CurrencyType.eur: 2300
    }

    ensure_dual_currencies_in_balance(balance)

    assert balance[CurrencyType.gbp] == 2000
    assert balance[CurrencyType.eur] == 2300
