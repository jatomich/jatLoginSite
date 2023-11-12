from flask_sqlalchemy import SQLAlchemy

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
                new_content = Movie(**details)
            elif target_table_format == "tv show":
                new_content = TVShow(**details)
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
