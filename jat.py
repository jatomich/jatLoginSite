from dotenv import load_dotenv
load_dotenv()

from config import Config, basedir
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pandas as pd
from flask_restful import Api, Resource

###########################
# INSTANTIATE APPLICATION #
###########################
app = Flask(__name__,
            instance_path=basedir,
            instance_relative_config=True,
            static_url_path=str(basedir) + '/static',
            static_folder='./static',
            template_folder='./templates'
            )
app.config.from_object(Config)
app.config.from_envvar('CUSTOM_CONFIG')

######################
# CONFIGURE DATABASE #
######################
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def add_new_user(username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

    def __repr__(self):
        return f"<User {self.username}>"


class NetflixMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String(24), index=True, unique=True)
    format = db.Column(db.String(16))
    title = db.Column(db.String(120))
    director = db.Column(db.String(120))
    cast = db.Column(db.String(256))
    country = db.Column(db.String(64))
    date_added = db.Column(db.String(16))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.String(8))
    duration = db.Column(db.Integer)
    listed_in = db.Column(db.String(256))
    description = db.Column(db.String(512))

    def __repr__(self):
        return f"<Netflix Media: {self.title}; {self.format}>"
    
with app.app_context():
    db.create_all()

################################# 
# CROSS-ORIGIN RESOURCE SHARING #
#################################
CORS(app)

########################### 
# INSTANTIATE RESTFUL API #
###########################
class NetflixShows(Resource):
    def get(self):
        # columns = ["title", "director", "cast", "description", "show_id"]
        shows = [{k: v for k, v in list(s.__dict__.items())[1:]} for s in NetflixMedia.query if s.format.lower() == 'tv show']
        return shows

api = Api(app)
#####################################
# BOOTSTRAP FOR FRONTEND FORMATTING #
#####################################
Bootstrap(app)

##################
# VIEW FUNCTIONS #
##################
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/netflixdf')
def netflixdf():
    netflix_raw_df = pd.read_csv(url_for('static', filename='input/csv/netflix_titles.csv')).rename(columns={'type': 'format'})

    netflix_df = netflix_raw_df.dropna().sort_values(
        ['format', 'title']
        ).reset_index(drop=True).copy()

    # print(netflix_df.iloc[:10, 0:3])

    for row in netflix_df.iterrows():
        new_item = NetflixMedia(**row[1])
        db.session.add(new_item)
        db.session.commit()

    return redirect(url_for('index'))

class NetflixMovies(Resource):
# @app.route("/netflix_movies")
# def netflix_movies():
#     columns = ["title", "director", "cast", "description", "show_id"]
#     movies = [{k: v for k, v in m.__dict__.items() if k in columns} for m in Movie.query]
#     return {'movies': movies}

    def get(self):
        # columns = ["title", "director", "cast", "description", "show_id"]
        movies = [{k: v for k, v in list(s.__dict__.items())[1:]} for s in NetflixMedia.query if s.format.lower() == 'movie']
        return movies
    
api.add_resource(NetflixMovies, '/api/netflix_movies')

    # @classmethod
    # def make_api(cls, response):
    #     cls.response = response
    #     return cls

# @app.route("/netflix_shows")
# def netflix_shows():
#     columns = ["title", "director", "cast", "description", "show_id"]
#     shows = [{k: v for k, v in s.__dict__.items() if k in columns} for s in TVShow.query]
#     return {'shows': shows}
###########################
# INSTANTIATE APPLICATION #
###########################
app = Flask(__name__,
            instance_path=basedir,
            instance_relative_config=True,
            static_url_path=str(basedir) + '/static',
            static_folder='./static',
            template_folder='./templates'
            )
app.config.from_object(Config)
app.config.from_envvar('CUSTOM_CONFIG')

################################# 
# CROSS-ORIGIN RESOURCE SHARING #
#################################
CORS(app)

#####################################
# BOOTSTRAP FOR FRONTEND FORMATTING #
#####################################
Bootstrap(app)

######################
# CONFIGURE DATABASE #
######################
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def add_new_user(username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

    def __repr__(self):
        return f"<User {self.username}>"


class NetflixMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String(24), index=True, unique=True)
    format = db.Column(db.String(16))
    title = db.Column(db.String(120))
    director = db.Column(db.String(120))
    cast = db.Column(db.String(256))
    country = db.Column(db.String(64))
    date_added = db.Column(db.String(16))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.String(8))
    duration = db.Column(db.Integer)
    listed_in = db.Column(db.String(256))
    description = db.Column(db.String(512))

    def __repr__(self):
        return f"<Netflix Media: {self.title}; {self.format}>"
    
with app.app_context():
    db.create_all()

########################### 
# INSTANTIATE RESTFUL API #
###########################
class NetflixMovies(Resource):

    def get(self):
        # columns = ["title", "director", "cast", "description", "show_id"]
        movies = [{k: v for k, v in list(s.__dict__.items())[1:]} for s in NetflixMedia.query if s.format.lower() == 'movie']
        return jsonify(kwargs=movies)
    
class NetflixShows(Resource):
    
    def get(self):
        # columns = ["title", "director", "cast", "description", "show_id"]
        shows = [{k: v for k, v in list(s.__dict__.items())[1:]} for s in NetflixMedia.query if s.format.lower() == 'tv show']
        return jsonify(kwargs=shows)

api = Api(app)

api.add_resource(NetflixMovies, '/api/netflix_movies')
api.add_resource(NetflixShows, '/api/netflix_shows')


##################
# VIEW FUNCTIONS #
##################
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/netflixdf')
def netflixdf():
    netflix_raw_df = pd.read_csv(url_for('static', filename='input/csv/netflix_titles.csv')).rename(columns={'type': 'format'})

    netflix_df = netflix_raw_df.dropna().sort_values(
        ['format', 'title']
        ).reset_index(drop=True).copy()

    # print(netflix_df.iloc[:10, 0:3])

    for row in netflix_df.iterrows():
        new_item = NetflixMedia(**row[1])
        print(new_item)
        db.session.add(new_item)
        db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




# @app.route("/netflix_movies")
# def netflix_movies():
#     columns = ["title", "director", "cast", "description", "show_id"]
#     movies = [{k: v for k, v in m.__dict__.items() if k in columns} for m in Movie.query]
#     return {'movies': movies}

    # @classmethod
    # def make_api(cls, response):
    #     cls.response = response
    #     return cls





# instance = axios.create({
#     baseURL: 'http://localhost:5000',
#     timeout: 1000,
#     headers: {'X-Custom-Header': 'foobar'}
# });