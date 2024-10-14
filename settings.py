from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "City Temperature Management API"

    DATABASE_URL: str = "sqlite+aiosqlite:///./cities_temperature.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
