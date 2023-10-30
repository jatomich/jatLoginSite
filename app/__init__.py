from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_cors import CORS

db = SQLAlchemy()
bootstrap = Bootstrap()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__,
                instance_path='/jatLoginSite/app',
                instance_relative_config=True,
                static_url_path='/jatLoginSite/app/static',
                static_folder='static',
                template_folder='templates')
    app.config.from_object(config_class)
    app.config.from_envvar('CUSTOM_CONFIG')

    db.init_app(app)
    bootstrap.init_app(app)
    cors.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app