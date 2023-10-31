from flask import (render_template,
                   redirect,
                   request,
                   jsonify,
                   url_for,
                   current_app as app)
from app import db, api
from .models import User, Movie, TVShow
import pandas as pd
import json
from flask_restful import Resource


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/netflixdf")
def netflixdf():
    netflix_df = pd.read_csv(url_for('static', filename='input/csv/netflix_titles.csv'))
    print(netflix_df)
    for tup in netflix_df.itertuples():
        if tup.type == "Movie" and tup.show_id not in [movie.show_id for movie in Movie.query]:
            db.session.add(Movie(show_id=tup.show_id, title=tup.title, director=tup.director, cast=tup.cast, country=tup.country, date_added=tup.date_added, release_year=tup.release_year, rating=tup.rating, duration=tup.duration, listed_in=tup.listed_in, description=tup.description))
            db.session.commit()
            continue
        if tup.type == "TV Show" and tup.show_id not in [tvshow.show_id for tvshow in TVShow.query]:
            db.session.add(TVShow(show_id=tup.show_id, title=tup.title, director=tup.director, cast=tup.cast, country=tup.country, date_added=tup.date_added, release_year=tup.release_year, rating=tup.rating, duration=tup.duration, listed_in=tup.listed_in, description=tup.description))
            db.session.commit()
    # netflix_df.to_json('app/static/netflix.json')
    # with open("{{ url_for('static', filename=)}}", 'r') as feed_json:
    #     json_data = json.load(feed_json)
    # return json_data
    return redirect("index")


# @app.route("/netflix_movies")
# def netflix_movies():
#     columns = ['TITLE', 'DIRECTOR', 'CAST', 'DESCRIPTION']
#     movies = [[m.title, m.director, m.cast, m.description] for m in Movie.query]

#     return render_template("netflix_movies.html", columns=columns, movies=movies)


# @app.route("/netflix_shows")
# def netflix_shows():
#     columns = ['TITLE', 'DIRECTOR', 'CAST', 'DESCRIPTION']
#     shows = [[s.title, s.director, s.cast, s.description] for s in TVShow.query]

#     return render_template("netflix_shows.html", columns=columns, shows=shows)


# @app.route("/netflix_movies")
class NetflixMovies(Resource):
    def get(self):
        self.columns = ['TITLE', 'DIRECTOR', 'CAST', 'DESCRIPTION']
        self.movies = [{c: m.c for c in self.columns} for m in Movie.query]
        # return {'movies': self.movies}
        return self.response
    
    @classmethod
    def make_api(cls, response):
        cls.response = response
        return cls
    

# @app.route("/netflix_shows")
class NetflixShows(Resource):
    def get(self):
        self.columns = ['TITLE', 'DIRECTOR', 'CAST', 'DESCRIPTION']
        self.shows = [{c: s.c for c in self.columns} for s in TVShow.query]
        # return {'shows': self.shows}
        return self.response
    
    @classmethod
    def make_api(cls, response):
        cls.response = response
        return cls