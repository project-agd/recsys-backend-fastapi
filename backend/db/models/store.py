from sqlalchemy import Column, String, DateTime, Float, BigInteger

from backend.db.database import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(String, primary_key=True)
    closed_on = Column(String)
    creation_date_time = Column(DateTime)
    description = Column(String)
    location = Column(String)
    name = Column(String)
    opening_hours = Column(String)
    phone = Column(String)
    rating = Column(Float)
    update_date_time = Column(DateTime)


class StoreCategory(Base):
    __tablename__ = 'store_category'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)


class StoreStoreCategoryMap(Base):
    __tablename__ = 'store_store_category_map'

    id = Column(String, primary_key=True)
    store_category_id = Column(BigInteger)
    store_id = Column(String)
