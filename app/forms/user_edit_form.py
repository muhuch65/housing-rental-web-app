from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class UserEditForm(FlaskForm):
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

    role = SelectField(
        "Роль",
        choices=[
            ("user", "Пользователь"),
            ("admin", "Администратор"),
        ],
        validators=[
            DataRequired(message="Выберите роль"),
        ],
    )

    is_active_account = SelectField(
        "Статус аккаунта",
        choices=[
            ("1", "Активен"),
            ("0", "Заблокирован"),
        ],
        validators=[
            DataRequired(message="Выберите статус"),
        ],
    )

    submit = SubmitField("Сохранить")
