import tempfile
import json
from pathlib import Path
from app.services.account_service import get_account_by_id, load_accounts

FAKE_DATA = [
    { "id": "7299be1b-8506-4702-8eb9-c418761f2dcf", "name": "Test Account T1" },
    { "id": "d8867c4c-f0ed-4876-8391-3c982c378b12", "name": "Test Account T2" },
    { "id": "e95e7c0f-0a97-4e03-b9ec-826c6556df57", "name": "Test Account T3" }
]

def test_load_accounts_with_tempfile(monkeypatch):

    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        json.dump(FAKE_DATA, tmp)
        tmp_path = tmp.name

    monkeypatch.setattr("app.services.account_service.ACCOUNTS_PATH", Path(tmp_path))

    accounts = load_accounts()
    assert len(accounts) == 3
    assert accounts[0].name == "Test Account T1"
    assert accounts[1].name == "Test Account T2"
    assert accounts[2].name == "Test Account T3"

def test_load_accounts_file_not_found(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    monkeypatch.setattr("app.services.account_service.ACCOUNTS_PATH", Path(tmp_path))

    Path(tmp_path).unlink(missing_ok=True)
    
    try:
        load_accounts()
    except FileNotFoundError as e:
        assert str(e) == f"Accounts data file not found at {Path(tmp_path)}"
    else:
        assert False, "Expected FileNotFoundError was not raised"

def test_get_account_by_id(monkeypatch):

    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        json.dump(FAKE_DATA, tmp)
        tmp_path = tmp.name

    monkeypatch.setattr("app.services.account_service.ACCOUNTS_PATH", Path(tmp_path))

    account = get_account_by_id("7299be1b-8506-4702-8eb9-c418761f2dcf")
    assert account.name == "Test Account T1"

    try:
        get_account_by_id("non-existent-id")
    except ValueError as e:
        assert str(e) == "Account with ID non-existent-id not found"
    else:
        assert False, "Expected ValueError was not raised"
    
def test_get_account_by_id_file_not_found(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    monkeypatch.setattr("app.services.account_service.ACCOUNTS_PATH", Path(tmp_path))

    Path(tmp_path).unlink(missing_ok=True)

    try:
        get_account_by_id("7299be1b-8506-4702-8eb9-c418761f2dcf")
    except FileNotFoundError as e:
        assert str(e) == f"Accounts data file not found at {Path(tmp_path)}"
    else:
        assert False, "Expected FileNotFoundError was not raised"
    
def test_get_account_by_id_invalid_id(monkeypatch):
    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        json.dump(FAKE_DATA, tmp)
        tmp_path = tmp.name

    monkeypatch.setattr("app.services.account_service.ACCOUNTS_PATH", Path(tmp_path))

    try:
        get_account_by_id("invalid-uuid")
    except ValueError as e:
        assert str(e) == "Account with ID invalid-uuid not found"
    else:
        assert False, "Expected ValueError was not raised"
    
def test_get_account_by_id_empty_data(monkeypatch):
    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        json.dump([], tmp)
        tmp_path = tmp.name

    monkeypatch.setattr("app.services.account_service.ACCOUNTS_PATH", Path(tmp_path))

    try:
        get_account_by_id("7299be1b-8506-4702-8eb9-c418761f2dcf")
    except ValueError as e:
        assert str(e) == "Account with ID 7299be1b-8506-4702-8eb9-c418761f2dcf not found"
    else:
        assert False, "Expected ValueError was not raised"