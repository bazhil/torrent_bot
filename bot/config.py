import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings:
    BOT_TOKEN = os.getenv("TG_TOKEN")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    CATEGORIES_FILE = BASE_DIR / "categories_dict.json"

settings = Settings()