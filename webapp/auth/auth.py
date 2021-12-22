from flask import Blueprint, render_template, request, flash, redirect, url_for
from webapp.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from webapp import db
from flask_login import login_user, login_required, logout_user, current_user

auth_blueprint = Blueprint('auth', __name__)


# @auth_blueprint.route('/')
# @login_required
# def home():
#     return render_template('home.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_blueprint.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be longer then 4 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be longer then 1 characters', category='error')
        elif len(last_name) < 3:
            flash('Last name must be longer then 2 characters', category='error')
        elif password1 != password2:
            flash("Password don't match", category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('home.home'))

    return render_template("sign_up.html", user=current_user)


@auth_blueprint.route("/personal-area")
def personal():
    return render_template("personal-area.html", user=current_user)
