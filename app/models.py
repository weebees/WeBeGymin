from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """Model to represent a user for authentication."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Sleep(db.Model):
    """Model to track user sleep data."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref=db.backref('sleep_records', lazy=True))


class Food(db.Model):
    """Model to track user food data."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    meal = db.Column(db.String(200), nullable=False)
    calories = db.Column(db.Integer)
    user = db.relationship('User', backref=db.backref('food_records', lazy=True))


class Workout(db.Model):
    """Model to track user workout data."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Float, nullable=False)  # Duration in hours
    user = db.relationship('User', backref=db.backref('workout_records', lazy=True))
