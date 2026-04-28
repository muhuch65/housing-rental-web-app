from app.database import db
from app.models.user import User


class UserService:
    @staticmethod
    def get_all_users():
        return User.query.order_by(User.id.asc()).all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def update_user(user_id, name, email, role, is_active_account):
        user = UserService.get_user_by_id(user_id)

        if not user:
            return None, "Пользователь не найден"

        existing_user = UserService.get_user_by_email(email)

        if existing_user and existing_user.id != user.id:
            return None, "Пользователь с таким email уже существует"

        user.name = name
        user.email = email
        user.role = role
        user.is_active_account = is_active_account

        db.session.commit()

        return user, None

    @staticmethod
    def block_user(user_id):
        user = UserService.get_user_by_id(user_id)

        if not user:
            return None, "Пользователь не найден"

        user.is_active_account = False
        db.session.commit()

        return user, None

    @staticmethod
    def unblock_user(user_id):
        user = UserService.get_user_by_id(user_id)

        if not user:
            return None, "Пользователь не найден"

        user.is_active_account = True
        db.session.commit()

        return user, None

    @staticmethod
    def delete_user(user_id):
        user = UserService.get_user_by_id(user_id)

        if not user:
            return False, "Пользователь не найден"

        db.session.delete(user)
        db.session.commit()

        return True, None
