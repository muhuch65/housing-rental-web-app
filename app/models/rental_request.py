from datetime import datetime

from app.database import db


class RentalRequest(db.Model):
    __tablename__ = "rental_requests"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    rental_object_id = db.Column(
        db.Integer,
        db.ForeignKey("rental_objects.id"),
        nullable=False,
        index=True,
    )

    status = db.Column(db.String(30), nullable=False, default="На рассмотрении")

    message = db.Column(db.Text, nullable=True)

    admin_comment = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    user = db.relationship("User", back_populates="rental_requests")

    rental_object = db.relationship("RentalObject", back_populates="rental_requests")

    def is_pending(self):
        return self.status == "На рассмотрении"

    def is_approved(self):
        return self.status == "Одобрена"

    def is_rejected(self):
        return self.status == "Отклонена"

    def __repr__(self):
        return f"<RentalRequest {self.id}>"
