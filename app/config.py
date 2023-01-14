from pydantic import BaseSettings


class Settings(BaseSettings):
    db_password: str
    db_user: str
    db_host: str
    db_name: str


settings = Settings()
