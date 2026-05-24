from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from app import db
from app.models import Place, Trip, Review

place_bp = Blueprint('place', __name__)


@place_bp.route('/trips/<int:trip_id>/places', methods=['POST'])
@login_required
def add_place(trip_id):
    trip = Trip.query.get_or_404(trip_id)

    if trip.user_id != current_user.id:
        abort(403)

    name     = request.form.get('name')
    category = request.form.get('category')
    notes    = request.form.get('notes')
    est_cost = float(request.form.get('est_cost') or 0)

    place = Place(trip_id=trip_id, name=name, category=category, notes=notes, est_cost=est_cost)
    db.session.add(place)
    db.session.commit()

    flash(f'"{name}" added to your trip!', 'success')
    return redirect(url_for('trip.trip_detail', id=trip_id))


@place_bp.route('/places/<int:place_id>/delete', methods=['POST'])
@login_required
def delete_place(place_id):
    place = Place.query.get_or_404(place_id)
    trip  = Trip.query.get(place.trip_id)

    if trip.user_id != current_user.id:
        abort(403)

    trip_id = place.trip_id
    db.session.delete(place)
    db.session.commit()

    flash('Place removed.', 'info')
    return redirect(url_for('trip.trip_detail', id=trip_id))


@place_bp.route('/search')
def search_trips():
    query   = request.args.get('q', '')
    results = []

    if query:
        results = Trip.query.filter(
            Trip.is_public == True,
            Trip.destination.ilike(f'%{query}%')
        ).all()

    return render_template('search_results.html', results=results, query=query)


@place_bp.route('/filter')
def filter_trips():
    max_budget = request.args.get('max_budget', type=float)
    min_budget = request.args.get('min_budget', type=float)

    trips = Trip.query.filter(Trip.is_public == True)

    if max_budget is not None:
        trips = trips.filter(Trip.budget <= max_budget)
    if min_budget is not None:
        trips = trips.filter(Trip.budget >= min_budget)

    trips = trips.order_by(Trip.budget.asc()).all()

    return render_template('filter_results.html', trips=trips,
                           max_budget=max_budget, min_budget=min_budget)


@place_bp.route('/trips/<int:trip_id>/review', methods=['POST'])
@login_required
def add_review(trip_id):
    trip = Trip.query.get_or_404(trip_id)

    rating  = int(request.form.get('rating'))
    comment = request.form.get('comment')

    existing = Review.query.filter_by(trip_id=trip_id, user_id=current_user.id).first()
    if existing:
        flash('You already reviewed this trip.', 'error')
        return redirect(url_for('trip.trip_detail', id=trip_id))

    review = Review(trip_id=trip_id, user_id=current_user.id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()

    flash('Review added!', 'success')
    return redirect(url_for('trip.trip_detail', id=trip_id))


@place_bp.route('/reviews/<int:review_id>/delete', methods=['POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)

    if review.user_id != current_user.id:
        abort(403)

    trip_id = review.trip_id
    db.session.delete(review)
    db.session.commit()

    flash('Review deleted.', 'info')
    return redirect(url_for('trip.trip_detail', id=trip_id))
