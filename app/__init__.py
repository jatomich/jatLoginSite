from flask import Flask
from config import Config, instance_path
from flask_bootstrap import Bootstrap
from flask_restful import Api
# from .models import NetflixMovies, NetflixShows
from main import models, routes

# db = SQLAlchemy()
api = Api()
bootstrap = Bootstrap()

movie_list = (movies := models.Movie.query) if models.Movie.query else []
show_list = (shows := models.Show.query) if models.Show.query else []


def create_app(config_class=Config):
    app = Flask(__name__,
                instance_path=instance_path,
                instance_relative_config=True)
                
    app.config.from_object(config_class)
    app.config.from_envvar('CUSTOM_CONFIG')

    db.init_app(app)
    api.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        db.create_all()
       
    return app