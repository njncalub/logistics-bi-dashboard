from sqlalchemy import create_engine

from .models.models import BaseModel


def initialize_database(engine):
    db_engine = create_engine(engine)
    BaseModel.metadata.create_all(db_engine)
