import os

SECRET_KEY = os.environ.get("SECRET_KEY", "miss")
CORS_ALLOW_HEADERS = "*"
CORS_ORIGINS = "*"