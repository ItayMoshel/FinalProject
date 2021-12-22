from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from webapp.models import Movies, User, Upcoming
import random

main_print = Blueprint('home', __name__)


@main_print.route('/')
@main_print.route('/home')
def home():
    title = Movies.title
    top_movies = Movies.query.filter_by(title=title)
    title2 = Upcoming.title
    upcoming = Upcoming.query.filter_by(title=title2)
    genre = Movies.genre
    top_by_genre = Movies.query.filter_by(genre=genre)
    top_by_action = []
    top_by_comedy = []
    top_by_thriller = []
    top_by_drama = []
    top_by_crime = []
    genre_list = []
    for item in top_by_genre:
        if "Thriller" in item.genre.split(", "):
            top_by_thriller.append(item.photo_link)
        if "Drama" in item.genre.split(", "):
            top_by_drama.append(item.photo_link)
        if "Comedy" in item.genre.split(", "):
            top_by_comedy.append(item.photo_link)
        if "Action" in item.genre.split(", "):
            top_by_action.append(item.photo_link)
        if "Crime" in item.genre.split(", "):
            top_by_crime.append(item.photo_link)

    return render_template('home.html', user=current_user, crime=top_by_crime, drama=top_by_drama, action=top_by_action,
                           thriller=top_by_thriller, random=random, top_movies=top_movies, upcoming=upcoming)


@main_print.route('/search', methods=['POST', 'GET'])
def search():
    inp_src = request.form['search'].split()
    list_inp_src = []
    for item in inp_src:
        list_inp_src.append(item.capitalize())
    new_inp_src = " ".join(list_inp_src)
    top_title = Movies.title
    up_title = Upcoming.title
    top_movies = Movies.query.filter_by(title=top_title)
    upcoming = Upcoming.query.filter_by(title=up_title)
    t_dir = Movies.director
    u_dir = Upcoming.director
    top_dir = Movies.query.filter_by(director=t_dir)
    up_dir = Upcoming.query.filter_by(director=u_dir)
    t_genre = Movies.genre
    u_genre = Upcoming.genre
    top_genre = Movies.query.filter_by(genre=t_genre)
    up_genre = Upcoming.query.filter_by(genre=u_genre)

    return render_template('search.html', user=current_user, top=top_movies, up=upcoming, top_dir=top_dir,
                           up_dir=up_dir, top_genre=top_genre, up_genre=up_genre, user_input=new_inp_src)
