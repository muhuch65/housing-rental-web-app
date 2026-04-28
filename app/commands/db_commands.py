import click

from app.database import db
from app.models.rental_object import RentalObject
from app.models.user import User


def register_db_commands(app):
    @app.cli.command("create-db")
    def create_db():
        db.create_all()
        click.echo("База данных создана.")

    @app.cli.command("drop-db")
    def drop_db():
        db.drop_all()
        click.echo("Все таблицы удалены.")

    @app.cli.command("reset-db")
    def reset_db():
        db.drop_all()
        db.create_all()
        click.echo("База данных пересоздана.")

    @app.cli.command("make-admin")
    @click.argument("email")
    def make_admin(email):
        user = User.query.filter_by(email=email).first()

        if not user:
            click.echo("Пользователь не найден.")
            return

        user.role = "admin"
        db.session.commit()

        click.echo(f"Пользователь {email} назначен администратором.")

    @app.cli.command("seed-housing")
    def seed_housing():
        apartments = [
            {
                "title": "Однокомнатная квартира",
                "address": "г. Ставрополь, ул. Ленина, 15",
                "price": 25000,
                "rooms": 1,
                "area": 38.0,
                "housing_type": "Квартира",
                "status": "Доступно",
                "description": "Уютная однокомнатная квартира рядом с остановкой, магазинами и аптекой.",
            },
            {
                "title": "Двухкомнатная квартира",
                "address": "г. Ставрополь, ул. Мира, 42",
                "price": 35000,
                "rooms": 2,
                "area": 56.0,
                "housing_type": "Квартира",
                "status": "Доступно",
                "description": "Просторная квартира с мебелью, бытовой техникой и раздельными комнатами.",
            },
            {
                "title": "Студия в новом доме",
                "address": "г. Ставрополь, ул. Доваторцев, 21",
                "price": 22000,
                "rooms": 1,
                "area": 29.5,
                "housing_type": "Студия",
                "status": "Доступно",
                "description": "Современная студия с ремонтом, кухонной зоной и удобной транспортной доступностью.",
            },
            {
                "title": "Трёхкомнатная квартира",
                "address": "г. Ставрополь, пр-т Кулакова, 8",
                "price": 48000,
                "rooms": 3,
                "area": 74.0,
                "housing_type": "Квартира",
                "status": "Занято",
                "description": "Большая квартира для семьи, рядом школа, детский сад и продуктовые магазины.",
            },
            {
                "title": "Комната в квартире",
                "address": "г. Ставрополь, ул. Пушкина, 10",
                "price": 12000,
                "rooms": 1,
                "area": 18.0,
                "housing_type": "Комната",
                "status": "Доступно",
                "description": "Отдельная комната в квартире, подходит для студента или одного жильца.",
            },
            {
                "title": "Квартира бизнес-класса",
                "address": "г. Ставрополь, ул. 50 лет ВЛКСМ, 93",
                "price": 60000,
                "rooms": 2,
                "area": 68.0,
                "housing_type": "Квартира",
                "status": "Доступно",
                "description": "Квартира с качественным ремонтом, закрытой территорией и парковочным местом.",
            },
            {
                "title": "Небольшой частный дом",
                "address": "г. Ставрополь, ул. Южная, 5",
                "price": 40000,
                "rooms": 3,
                "area": 82.0,
                "housing_type": "Дом",
                "status": "На обслуживании",
                "description": "Частный дом с участком, временно недоступен из-за технического обслуживания.",
            },
        ]

        added_count = 0
        skipped_count = 0

        for item in apartments:
            existing = RentalObject.query.filter_by(
                title=item["title"],
                address=item["address"],
            ).first()

            if existing:
                skipped_count += 1
                continue

            db.session.add(RentalObject(**item))
            added_count += 1

        db.session.commit()

        click.echo(f"Добавлено объектов: {added_count}")
        click.echo(f"Пропущено дубликатов: {skipped_count}")
