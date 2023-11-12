from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.models import (db,
                        User,
                        Movie,
                        TVShow,
                        NetflixMedia)


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Movie': Movie,
            'TVShow': TVShow,
            'User': User,
            'NetflixMedia': NetflixMedia}