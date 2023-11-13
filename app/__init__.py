from flask import Flask
from config import Config, instance_path
from flask_bootstrap import Bootstrap
from flask_restful import Api
from app.main import bp as MainBP
from .main import db, User, Movie, TVShow, NetflixMedia

api = Api()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__,
                instance_path=instance_path,
                instance_relative_config=True,
                static_url_path=str(instance_path) + '/static',
                static_folder='./static',
                template_folder='./templates')
                
    app.config.from_object(config_class)
    app.config.from_envvar('CUSTOM_CONFIG')

    app.register_blueprint(MainBP)
    api.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        db.create_all()
       
    return app

