from collections import defaultdict
from uuid import UUID
from app.schemas.account import Account, TransactionSummaryResponse
from app.schemas.transaction import CurrencyType, TransactionType
from app.services.account_service import get_account_by_id
from app.services.transaction_service import get_transactions_by_account
from app.utils.currency import ensure_dual_currencies_in_balance, ensure_dual_currencies_in_totals

def compute_summary(account_id: UUID) -> TransactionSummaryResponse:
    account = get_account_by_id(str(account_id))
    if not account:
        return TransactionSummaryResponse(account=Account(id=UUID(int=0), name="Unknown"), transactions={}, balance={})

    transactions = get_transactions_by_account(str(account.id))

    tx_totals = defaultdict(lambda: defaultdict(int))
    balance = defaultdict(int)

    for tx in transactions:
        amount = int(tx.amount)
        tx_type = tx.type.value.lower()
        currency = tx.currency

        tx_totals[tx_type][currency] += amount

        if tx.type == TransactionType.settled:
            balance[currency] += amount
        elif tx.type in {TransactionType.refunded, TransactionType.chargeback}:
            balance[currency] -= amount


    ensure_dual_currencies_in_totals(tx_totals)
    ensure_dual_currencies_in_balance(balance)

    return TransactionSummaryResponse(
        account=account,
        transactions=tx_totals,
        balance=balance
    )

