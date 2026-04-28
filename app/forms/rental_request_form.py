from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, Optional


class RentalRequestForm(FlaskForm):
    message = TextAreaField(
        "Комментарий к заявке",
        validators=[
            Optional(),
            Length(max=1000, message="Комментарий не должен превышать 1000 символов"),
        ],
    )

    submit = SubmitField("Оставить заявку")
