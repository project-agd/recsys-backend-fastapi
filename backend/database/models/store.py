from sqlalchemy import Column, String, DateTime, Float

from backend.database.database import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(String, primary_key=True)
    creation_date_time = Column(DateTime)
    update_date_time = Column(DateTime)
    name = Column(String)
    description = Column(String)
    location = Column(String)
    opening_hours = Column(String)
    rating = Column(Float)
