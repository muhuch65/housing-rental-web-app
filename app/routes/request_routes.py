from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.forms.rental_request_form import RentalRequestForm
from app.services.housing_service import HousingService
from app.services.request_service import RequestService
from app.utils.decorators import admin_required

request_bp = Blueprint("requests", __name__)


@request_bp.route("/housing/<int:housing_id>/request", methods=["GET", "POST"])
@login_required
def create_request(housing_id):
    housing = HousingService.get_object_by_id(housing_id)

    if not housing:
        abort(404)

    form = RentalRequestForm()

    if form.validate_on_submit():
        rental_request, error = RequestService.create_request(
            user_id=current_user.id,
            rental_object_id=housing.id,
            message=form.message.data,
        )

        if error:
            flash(error, "danger")
            return render_template(
                "housing_detail.html",
                housing=housing,
                request_form=form,
            )

        flash("Заявка на аренду успешно отправлена", "success")
        return redirect(url_for("requests.my_requests"))

    return render_template(
        "housing_detail.html",
        housing=housing,
        request_form=form,
    )


@request_bp.route("/my-requests")
@login_required
def my_requests():
    rental_requests = RequestService.get_user_requests(current_user.id)

    return render_template(
        "user/my_requests.html",
        rental_requests=rental_requests,
    )


@request_bp.route("/my-requests/<int:request_id>/cancel", methods=["POST"])
@login_required
def cancel_request(request_id):
    rental_request, error = RequestService.cancel_request(
        request_id=request_id,
        user_id=current_user.id,
    )

    if error:
        flash(error, "danger")
    else:
        flash("Заявка отменена", "success")

    return redirect(url_for("requests.my_requests"))


@request_bp.route("/admin/requests")
@login_required
@admin_required
def admin_requests():
    rental_requests = RequestService.get_all_requests()

    return render_template(
        "admin/requests.html",
        rental_requests=rental_requests,
    )


@request_bp.route("/admin/requests/<int:request_id>")
@login_required
@admin_required
def admin_request_detail(request_id):
    rental_request = RequestService.get_request_by_id(request_id)

    if not rental_request:
        abort(404)

    return render_template(
        "admin/request_detail.html",
        rental_request=rental_request,
    )


@request_bp.route("/admin/requests/<int:request_id>/approve", methods=["POST"])
@login_required
@admin_required
def approve_request(request_id):
    admin_comment = request.form.get("admin_comment", "").strip()

    rental_request, error = RequestService.approve_request(
        request_id=request_id,
        admin_comment=admin_comment,
    )

    if error:
        flash(error, "danger")
    else:
        flash("Заявка одобрена", "success")

    return redirect(url_for("requests.admin_request_detail", request_id=request_id))


@request_bp.route("/admin/requests/<int:request_id>/reject", methods=["POST"])
@login_required
@admin_required
def reject_request(request_id):
    admin_comment = request.form.get("admin_comment", "").strip()

    rental_request, error = RequestService.reject_request(
        request_id=request_id,
        admin_comment=admin_comment,
    )

    if error:
        flash(error, "danger")
    else:
        flash("Заявка отклонена", "success")

    return redirect(url_for("requests.admin_request_detail", request_id=request_id))


@request_bp.route("/admin/requests/<int:request_id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_request(request_id):
    success, error = RequestService.delete_request(request_id)

    if error:
        flash(error, "danger")
    else:
        flash("Заявка удалена", "success")

    return redirect(url_for("requests.admin_requests"))
