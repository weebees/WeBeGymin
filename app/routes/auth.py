from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User  # assuming a User model is created in models.py
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('main', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Route to handle user registration."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('auth.register'))

        # Hash password and add user to the database
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Route to handle user login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database for the user
        user = User.query.filter_by(username=username).first()

        # Verify password and log the user in
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login failed! Check your username and password.')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """Route to log the user out."""
    logout_user()
    return redirect(url_for('auth.login'))