import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = '123abc'
    SQLALCHEMY_DATABASE_URI = ""