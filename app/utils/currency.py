from typing import Dict
from app.schemas.transaction import CurrencyType

def exchange_rates() -> Dict[CurrencyType, float]:
    return {
        CurrencyType.gbp: 1.0,
        CurrencyType.eur: 1.15,
    }

def convert_currency(amount: int, from_currency: CurrencyType, to_currency: CurrencyType) -> int:
    rates = exchange_rates()

    if from_currency == to_currency:
        return amount

    if from_currency not in rates or to_currency not in rates:
        raise ValueError(f"Unsupported currency conversion from {from_currency} to {to_currency}")

    converted = amount * (rates[to_currency] / rates[from_currency])
    return int(round(converted))


def ensure_dual_currencies_in_totals(tx_totals: Dict[str, Dict[CurrencyType, int]]) -> None:
    currencies = {CurrencyType.gbp, CurrencyType.eur}

    for tx_type, totals in tx_totals.items():
        missing = currencies - totals.keys()
        for curr in missing:
            other = next(iter(currencies - {curr}))
            if other in totals:
                totals[curr] = convert_currency(totals[other], other, curr)


def ensure_dual_currencies_in_balance(balance: Dict[CurrencyType, int]) -> None:
    currencies = {CurrencyType.gbp, CurrencyType.eur}

    missing = currencies - balance.keys()
    for curr in missing:
        other = next(iter(currencies - {curr}))
        if other in balance:
            balance[curr] = convert_currency(balance[other], other, curr)
