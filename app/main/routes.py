from flask import (render_template,
                   redirect,
                   url_for,
                   current_app as app)
from app.main import main_bp
import pandas as pd
from flask_restful import Resource

@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('index.html')


@main_bp.route('/api/netflixdf')
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
    return redirect(url_for('main.index'))

class NetflixMovies(Resource):
# @app.route("/netflix_movies")
# def netflix_movies():
#     columns = ["title", "director", "cast", "description", "show_id"]
#     movies = [{k: v for k, v in m.__dict__.items() if k in columns} for m in Movie.query]
#     return {'movies': movies}

    def get(self):
        columns = ["title", "director", "cast", "description", "show_id"]
        movies = [{k: v for k, v in m.__dict__.items() if m in columns} for m in main_bp.db.Movie.query]
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
        shows = [{k: v for k, v in s.__dict__.items() if k in columns} for s in main_bp.db.TVShow.query]
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