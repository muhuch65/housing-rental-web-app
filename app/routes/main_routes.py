from flask import Blueprint, render_template
from flask_login import current_user, login_required

from app.services.housing_service import HousingService
from app.services.request_service import RequestService

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    housing_items = HousingService.get_available_objects()[:3]
    return render_template("index.html", housing_items=housing_items)


@main_bp.route("/profile")
@login_required
def profile():
    rental_requests = RequestService.get_user_requests(current_user.id)

    return render_template(
        "profile.html",
        user=current_user,
        rental_requests=rental_requests,
    )
