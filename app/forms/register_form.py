from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    name = StringField(
        "Имя",
        validators=[
            DataRequired(message="Введите имя"),
            Length(min=2, max=100, message="Имя должно содержать от 2 до 100 символов"),
        ],
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Введите email"),
            Email(message="Введите корректный email"),
            Length(max=120, message="Email слишком длинный"),
        ],
    )

    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired(message="Введите пароль"),
            Length(
                min=6, max=100, message="Пароль должен содержать минимум 6 символов"
            ),
        ],
    )

    confirm_password = PasswordField(
        "Повторите пароль",
        validators=[
            DataRequired(message="Повторите пароль"),
            EqualTo("password", message="Пароли не совпадают"),
        ],
    )

    submit = SubmitField("Зарегистрироваться")
