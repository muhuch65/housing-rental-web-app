from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import NumberRange, Optional


class HousingFilterForm(FlaskForm):
    search = StringField(
        "Поиск",
        validators=[Optional()],
    )

    housing_type = SelectField(
        "Тип жилья",
        choices=[
            ("", "Все типы"),
            ("Квартира", "Квартира"),
            ("Дом", "Дом"),
            ("Студия", "Студия"),
            ("Комната", "Комната"),
        ],
        validators=[Optional()],
    )

    status = SelectField(
        "Статус",
        choices=[
            ("", "Все статусы"),
            ("Доступно", "Доступно"),
            ("Занято", "Занято"),
            ("На обслуживании", "На обслуживании"),
        ],
        validators=[Optional()],
    )

    min_price = IntegerField(
        "Цена от",
        validators=[
            Optional(),
            NumberRange(min=0, message="Цена не может быть отрицательной"),
        ],
    )

    max_price = IntegerField(
        "Цена до",
        validators=[
            Optional(),
            NumberRange(min=0, message="Цена не может быть отрицательной"),
        ],
    )

    rooms = SelectField(
        "Количество комнат",
        choices=[
            ("", "Любое"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5 и более"),
        ],
        validators=[Optional()],
    )

    sort = SelectField(
        "Сортировка",
        choices=[
            ("newest", "Сначала новые"),
            ("price_asc", "Цена по возрастанию"),
            ("price_desc", "Цена по убыванию"),
            ("area_asc", "Площадь по возрастанию"),
            ("area_desc", "Площадь по убыванию"),
        ],
        validators=[Optional()],
    )

    submit = SubmitField("Применить")
