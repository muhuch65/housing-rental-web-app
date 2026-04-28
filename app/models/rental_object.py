from app.database import db


class RentalObject(db.Model):
    __tablename__ = "rental_objects"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    address = db.Column(db.String(255), nullable=False)

    price = db.Column(db.Integer, nullable=False)

    rooms = db.Column(db.Integer, nullable=False)

    area = db.Column(db.Float, nullable=False)

    housing_type = db.Column(db.String(50), nullable=False, default="Квартира")

    status = db.Column(db.String(30), nullable=False, default="Доступно")

    description = db.Column(db.Text, nullable=True)

    rental_requests = db.relationship(
        "RentalRequest",
        back_populates="rental_object",
        cascade="all, delete-orphan",
    )

    def is_available(self):
        return self.status == "Доступно"

    def __repr__(self):
        return f"<RentalObject {self.title}>"
