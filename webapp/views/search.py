from flask import Blueprint, render_template, request, redirect, url_for
from webapp.models import User, Movies, Upcoming

search_print = Blueprint('search', __name__)


# @search_print.route('/search', methods=['POST'])
# def search():
#     q = request.form['q']
#     print(q)
#     return redirect(url_for('home.home'))



