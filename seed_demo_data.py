from app import create_app
from app.database import db
from app.models.rental_object import RentalObject
from app.models.rental_request import RentalRequest
from app.models.user import User

app = create_app()


def create_user(name, email, password, role="user"):
    user = User.query.filter_by(email=email).first()

    if user:
        return user

    user = User(
        name=name,
        email=email,
        role=role,
        is_active_account=True,
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user


def create_rental_object(data):
    existing = RentalObject.query.filter_by(
        title=data["title"],
        address=data["address"],
    ).first()

    if existing:
        return existing

    rental_object = RentalObject(**data)
    db.session.add(rental_object)
    db.session.commit()

    return rental_object


def create_request(
    user, rental_object, status="На рассмотрении", message=None, admin_comment=None
):
    existing = RentalRequest.query.filter_by(
        user_id=user.id,
        rental_object_id=rental_object.id,
        status=status,
    ).first()

    if existing:
        return existing

    rental_request = RentalRequest(
        user_id=user.id,
        rental_object_id=rental_object.id,
        status=status,
        message=message,
        admin_comment=admin_comment,
    )

    db.session.add(rental_request)

    if status == "Одобрена":
        rental_object.status = "Занято"

    db.session.commit()

    return rental_request


apartments = [
    {
        "title": "Однокомнатная квартира",
        "address": "г. Ставрополь, ул. Ленина, 15",
        "price": 25000,
        "rooms": 1,
        "area": 38.0,
        "housing_type": "Квартира",
        "status": "Доступно",
        "description": "Уютная квартира рядом с остановкой, магазинами и аптекой.",
    },
    {
        "title": "Двухкомнатная квартира",
        "address": "г. Ставрополь, ул. Мира, 42",
        "price": 35000,
        "rooms": 2,
        "area": 56.0,
        "housing_type": "Квартира",
        "status": "Доступно",
        "description": "Просторная квартира с мебелью и бытовой техникой.",
    },
    {
        "title": "Студия в новом доме",
        "address": "г. Ставрополь, ул. Доваторцев, 21",
        "price": 22000,
        "rooms": 1,
        "area": 29.5,
        "housing_type": "Студия",
        "status": "Доступно",
        "description": "Современная студия с ремонтом и кухонной зоной.",
    },
    {
        "title": "Трёхкомнатная квартира",
        "address": "г. Ставрополь, пр-т Кулакова, 8",
        "price": 48000,
        "rooms": 3,
        "area": 74.0,
        "housing_type": "Квартира",
        "status": "Доступно",
        "description": "Большая квартира для семьи рядом со школой.",
    },
    {
        "title": "Комната в квартире",
        "address": "г. Ставрополь, ул. Пушкина, 10",
        "price": 12000,
        "rooms": 1,
        "area": 18.0,
        "housing_type": "Комната",
        "status": "Доступно",
        "description": "Отдельная комната для студента или одного жильца.",
    },
    {
        "title": "Квартира бизнес-класса",
        "address": "г. Ставрополь, ул. 50 лет ВЛКСМ, 93",
        "price": 60000,
        "rooms": 2,
        "area": 68.0,
        "housing_type": "Квартира",
        "status": "Доступно",
        "description": "Квартира с качественным ремонтом и парковочным местом.",
    },
    {
        "title": "Небольшой частный дом",
        "address": "г. Ставрополь, ул. Южная, 5",
        "price": 40000,
        "rooms": 3,
        "area": 82.0,
        "housing_type": "Дом",
        "status": "На обслуживании",
        "description": "Частный дом с участком, временно на обслуживании.",
    },
]


with app.app_context():
    db.drop_all()
    db.create_all()

    admin = create_user(
        name="Администратор",
        email="admin@example.com",
        password="admin123",
        role="admin",
    )

    user1 = create_user(
        name="Иван Петров",
        email="ivan@example.com",
        password="user123",
    )

    user2 = create_user(
        name="Мария Соколова",
        email="maria@example.com",
        password="user123",
    )

    user3 = create_user(
        name="Алексей Иванов",
        email="alexey@example.com",
        password="user123",
    )

    objects = [create_rental_object(item) for item in apartments]

    create_request(
        user=user1,
        rental_object=objects[0],
        status="На рассмотрении",
        message="Хочу посмотреть квартиру на этой неделе.",
    )

    create_request(
        user=user2,
        rental_object=objects[1],
        status="Одобрена",
        message="Интересует аренда на длительный срок.",
        admin_comment="Заявка одобрена. Объект закреплён за пользователем.",
    )

    create_request(
        user=user3,
        rental_object=objects[2],
        status="Отклонена",
        message="Можно ли заселиться завтра?",
        admin_comment="Заявка отклонена из-за отсутствия свободного времени для показа.",
    )

    create_request(
        user=user1,
        rental_object=objects[4],
        status="Отменена",
        message="Передумал арендовать комнату.",
    )

print("Демонстрационная база данных успешно подготовлена.")
print("Администратор: admin@example.com / admin123")
print("Пользователи:")
print("ivan@example.com / user123")
print("maria@example.com / user123")
print("alexey@example.com / user123")
