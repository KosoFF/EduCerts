
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from configuration.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
session_for_sec = sessionmaker(bind=engine, autoflush=False, autocommit=False)
db_session = scoped_session(session_for_sec)


Base = declarative_base(bind=engine)
Base.query = db_session.query_property()

from database import models


def loadSession():
    metadata = Base.metadata
    session = db_session
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(models.UserAccount).all()

    print(res[0].roles.append())
    print(res[0].get_security_payload())
