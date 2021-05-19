from sqlalchemy import Column, String, Integer, BigInteger

from backend.database.database import Base


class VisitLog(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    sex = Column(String)
