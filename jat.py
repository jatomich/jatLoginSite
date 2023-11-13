from dotenv import load_dotenv
load_dotenv()

from config import Config, basedir
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pandas as pd
from flask_restful import Resource

######################
# CONFIGURE DATABASE #
######################
db = SQLAlchemy()


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

        
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String(24), index=True, unique=True)
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

    def add_new_movie():
        pass

    def __repr__(self):
        return f"<Movie: {self.title}>"
    

class TVShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String(24), index=True, unique=True)
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
        return f"<TV Show: {self.title}>"
    

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

    def add_content(format: str, details: dict=None):
        try:
            target_table_format = format.lower()
            if target_table_format == "movie":
                new_content = NetflixMedia(**details)
            elif target_table_format == "tv show":
                new_content = NetflixMedia(**details)
        except ValueError as error:
            print(error)
            return
        finally:
            try:
                db.session.add(new_content)
                db.session.commit()
            except Exception as error:
                print(error)
                return

    def __repr__(self):
        return f"<Netflix Media: {self.title}; {self.format}>"
    
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

CORS(app)
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
    netflix_df = pd.read_csv(url_for('static', filename='input/csv/netflix_titles.csv'))
    print(netflix_df)

    for tup in netflix_df.itertuples():
        pass

    # movies_df = netflix_df.loc[netflix_df['type'] == 'Movie', :].sort_values('title').reset_index(drop=True).copy()
    # shows_df = netflix_df.loc[netflix_df['type'] == 'TV Show', :].sort_values('title').reset_index(drop=True).copy()
    # for tup in movies_df.itertuples():
    #     if tup.show_id not in [movie.show_id for movie in Movie.query]:
    #         db.session.add(Movie(show_id=tup.show_id, title=tup.title, director=tup.director, cast=tup.cast, country=tup.country, date_added=tup.date_added, release_year=tup.release_year, rating=tup.rating, duration=tup.duration, listed_in=tup.listed_in, description=tup.description))
    #         db.session.commit()
    # for tup in shows_df.itertuples():
    #     if tup.show_id not in [tvshow.show_id for tvshow in TVShow.query]:
    #         db.session.add(TVShow(show_id=tup.show_id, title=tup.title, director=tup.director, cast=tup.cast, country=tup.country, date_added=tup.date_added, release_year=tup.release_year, rating=tup.rating, duration=tup.duration, listed_in=tup.listed_in, description=tup.description))
    #         db.session.commit()
    # netflix_df.to_json('app/static/netflix.json')
    # with open("{{ url_for('static', filename=)}}", 'r') as feed_json:
    #     json_data = json.load(feed_json)
    # return json_data
    return redirect(url_for('index'))

class NetflixMovies(Resource):
# @app.route("/netflix_movies")
# def netflix_movies():
#     columns = ["title", "director", "cast", "description", "show_id"]
#     movies = [{k: v for k, v in m.__dict__.items() if k in columns} for m in Movie.query]
#     return {'movies': movies}

    def get(self):
        columns = ["title", "director", "cast", "description", "show_id"]
        movies = [{k: v for k, v in m.__dict__.items() if m in columns} for m in Movie.query]
        return movies

    # @classmethod
    # def make_api(cls, response):
    #     cls.response = response
    #     return cls

class NetflixShows(Resource):
# @app.route("/netflix_shows")
# def netflix_shows():
#     columns = ["title", "director", "cast", "description", "show_id"]
#     shows = [{k: v for k, v in s.__dict__.items() if k in columns} for s in TVShow.query]
#     return {'shows': shows}

    def get(self):
        columns = ["title", "director", "cast", "description", "show_id"]
        shows = [{k: v for k, v in s.__dict__.items() if k in columns} for s in TVShow.query]
        return shows

    # @classmethod
    # def make_api(cls, response):
    #     cls.response = response
    #     return cls



# @app.route("/imdb/<endpoint>'", methods=["GET", "POST"])
# def imdb_data(endpoint):
#     imdb_df = pd.read_csv('static/output/imdb.csv',
#                           low_memory=False)
#     print(imdb_df)


if __name__ == '__main__':
    app.run(debug=True)