from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Trip, Place
from datetime import datetime
from flask import abort
import os
from werkzeug.utils import secure_filename

trip_bp = Blueprint('trip', __name__)


@trip_bp.route('/home')
def home():
    public_trips = Trip.query.filter_by(is_public=True).order_by(Trip.id.desc()).all()
    return render_template('home.html', trips=public_trips)


@trip_bp.route('/trips')
@login_required
def trips():
    user_trips = Trip.query.filter_by(user_id=current_user.id).order_by(Trip.id.desc()).all()
    return render_template('trips.html', trips=user_trips)


@trip_bp.route('/trips/new', methods=['GET', 'POST'])
@login_required
def new_trip():
    if request.method == 'POST':
        image = request.files.get('image')
        image_filename = None
        if image and image.filename:
            image_filename = secure_filename(image.filename)
            image.save(os.path.join('app', 'static', 'uploads', image_filename))

        name        = request.form.get('name')
        destination = request.form.get('destination')
        start_date  = request.form.get('start_date')
        end_date    = request.form.get('end_date')
        budget      = request.form.get('budget')
        is_public   = True if request.form.get('is_public') == 'on' else False

        if not name or not destination:
            flash('Trip name and destination are required.', 'error')
            return redirect(url_for('trip.new_trip'))
        trip = Trip(
            name        = name,
            destination = destination,
            start_date  = datetime.strptime(start_date, '%Y-%m-%d').date() if start_date else None,
            end_date    = datetime.strptime(end_date, '%Y-%m-%d').date() if end_date else None,
            budget      = float(budget) if budget else 0,
            is_public   = is_public,
            user_id     = current_user.id,
            accommodation = request.form.get('accommodation'),
            highlights    = request.form.get('highlights'),
            tips          = request.form.get('tips'),
            duration_days = int(request.form.get('duration_days')) if request.form.get('duration_days') else None
        )

        db.session.add(trip)
        db.session.commit()
        flash('Trip created successfully.', 'success')
        return redirect(url_for('trip.trips'))

    return render_template('new_trip.html')


@trip_bp.route('/trips/<int:id>')
@login_required
def trip_detail(id):
    trip = Trip.query.get_or_404(id)
    if not trip.is_public and trip.user_id != current_user.id:
        abort(403)
    places = Place.query.filter_by(trip_id=trip.id).all()
    return render_template('trip_detail.html', trip=trip, places=places)


@trip_bp.route('/trips/<int:id>/delete', methods=['POST'])
@login_required
def delete_trip(id):
    trip = Trip.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(trip)
    db.session.commit()
    flash('Trip deleted successfully.', 'success')
    return redirect(url_for('trip.trips'))


@trip_bp.route('/search')
def search():
    query = request.args.get('q', '').strip()

    if not query:
        return render_template('search_results.html', results=[], query=None)

    results = Trip.query.filter(
        Trip.is_public == True,
        Trip.destination.ilike(f"%{query}%")
    ).order_by(Trip.id.desc()).all()

    return render_template('search_results.html', results=results, query=query)