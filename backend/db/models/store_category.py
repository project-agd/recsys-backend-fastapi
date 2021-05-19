from sqlalchemy import Column, String, BigInteger

from backend.db.database import Base


class StoreCategory(Base):
    __tablename__ = 'store_category'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
