from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tab Coding Assignment"
    VERSION: str = "1.0"
    ACCOUNTS_DATA_PATH: str = "../data/accounts.json"
    TRANSACTIONS_DATA_PATH: str = "../data/transactions.json"


settings = Settings()