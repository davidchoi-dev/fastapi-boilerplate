from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from core.config import get_config

engine = create_engine(get_config().DB_URL, pool_recycle=3600)
session: Union[Session, scoped_session] = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)
Base = declarative_base()
