import os
from config import basedir

SECRET_KEY = os.environ.get("SECRET_KEY", "miss")
SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir}/" + "app.db"