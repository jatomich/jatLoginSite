from flask import (render_template,
                   redirect,
                   request,
                   jsonify,
                   url_for,
                   current_app as app)
from app import db
from .models import User, Movie, TVShow
import pandas as pd
import json


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/hello", methods=['POST'])
def hello():
    # This gets the JSON data from the React request
    data = request.get_json()
    # This gets the name from the data
    username = data.get('name')
    email = data.get('email')
    # Check db.  If user does not already exist, add user to db
    if username not in [user.username for user in User.query]:
        db.session.add(User(username=username, email=email))
        db.session.commit()
    # This returns a JSON response with a greeting message
    return jsonify({'message': f'Hello, {username}!'})


@app.route("/netflixdf")
def netflixdf():
    netflix_df = pd.read_csv("{{ url_for('static', filename='netflix_titles.csv') }}")
    print(netflix_df)
    # if not Movie.query or not TVShow.query:
    #     for tup in netflix_df.itertuples():
    #         if tup.type == "Movie" and tup.show_id not in [movie.show_id for movie in Movie.query]:
    #             db.session.add(Movie(show_id=tup.show_id, title=tup.title, director=tup.director, cast=tup.cast, country=tup.country, date_added=tup.date_added, release_year=tup.release_year, rating=tup.rating, duration=tup.duration, listed_in=tup.listed_in, description=tup.description))
    #             db.session.commit()
    #             continue
    #         if tup.type == "TV Show" and tup.show_id not in [tvshow.show_id for tvshow in TVShow.query]:
    #             db.session.add(TVShow(show_id=tup.show_id, title=tup.title, director=tup.director, cast=tup.cast, country=tup.country, date_added=tup.date_added, release_year=tup.release_year, rating=tup.rating, duration=tup.duration, listed_in=tup.listed_in, description=tup.description))
    #             db.session.commit()

    movies = [[m.title, m.director, m.cast, m.description] for m in Movie.query]

    shows = [[s.title, s.director, s.cast, s.description] for s in TVShow.query]

    columns = ['TITLE', 'DIRECTOR', 'CAST', 'DESCRIPTION']

    netflix_df.to_json('app/static/netflix.json')
    with open("{{ url_for('static', filename=)}}", 'r') as feed_json:
        json_data = json.load(feed_json)
    # return json_data
    return render_template("netflix.html", movies=movies, shows=shows, columns=columns)