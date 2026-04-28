from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))

    form = RegisterForm()

    if form.validate_on_submit():
        user, error = AuthService.register_user(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )

        if error:
            flash(error, "danger")
            return render_template("register.html", form=form)

        login_user(user)
        flash("Регистрация выполнена успешно", "success")
        return redirect(url_for("main.profile"))

    return render_template("register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))

    form = LoginForm()

    if form.validate_on_submit():
        user, error = AuthService.authenticate_user(
            email=form.email.data,
            password=form.password.data,
        )

        if error:
            flash(error, "danger")
            return render_template("login.html", form=form)

        login_user(user, remember=form.remember.data)

        next_page = request.args.get("next")

        flash("Вы успешно вошли в систему", "success")
        return redirect(next_page or url_for("main.profile"))

    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из системы", "info")
    return redirect(url_for("main.index"))
