from flask import Flask
from config import Config, basedir
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_cors import CORS
# from flask_restful import Api

db = SQLAlchemy()
# api = Api()
bootstrap = Bootstrap()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__,
                instance_path=basedir + "/app",
                instance_relative_config=True,
                static_url_path=basedir + "/app/static",
                static_folder="/static")
                
    app.config.from_object(config_class)
    app.config.from_envvar('CUSTOM_CONFIG')

    db.init_app(app)
    # api.init_app(app)
    bootstrap.init_app(app)
    cors.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()
        # url_map = app.url_map
        # try:
        #     for rule in url_map.iter_rules('static'):
        #         url_map._rules.remove(rule)
        # except ValueError:
        #     # no static view yet created
        #     pass

        # # register new; the same function is used
        # app.add_url_rule(
        #     app.static_url_path + '/<path:filename>',
        #     endpoint='static', view_func=app.send_static_file
        # )
        # movies = routes.NetflixMovies()
        # shows = routes.NetflixShows()
        # movies_api = movies.make_api({"key": "value"})
        # shows_api = shows.make_api({"key": "value"})
        # api.add_resource(movies_api, '/netflix_movies')
        # api.add_resource(shows_api, '/netflix_shows')

    return app

