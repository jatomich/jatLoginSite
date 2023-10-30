from flask import render_template, current_app as app
from app import db


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")