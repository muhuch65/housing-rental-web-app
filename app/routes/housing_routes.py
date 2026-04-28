from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.forms.housing_filter_form import HousingFilterForm
from app.forms.housing_form import HousingForm
from app.services.housing_service import HousingService
from app.utils.decorators import admin_required

housing_bp = Blueprint("housing", __name__)


@housing_bp.route("/housing")
def housing_list():
    form = HousingFilterForm(request.args, meta={"csrf": False})

    search = request.args.get("search", "").strip()
    housing_type = request.args.get("housing_type", "").strip()
    status = request.args.get("status", "").strip()
    rooms = request.args.get("rooms", "").strip()
    sort = request.args.get("sort", "newest").strip()

    min_price = request.args.get("min_price", type=int)
    max_price = request.args.get("max_price", type=int)

    housing_items = HousingService.search_objects(
        search=search,
        housing_type=housing_type,
        status=status,
        min_price=min_price,
        max_price=max_price,
        rooms=rooms,
        sort=sort,
    )

    return render_template(
        "housing_list.html",
        housing_items=housing_items,
        form=form,
        total_count=len(housing_items),
    )


@housing_bp.route("/housing/<int:housing_id>")
def housing_detail(housing_id):
    housing = HousingService.get_object_by_id(housing_id)

    if not housing:
        abort(404)

    return render_template("housing_detail.html", housing=housing)


@housing_bp.route("/admin/housing")
@login_required
@admin_required
def admin_housing_list():
    form = HousingFilterForm(request.args, meta={"csrf": False})

    search = request.args.get("search", "").strip()
    housing_type = request.args.get("housing_type", "").strip()
    status = request.args.get("status", "").strip()
    rooms = request.args.get("rooms", "").strip()
    sort = request.args.get("sort", "newest").strip()

    min_price = request.args.get("min_price", type=int)
    max_price = request.args.get("max_price", type=int)

    housing_items = HousingService.search_objects(
        search=search,
        housing_type=housing_type,
        status=status,
        min_price=min_price,
        max_price=max_price,
        rooms=rooms,
        sort=sort,
    )

    return render_template(
        "admin/housing.html",
        housing_items=housing_items,
        form=form,
        total_count=len(housing_items),
    )


@housing_bp.route("/admin/housing/create", methods=["GET", "POST"])
@login_required
@admin_required
def admin_housing_create():
    form = HousingForm()

    if form.validate_on_submit():
        HousingService.create_object(
            title=form.title.data,
            address=form.address.data,
            price=form.price.data,
            rooms=form.rooms.data,
            area=form.area.data,
            housing_type=form.housing_type.data,
            status=form.status.data,
            description=form.description.data,
        )

        flash("Объект аренды успешно добавлен", "success")
        return redirect(url_for("housing.admin_housing_list"))

    return render_template("admin/housing_create.html", form=form)


@housing_bp.route("/admin/housing/<int:housing_id>")
@login_required
@admin_required
def admin_housing_detail(housing_id):
    housing = HousingService.get_object_by_id(housing_id)

    if not housing:
        abort(404)

    return render_template("admin/housing_detail_admin.html", housing=housing)


@housing_bp.route("/admin/housing/<int:housing_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def admin_housing_edit(housing_id):
    housing = HousingService.get_object_by_id(housing_id)

    if not housing:
        abort(404)

    form = HousingForm(obj=housing)

    if form.validate_on_submit():
        updated_object, error = HousingService.update_object(
            object_id=housing.id,
            title=form.title.data,
            address=form.address.data,
            price=form.price.data,
            rooms=form.rooms.data,
            area=form.area.data,
            housing_type=form.housing_type.data,
            status=form.status.data,
            description=form.description.data,
        )

        if error:
            flash(error, "danger")
            return render_template(
                "admin/housing_edit.html", form=form, housing=housing
            )

        flash("Объект аренды успешно обновлён", "success")
        return redirect(
            url_for("housing.admin_housing_detail", housing_id=updated_object.id)
        )

    return render_template("admin/housing_edit.html", form=form, housing=housing)


@housing_bp.route("/admin/housing/<int:housing_id>/delete", methods=["POST"])
@login_required
@admin_required
def admin_housing_delete(housing_id):
    success, error = HousingService.delete_object(housing_id)

    if error:
        flash(error, "danger")
    else:
        flash("Объект аренды удалён", "success")

    return redirect(url_for("housing.admin_housing_list"))
