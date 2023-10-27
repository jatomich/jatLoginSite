from dotenv import load_dotenv
load_dotenv()

from app import create_app, db
from app.models import User, Movie, TVShow

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Movie': Movie, 'TV Show': TVShow}