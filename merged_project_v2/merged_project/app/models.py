from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ── User ──────────────────────────────────────────────────────
class User(UserMixin, db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    username   = db.Column(db.String(80), unique=True, nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    trips     = db.relationship('Trip', backref='user', lazy=True)
    wishlists = db.relationship('Wishlist', backref='user', lazy=True)
    reviews   = db.relationship('Review', backref='user', lazy=True)


# ── Trip ──────────────────────────────────────────────────────
class Trip(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name        = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    start_date  = db.Column(db.Date)
    end_date    = db.Column(db.Date)
    budget      = db.Column(db.Float, default=0)
    is_public   = db.Column(db.Boolean, default=False)
    accommodation = db.Column(db.String(500))
    highlights    = db.Column(db.Text)
    tips          = db.Column(db.Text)
    duration_days = db.Column(db.Integer)
    image_filename = db.Column(db.String(200))
    places  = db.relationship('Place', backref='trip', lazy=True, cascade='all, delete-orphan')
    reviews = db.relationship('Review', backref='trip', lazy=True, cascade='all, delete-orphan')


# ── Place ─────────────────────────────────────────────────────
class Place(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    trip_id  = db.Column(db.Integer, db.ForeignKey('trip.id'), nullable=False)
    name     = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    notes    = db.Column(db.Text)
    est_cost = db.Column(db.Float, default=0)
    day_number    = db.Column(db.Integer)
    opening_hours = db.Column(db.String(100))
    recommended   = db.Column(db.Boolean, default=True)

# ── Wishlist ──────────────────────────────────────────────────
class Wishlist(db.Model):
    id               = db.Column(db.Integer, primary_key=True)
    user_id          = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    destination      = db.Column(db.String(100), nullable=False)
    title            = db.Column(db.String(200), nullable=False)
    description      = db.Column(db.Text)
    estimated_budget = db.Column(db.Float, default=0)
    duration_days    = db.Column(db.Integer, default=0)
    is_public        = db.Column(db.Boolean, default=True)
    created_at       = db.Column(db.DateTime, default=datetime.utcnow)


# ── Review ────────────────────────────────────────────────────
class Review(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    trip_id    = db.Column(db.Integer, db.ForeignKey('trip.id'), nullable=False)
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating     = db.Column(db.Integer, nullable=False)   # 1–5
    comment    = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
