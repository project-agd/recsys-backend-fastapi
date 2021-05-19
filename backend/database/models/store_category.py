from sqlalchemy import Column, String, BigInteger

from backend.database.database import Base


class VisitLog(Base):
    __tablename__ = 'store_category'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
