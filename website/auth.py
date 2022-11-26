import email
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from crypt import methods
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from website import db
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user is not None and current_user.is_authenticated:  # type: ignore
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user is not None:
            if not check_password_hash(user.password, password):  # type: ignore
                flash("Password incorrect", "error")
                return redirect(url_for('auth.login'))
            login_user(user)
            flash("Login successful","success")
        return redirect(url_for('views.home'))

    return render_template("login.html")


@ auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@ auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user is not None and current_user.is_authenticated:  # type: ignore
        return redirect(url_for('views.home'))
    if request.method == 'POST':

        first_name = request.form.get('firstName')
        email = request.form.get('email')

        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # user = User.query.filter(email=email).first()
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")

        if len(email) < 4:      # type: ignore
            flash("Email is greater than 3 characters.", category="error")

        elif len(first_name) < 2:      # type: ignore
            flash("First Name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:  # type: ignore
            flash("Password must be atleast 7 characters", category="error")
        else:

            new_user = User(email=email,
                            first_name=first_name,
                            password=generate_password_hash(
                                password1, method='sha256'))  # type: ignore
            db.session.add(new_user)
            db.session.commit()

            flash("Account created!", category="success")
            return redirect(url_for('views.home'))
    return render_template("sign-up.html")
