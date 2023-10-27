from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

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
