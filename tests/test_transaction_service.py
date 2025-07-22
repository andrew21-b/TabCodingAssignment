import tempfile
import json
from pathlib import Path
from app.schemas.transaction import Transaction
from app.services.transaction_service import get_transactions_by_account, load_transactions

FAKE_DATA = [
        {
            "id": "T-01",
            "accountId": "44e2c7e6-bdd8-40fa-97ed-30d14da04b92",
            "amount": "1000",
            "currency": "GBP",
            "type": "Settled",
            "dateTime": "2021-04-20T12:08:25+00:00"
        },
        {
            "id": "T-02",
            "accountId": "805d10da-3f30-4987-9bff-50da0bec6879",
            "amount": "500",
            "currency": "EUR",
            "type": "Refunded",
            "dateTime": "2021-04-21T12:08:25+00:00"
        },
        {
            "id": "T-03",
            "accountId": "7299be1b-8506-4702-8eb9-c418761f2dcf",
            "amount": "2000",
            "currency": "GBP",
            "type": "Chargeback",
            "dateTime": "2021-04-22T12:08:25+00:00"
        },
        {
            "id": "T-04",
            "accountId": "7299be1b-8506-4702-8eb9-c418761f2dcf",
            "amount": "1500",
            "currency": "GBP",
            "type": "Settled",
            "dateTime": "2021-04-23T12:08:25+00:00"
        },
        {
            "id": "T-05",
            "accountId": "7299be1b-8506-4702-8eb9-c418761f2dcf",
            "amount": "3000",
            "currency": "GBP",
            "type": "Refunded",
            "dateTime": "2021-04-24T12:08:25+00:00"
        }
    ]

def test_load_transactions(monkeypatch):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        json.dump(FAKE_DATA, tmp)
        tmp_path = Path(tmp.name)


    monkeypatch.setattr("app.services.transaction_service.TRANSACTIONS_PATH", tmp_path)

    transactions = load_transactions()
    assert len(transactions) == 5
    assert isinstance(transactions[0], Transaction)
    assert transactions[0].id == "T-01"
    assert transactions[0].currency == "GBP"

def test_load_transactions_file_not_found(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = Path(tmp.name)

    monkeypatch.setattr("app.services.transaction_service.TRANSACTIONS_PATH", tmp_path)

    Path(tmp_path).unlink(missing_ok=True)

    try:
        load_transactions()
    except FileNotFoundError as e:
        assert str(e) == f"Transactions data file not found at {tmp_path}"
    else:
        assert False, "Expected FileNotFoundError was not raised"

def test_get_transactions_by_account(monkeypatch):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        json.dump(FAKE_DATA, tmp)
        tmp_path = Path(tmp.name)

    monkeypatch.setattr("app.services.transaction_service.TRANSACTIONS_PATH", tmp_path)

    transactions = get_transactions_by_account("7299be1b-8506-4702-8eb9-c418761f2dcf")

    assert len(transactions) == 3
    assert all(str(tx.accountId) == "7299be1b-8506-4702-8eb9-c418761f2dcf" for tx in transactions)
    assert transactions[0].type == "Chargeback"

def test_get_transactions_by_account_no_transactions(monkeypatch):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        json.dump([], tmp)
        tmp_path = Path(tmp.name)

    monkeypatch.setattr("app.services.transaction_service.TRANSACTIONS_PATH", tmp_path)

    transactions = get_transactions_by_account("7299be1b-8506-4702-8eb9-c418761f2dcf")

    assert len(transactions) == 0