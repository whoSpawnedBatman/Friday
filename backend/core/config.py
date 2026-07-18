"""
Friday Backend — Core Configuration

Loads environment variables and provides typed settings
for the entire application via Pydantic BaseSettings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "Friday"
    app_env: str = "development"
    debug: bool = True

    # Database
    database_url: str = "postgresql+asyncpg://postgres:password@localhost:5432/friday"

    # AI
    openai_api_key: str = ""

    # Security
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 1440  # 24 hours

    # CORS
    frontend_url: str = "http://localhost:3000"

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


# Singleton instance
settings = Settings()
