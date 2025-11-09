# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Umoja AI"
    app_version: str = "1.0.0"
    database_url: str = "sqlite+aiosqlite:///./umoja_ai.db"
    
    # Supported Kenyan languages
    supported_languages: list[str] = [
        "sw",  # Swahili
        "en",  # English
        "ki",  # Kikuyu
        "lu",  # Luhya
        "luo", # Luo
        "kam", # Kamba
    ]
    
    class Config:
        env_file = ".env"

settings = Settings()