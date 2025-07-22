from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tab Coding Assignment"
    VERSION: str = "1.0"


settings = Settings()