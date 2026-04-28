from sqlalchemy import or_

from app.database import db
from app.models.rental_object import RentalObject


class HousingService:
    @staticmethod
    def get_all_objects():
        return RentalObject.query.order_by(RentalObject.id.desc()).all()

    @staticmethod
    def get_available_objects():
        return (
            RentalObject.query.filter_by(status="Доступно")
            .order_by(RentalObject.id.desc())
            .all()
        )

    @staticmethod
    def get_object_by_id(object_id):
        return RentalObject.query.get(object_id)

    @staticmethod
    def search_objects(
        search=None,
        housing_type=None,
        status=None,
        min_price=None,
        max_price=None,
        rooms=None,
        sort="newest",
    ):
        query = RentalObject.query

        if search:
            search_pattern = f"%{search.strip()}%"
            query = query.filter(
                or_(
                    RentalObject.title.ilike(search_pattern),
                    RentalObject.address.ilike(search_pattern),
                    RentalObject.description.ilike(search_pattern),
                )
            )

        if housing_type:
            query = query.filter(RentalObject.housing_type == housing_type)

        if status:
            query = query.filter(RentalObject.status == status)

        if min_price is not None:
            query = query.filter(RentalObject.price >= min_price)

        if max_price is not None:
            query = query.filter(RentalObject.price <= max_price)

        if rooms:
            if rooms == "5":
                query = query.filter(RentalObject.rooms >= 5)
            else:
                query = query.filter(RentalObject.rooms == int(rooms))

        if sort == "price_asc":
            query = query.order_by(RentalObject.price.asc())
        elif sort == "price_desc":
            query = query.order_by(RentalObject.price.desc())
        elif sort == "area_asc":
            query = query.order_by(RentalObject.area.asc())
        elif sort == "area_desc":
            query = query.order_by(RentalObject.area.desc())
        else:
            query = query.order_by(RentalObject.id.desc())

        return query.all()

    @staticmethod
    def create_object(
        title, address, price, rooms, area, housing_type, status, description
    ):
        rental_object = RentalObject(
            title=title,
            address=address,
            price=price,
            rooms=rooms,
            area=area,
            housing_type=housing_type,
            status=status,
            description=description,
        )

        db.session.add(rental_object)
        db.session.commit()

        return rental_object

    @staticmethod
    def update_object(
        object_id, title, address, price, rooms, area, housing_type, status, description
    ):
        rental_object = HousingService.get_object_by_id(object_id)

        if not rental_object:
            return None, "Объект аренды не найден"

        rental_object.title = title
        rental_object.address = address
        rental_object.price = price
        rental_object.rooms = rooms
        rental_object.area = area
        rental_object.housing_type = housing_type
        rental_object.status = status
        rental_object.description = description

        db.session.commit()

        return rental_object, None

    @staticmethod
    def delete_object(object_id):
        rental_object = HousingService.get_object_by_id(object_id)

        if not rental_object:
            return False, "Объект аренды не найден"

        db.session.delete(rental_object)
        db.session.commit()

        return True, None
