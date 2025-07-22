import pytest
from uuid import UUID
from datetime import datetime
from app.schemas.transaction import Transaction, TransactionType, CurrencyType
from app.schemas.account import Account, TransactionSummaryResponse
from app.services.summary_service import compute_summary, get_account_by_id


@pytest.fixture
def mock_account():
    return Account(id=UUID("7299be1b-8506-4702-8eb9-c418761f2dcf"), name="TEST ACCOUNT 1")


@pytest.fixture
def mock_transactions():
    return [
        Transaction(
            id="T-01",
            accountId=UUID("7299be1b-8506-4702-8eb9-c418761f2dcf"),
            amount=100000,
            currency=CurrencyType.gbp,
            type=TransactionType.settled,
            dateTime=datetime(2021, 4, 20, 12, 8, 25, 0, tzinfo=None)
        ),
        Transaction(
            id="T-02",
            accountId=UUID("7299be1b-8506-4702-8eb9-c418761f2dcf"),
            amount=200000,
            currency=CurrencyType.eur,
            type=TransactionType.settled,
            dateTime=datetime(2021, 4, 21, 13, 8, 25, 0, tzinfo=None)
        ),
        Transaction(
            id="T-03",
            accountId=UUID("7299be1b-8506-4702-8eb9-c418761f2dcf"),
            amount=30000,
            currency=CurrencyType.gbp,
            type=TransactionType.chargeback,
            dateTime=datetime(2021, 4, 22, 13, 8, 25, 0, tzinfo=None)
        ),
    ]


def test_compute_summary_returns_correct_data(monkeypatch, mock_account, mock_transactions):
    def fake_get_account_by_id(account_id: str):
        return mock_account

    def fake_get_transactions_by_account(account_id: str):
        return mock_transactions

    monkeypatch.setattr("app.services.summary_service.get_account_by_id", fake_get_account_by_id)
    monkeypatch.setattr("app.services.summary_service.get_transactions_by_account", fake_get_transactions_by_account)


    result = compute_summary(mock_account.id)

    assert result.account.id == mock_account.id
    assert result.account.name == mock_account.name


    assert result.transactions["settled"][CurrencyType.gbp] == 100000
    assert result.transactions["settled"][CurrencyType.eur] == 200000

    assert result.transactions["chargeback"][CurrencyType.gbp] == 30000
    assert CurrencyType.eur in result.transactions["chargeback"]

    assert result.balance[CurrencyType.gbp] == 70000
    assert result.balance[CurrencyType.eur] > 0


def test_compute_summary_missing_account(monkeypatch):
    def fake_get_account_by_id(account_id: str):
        return None

    monkeypatch.setattr("app.services.summary_service.get_account_by_id", fake_get_account_by_id)
    monkeypatch.setattr("app.services.summary_service.get_transactions_by_account", lambda account_id: [])

    result = compute_summary(UUID("7299be1b-8506-4702-8eb9-c418761f2dcf"))
    assert result == TransactionSummaryResponse(account=Account(id=UUID('00000000-0000-0000-0000-000000000000'), name='Unknown'), transactions={}, balance={})

def test_compute_summary_no_transactions(monkeypatch, mock_account):
    def fake_get_account_by_id(account_id: str):
        return mock_account

    def fake_get_transactions_by_account(account_id: str):
        return []

    monkeypatch.setattr("app.services.summary_service.get_account_by_id", fake_get_account_by_id)
    monkeypatch.setattr("app.services.summary_service.get_transactions_by_account", fake_get_transactions_by_account)

    result = compute_summary(mock_account.id)

    assert result.account.id == mock_account.id
    assert result.account.name == mock_account.name
    assert result.transactions == {}
    assert result.balance == {}