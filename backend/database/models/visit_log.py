from sqlalchemy import Column, String, DateTime, Float

from backend.database.database import Base


class VisitLog(Base):
    __tablename__ = 'visit_log'

    id = Column(String, primary_key=True)
    store_id = Column(String)
    user_id = Column(String)
    creation_date_time = Column(DateTime)
    update_date_time = Column(DateTime)
    name = Column(String)
    text = Column(String)
    rating = Column(Float)
