from flask_wtf import FlaskForm
from wtforms import (
    FloatField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class HousingForm(FlaskForm):
    title = StringField(
        "Название объекта",
        validators=[
            DataRequired(message="Введите название объекта"),
            Length(
                min=3, max=150, message="Название должно содержать от 3 до 150 символов"
            ),
        ],
    )

    address = StringField(
        "Адрес",
        validators=[
            DataRequired(message="Введите адрес"),
            Length(
                min=5, max=255, message="Адрес должен содержать от 5 до 255 символов"
            ),
        ],
    )

    price = IntegerField(
        "Стоимость аренды в месяц",
        validators=[
            DataRequired(message="Введите стоимость аренды"),
            NumberRange(min=1, message="Стоимость должна быть больше 0"),
        ],
    )

    rooms = IntegerField(
        "Количество комнат",
        validators=[
            DataRequired(message="Введите количество комнат"),
            NumberRange(
                min=1, max=20, message="Количество комнат должно быть от 1 до 20"
            ),
        ],
    )

    area = FloatField(
        "Площадь",
        validators=[
            DataRequired(message="Введите площадь"),
            NumberRange(min=1, message="Площадь должна быть больше 0"),
        ],
    )

    housing_type = SelectField(
        "Тип жилья",
        choices=[
            ("Квартира", "Квартира"),
            ("Дом", "Дом"),
            ("Студия", "Студия"),
            ("Комната", "Комната"),
        ],
        validators=[
            DataRequired(message="Выберите тип жилья"),
        ],
    )

    status = SelectField(
        "Статус",
        choices=[
            ("Доступно", "Доступно"),
            ("Занято", "Занято"),
            ("На обслуживании", "На обслуживании"),
        ],
        validators=[
            DataRequired(message="Выберите статус"),
        ],
    )

    description = TextAreaField(
        "Описание",
        validators=[
            Optional(),
            Length(max=1000, message="Описание не должно превышать 1000 символов"),
        ],
    )

    submit = SubmitField("Сохранить")
