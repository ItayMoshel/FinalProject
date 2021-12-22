from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
import numpy

from webapp.models import User, Movies, Upcoming

scrape_print = Blueprint('scrape', __name__)


@scrape_print.route('/top_100')
def top_100():
    title = Movies.title
    top_movies = Movies.query.filter_by(title=title)
    return render_template('Top100.html', user=current_user, top_movies=top_movies)


@scrape_print.route('/upcoming_movies')
def upcoming_movies():
    title = Upcoming.title
    upcoming = Upcoming.query.filter_by(title=title)
    return render_template('Upcoming.html', user=current_user, upcoming=upcoming)
