from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app.forms.user_edit_form import UserEditForm
from app.services.user_service import UserService
from app.utils.decorators import admin_required

user_bp = Blueprint("users", __name__, url_prefix="/admin/users")


@user_bp.route("/")
@login_required
@admin_required
def users_list():
    users = UserService.get_all_users()
    return render_template("admin/users.html", users=users)


@user_bp.route("/<int:user_id>")
@login_required
@admin_required
def user_detail(user_id):
    user = UserService.get_user_by_id(user_id)

    if not user:
        abort(404)

    return render_template("admin/user_detail.html", user=user)


@user_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def user_edit(user_id):
    user = UserService.get_user_by_id(user_id)

    if not user:
        abort(404)

    form = UserEditForm(obj=user)

    if form.validate_on_submit():
        is_active_account = form.is_active_account.data == "1"

        updated_user, error = UserService.update_user(
            user_id=user.id,
            name=form.name.data,
            email=form.email.data,
            role=form.role.data,
            is_active_account=is_active_account,
        )

        if error:
            flash(error, "danger")
            return render_template("admin/user_edit.html", form=form, user=user)

        flash("Данные пользователя успешно обновлены", "success")
        return redirect(url_for("users.user_detail", user_id=updated_user.id))

    form.role.data = user.role
    form.is_active_account.data = "1" if user.is_active_account else "0"

    return render_template("admin/user_edit.html", form=form, user=user)


@user_bp.route("/<int:user_id>/block", methods=["POST"])
@login_required
@admin_required
def user_block(user_id):
    if current_user.id == user_id:
        flash("Нельзя заблокировать собственный аккаунт", "danger")
        return redirect(url_for("users.users_list"))

    user, error = UserService.block_user(user_id)

    if error:
        flash(error, "danger")
    else:
        flash("Пользователь заблокирован", "success")

    return redirect(url_for("users.users_list"))


@user_bp.route("/<int:user_id>/unblock", methods=["POST"])
@login_required
@admin_required
def user_unblock(user_id):
    user, error = UserService.unblock_user(user_id)

    if error:
        flash(error, "danger")
    else:
        flash("Пользователь разблокирован", "success")

    return redirect(url_for("users.users_list"))


@user_bp.route("/<int:user_id>/delete", methods=["POST"])
@login_required
@admin_required
def user_delete(user_id):
    if current_user.id == user_id:
        flash("Нельзя удалить собственный аккаунт", "danger")
        return redirect(url_for("users.users_list"))

    success, error = UserService.delete_user(user_id)

    if error:
        flash(error, "danger")
    else:
        flash("Пользователь удалён", "success")

    return redirect(url_for("users.users_list"))
