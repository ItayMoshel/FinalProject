from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from webapp.models import Movies, User, Upcoming
from webapp import db
import random

personal_print = Blueprint('personal', __name__)


@personal_print.route('lists', methods=['GET', 'POST'])
def mvlst():
    if request.method == 'POST':
        inp_title = request.form.get('title')
        usr_list = []

        movie = Movies.query.filter_by(title=inp_title).first()
        if movie:
            flash('Title Added!', category='success')
            usr_list.append(movie.title)
        elif len(inp_title) < 2:
            flash('Title must be longer then 2 characters', category='error')
        print(movie.title)
    return render_template("movieslists.html", user=current_user)
