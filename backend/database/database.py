from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend import env

engine = create_engine(
    url=f'{env.MAIN_DATABASE_MYSQL_HOST}/{env.MAIN_DATABASE_MYSQL_DATABASE_NAME}',
    encoding='utf-8',
    echo=True
)

session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
