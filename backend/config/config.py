from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGODB_URL : str
    DATABASE_NAME : str
    SECRET_KEY : str

    model_config = SettingsConfigDict(env_file="../.env")

settings = Settings()