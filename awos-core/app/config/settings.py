from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME", "AWOS")

    APP_VERSION = os.getenv("APP_VERSION", "Genesis v1.0")

    DEBUG = os.getenv("DEBUG", "False") == "True"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


settings = Settings()