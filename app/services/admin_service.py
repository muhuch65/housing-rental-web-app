from app.models.rental_object import RentalObject
from app.models.rental_request import RentalRequest
from app.models.user import User


class AdminService:
    @staticmethod
    def get_dashboard_data():
        return {
            "users_count": User.query.count(),
            "admins_count": User.query.filter_by(role="admin").count(),
            "objects_count": RentalObject.query.count(),
            "available_objects_count": RentalObject.query.filter_by(
                status="Доступно"
            ).count(),
            "occupied_objects_count": RentalObject.query.filter_by(
                status="Занято"
            ).count(),
            "maintenance_objects_count": RentalObject.query.filter_by(
                status="На обслуживании"
            ).count(),
            "requests_count": RentalRequest.query.count(),
            "pending_requests_count": RentalRequest.query.filter_by(
                status="На рассмотрении"
            ).count(),
            "approved_requests_count": RentalRequest.query.filter_by(
                status="Одобрена"
            ).count(),
            "rejected_requests_count": RentalRequest.query.filter_by(
                status="Отклонена"
            ).count(),
            "cancelled_requests_count": RentalRequest.query.filter_by(
                status="Отменена"
            ).count(),
        }

    @staticmethod
    def get_latest_users(limit=5):
        return User.query.order_by(User.id.desc()).limit(limit).all()

    @staticmethod
    def get_latest_objects(limit=5):
        return RentalObject.query.order_by(RentalObject.id.desc()).limit(limit).all()

    @staticmethod
    def get_latest_requests(limit=5):
        return RentalRequest.query.order_by(RentalRequest.id.desc()).limit(limit).all()
