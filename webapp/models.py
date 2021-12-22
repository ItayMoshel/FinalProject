from webapp import db
from flask_login import UserMixin


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    genre = db.Column(db.String())
    year = db.Column(db.String())
    length_in_min = db.Column(db.String())
    imdb_rate = db.Column(db.String())
    meta_score = db.Column(db.String())
    description = db.Column(db.String())
    director = db.Column(db.String())
    photo_link = db.Column(db.String())


class Upcoming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    genre = db.Column(db.String())
    length_in_min = db.Column(db.String())
    description = db.Column(db.String())
    director = db.Column(db.String())
    photo_link = db.Column(db.String())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
