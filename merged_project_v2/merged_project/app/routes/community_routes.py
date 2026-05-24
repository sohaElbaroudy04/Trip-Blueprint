from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Wishlist
from datetime import datetime

community_bp = Blueprint('community', __name__)


@community_bp.route('/community')
def community():
    wishlists = Wishlist.query.filter_by(is_public=True).order_by(Wishlist.id.desc()).all()
    return render_template('community.html', wishlists=wishlists)


@community_bp.route('/community/new', methods=['GET', 'POST'])
@login_required
def new_wishlist():
    if request.method == 'POST':
        destination      = request.form.get('destination')
        title            = request.form.get('title')
        description      = request.form.get('description')
        estimated_budget = request.form.get('estimated_budget')
        duration_days    = request.form.get('duration_days')
        is_public        = True if request.form.get('is_public') == 'on' else False

        if not destination or not title:
            flash('Destination and title are required.', 'error')
            return redirect(url_for('community.new_wishlist'))

        wishlist = Wishlist(
            user_id          = current_user.id,
            destination      = destination,
            title            = title,
            description      = description,
            estimated_budget = float(estimated_budget) if estimated_budget else 0,
            duration_days    = int(duration_days) if duration_days else 0,
            is_public        = is_public,
            created_at       = datetime.utcnow()
        )

        db.session.add(wishlist)
        db.session.commit()
        flash('Wishlist shared successfully.', 'success')
        return redirect(url_for('community.community'))

    return render_template('new_wishlist.html')


@community_bp.route('/community/<int:id>')
def wishlist_detail(id):
    wishlist = Wishlist.query.filter_by(id=id, is_public=True).first_or_404()
    return render_template('wishlist_detail.html', wishlist=wishlist)
