from app.database import db
from app.models.user import User


class AuthService:
    @staticmethod
    def register_user(name, email, password):
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return None, "Пользователь с таким email уже существует"

        user = User(
            name=name,
            email=email,
            role="user",
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user, None

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()

        if not user:
            return None, "Пользователь с таким email не найден"

        if not user.check_password(password):
            return None, "Неверный пароль"

        if not user.is_active_account:
            return None, "Аккаунт заблокирован"

        return user, None
