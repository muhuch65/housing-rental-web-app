from flask import Blueprint, render_template
from flask_login import login_required

from app.services.admin_service import AdminService
from app.utils.decorators import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/")
@login_required
@admin_required
def dashboard():
    statistics = AdminService.get_dashboard_data()
    latest_users = AdminService.get_latest_users()
    latest_objects = AdminService.get_latest_objects()
    latest_requests = AdminService.get_latest_requests()

    return render_template(
        "admin/dashboard.html",
        statistics=statistics,
        latest_users=latest_users,
        latest_objects=latest_objects,
        latest_requests=latest_requests,
    )
