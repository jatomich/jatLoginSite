from flask import (render_template,
                   request,
                   jsonify,
                   current_app as app)
from app import db


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/hello", methods=['POST'])
def hello():
    # This gets the JSON data from the React request
    data = request.get_json()
    # This gets the name from the data
    name = data.get('name')
    # This returns a JSON response with a greeting message
    return jsonify({'message': f'Hello, {name}!'})