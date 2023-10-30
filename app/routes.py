from flask import (render_template,
                   redirect,
                   request,
                   jsonify,
                   url_for,
                   current_app as app)
from app import db
from .models import User
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
    netflix_df = pd.read_csv('app/static/netflix_titles.csv')
    print(netflix_df)
    netflix_df.to_json('app/static/netflix.json')
    with open('app/static/netflix.json', 'r') as feed_json:
        json_data = json.load(feed_json)
    return json_data