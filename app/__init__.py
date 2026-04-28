from flask import Flask
from flask_login import LoginManager

from app.config import Config
from app.database import init_database
from app.models.user import User

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Для доступа к странице необходимо войти в систему."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_database(app)
    login_manager.init_app(app)

    from app.models import RentalObject, RentalRequest, User
    from app.routes.admin_routes import admin_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.housing_routes import housing_bp
    from app.routes.main_routes import main_bp
    from app.routes.request_routes import request_bp
    from app.routes.user_routes import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(housing_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(admin_bp)

    from app.commands.db_commands import register_db_commands
    from app.utils.error_handlers import register_error_handlers

    register_db_commands(app)
    register_error_handlers(app)

    return app
