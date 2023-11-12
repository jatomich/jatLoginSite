import os

SECRET_KEY = os.environ.get("SECRET_KEY", "miss")
CORS_ALLOW_HEADERS = os.environ.get("CORS_ALLOW_HEADERS", "Content-Type")
CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "http://127.0.0.1:5000")

