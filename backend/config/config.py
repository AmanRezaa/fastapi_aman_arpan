from pydantic import ValidationError
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import sys

# Check for .env file
env_path = Path(".env")

if env_path.exists():
    load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    DATABASE_URL_CLOUD: str
    SECRET_KEY: str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int


    class Config:
        env_file = ".env"  # Will only be used if .env exists

try:
    settings = Settings()
except ValidationError as e:
    print("\n[ERROR] Missing required environment variables:", file=sys.stderr)
    print(str(e), file=sys.stderr)
    sys.exit(1)
