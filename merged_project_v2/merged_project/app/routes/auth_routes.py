from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User,Trip, Review

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('trip.home'))
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email    = request.form.get('email').strip()
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('auth.register'))

        hashed = generate_password_hash(password)
        db.session.add(User(username=username, email=email, password=hashed))
        db.session.commit()
        flash('Account created! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email    = request.form.get('email').strip()
        password = request.form.get('password')
        user     = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Wrong email or password.', 'error')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('trip.home'))

    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile')
@login_required
def profile():
    user_trips = Trip.query.filter_by(user_id=current_user.id).order_by(Trip.id.desc()).all()
    user_reviews = Review.query.filter_by(user_id=current_user.id).order_by(Review.id.desc()).all()
    return render_template('profile.html', trips=user_trips, reviews=user_reviews)


@auth_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email    = request.form.get('email').strip()

        if User.query.filter(User.username == username, User.id != current_user.id).first():
            flash('Username already taken.', 'error')
            return redirect(url_for('auth.edit_profile'))

        if User.query.filter(User.email == email, User.id != current_user.id).first():
            flash('Email already in use.', 'error')
            return redirect(url_for('auth.edit_profile'))

        current_user.username = username
        current_user.email    = email
        db.session.commit()
        flash('Profile updated.', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('edit_profile.html')