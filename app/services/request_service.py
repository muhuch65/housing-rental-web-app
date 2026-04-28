from app.database import db
from app.models.rental_object import RentalObject
from app.models.rental_request import RentalRequest


class RequestService:
    @staticmethod
    def get_all_requests():
        return RentalRequest.query.order_by(RentalRequest.id.desc()).all()

    @staticmethod
    def get_request_by_id(request_id):
        return RentalRequest.query.get(request_id)

    @staticmethod
    def get_user_requests(user_id):
        return (
            RentalRequest.query.filter_by(user_id=user_id)
            .order_by(RentalRequest.id.desc())
            .all()
        )

    @staticmethod
    def get_pending_count():
        return RentalRequest.query.filter_by(status="На рассмотрении").count()

    @staticmethod
    def get_total_count():
        return RentalRequest.query.count()

    @staticmethod
    def create_request(user_id, rental_object_id, message=None):
        rental_object = RentalObject.query.get(rental_object_id)

        if not rental_object:
            return None, "Объект аренды не найден"

        if not rental_object.is_available():
            return None, "Нельзя оставить заявку на недоступный объект"

        existing_request = RentalRequest.query.filter_by(
            user_id=user_id,
            rental_object_id=rental_object_id,
            status="На рассмотрении",
        ).first()

        if existing_request:
            return None, "У вас уже есть активная заявка на этот объект"

        rental_request = RentalRequest(
            user_id=user_id,
            rental_object_id=rental_object_id,
            message=message,
            status="На рассмотрении",
        )

        db.session.add(rental_request)
        db.session.commit()

        return rental_request, None

    @staticmethod
    def approve_request(request_id, admin_comment=None):
        rental_request = RequestService.get_request_by_id(request_id)

        if not rental_request:
            return None, "Заявка не найдена"

        if rental_request.status != "На рассмотрении":
            return None, "Можно обработать только заявку со статусом 'На рассмотрении'"

        rental_request.status = "Одобрена"
        rental_request.admin_comment = admin_comment

        rental_request.rental_object.status = "Занято"

        db.session.commit()

        return rental_request, None

    @staticmethod
    def reject_request(request_id, admin_comment=None):
        rental_request = RequestService.get_request_by_id(request_id)

        if not rental_request:
            return None, "Заявка не найдена"

        if rental_request.status != "На рассмотрении":
            return None, "Можно обработать только заявку со статусом 'На рассмотрении'"

        rental_request.status = "Отклонена"
        rental_request.admin_comment = admin_comment

        db.session.commit()

        return rental_request, None

    @staticmethod
    def cancel_request(request_id, user_id):
        rental_request = RequestService.get_request_by_id(request_id)

        if not rental_request:
            return None, "Заявка не найдена"

        if rental_request.user_id != user_id:
            return None, "Нельзя отменить чужую заявку"

        if rental_request.status != "На рассмотрении":
            return None, "Можно отменить только заявку на рассмотрении"

        rental_request.status = "Отменена"

        db.session.commit()

        return rental_request, None

    @staticmethod
    def delete_request(request_id):
        rental_request = RequestService.get_request_by_id(request_id)

        if not rental_request:
            return False, "Заявка не найдена"

        db.session.delete(rental_request)
        db.session.commit()

        return True, None
