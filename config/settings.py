import os

class Settings:
    API_ID = 20173022
    API_HASH = "bab4a3351ed7634a8c1a3f8767fcf75c"
    PHONE_NUMBER = "+251913423473"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../database/medical_data.db")

settings = Settings()
