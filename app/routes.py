from flask import (render_template,
                   request,
                   jsonify,
                   current_app as app)
from app import db
from .models import User


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