from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from config import DB_URL, ALGORITHM, JWT_SECRET, API_V1_STR


class Settings(BaseSettings):
    API_V1_STR: str = API_V1_STR
    DB_URL: str = DB_URL
    DBBaseModel = declarative_base()

    JWT_SECRET: str = JWT_SECRET
    ALGORITHM: str = ALGORITHM

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
