from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    PROJECT_NAME : str = "Taskflow"
    VERSION : str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Setting()