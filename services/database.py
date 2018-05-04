from core import settings
from data.services import DataService


def get_database():
    db = DataService(engine=settings.DATABASE_URL)
    return db


db_service = get_database()
