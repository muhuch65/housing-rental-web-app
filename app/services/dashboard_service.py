from app.models.rental_object import RentalObject
from app.models.rental_request import RentalRequest
from app.models.user import User


class DashboardService:
    @staticmethod
    def get_admin_statistics():
        objects_count = RentalObject.query.count()
        users_count = User.query.count()
        requests_count = RentalRequest.query.count()

        available_objects_count = RentalObject.query.filter_by(
            status="Доступно"
        ).count()
        occupied_objects_count = RentalObject.query.filter_by(status="Занято").count()
        pending_requests_count = RentalRequest.query.filter_by(
            status="На рассмотрении"
        ).count()
        approved_requests_count = RentalRequest.query.filter_by(
            status="Одобрена"
        ).count()
        rejected_requests_count = RentalRequest.query.filter_by(
            status="Отклонена"
        ).count()

        return {
            "objects_count": objects_count,
            "users_count": users_count,
            "requests_count": requests_count,
            "available_objects_count": available_objects_count,
            "occupied_objects_count": occupied_objects_count,
            "pending_requests_count": pending_requests_count,
            "approved_requests_count": approved_requests_count,
            "rejected_requests_count": rejected_requests_count,
        }

    @staticmethod
    def get_latest_objects(limit=5):
        return RentalObject.query.order_by(RentalObject.id.desc()).limit(limit).all()

    @staticmethod
    def get_latest_requests(limit=5):
        return RentalRequest.query.order_by(RentalRequest.id.desc()).limit(limit).all()
