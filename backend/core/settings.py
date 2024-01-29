from pydantic.v1.env_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite://db.sqlite"
