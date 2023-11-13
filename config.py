import os

basedir = os.path.abspath(os.path.dirname(os.environ.get('LOC_ANCHOR', '__file__')))


class Config():
    SECRET_KEY = '123abc'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/" + "app.db"

    # static_url_path=str(instance_path) + '/static',
    #             static_folder='./static',
    #             template_folder='./templates'