
from sqlalchemy import create_engine, MetaData, Table

from sqlalchemy.orm import mapper, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgres://zyfyaacx:Sots53T4Hheq7h2pygbKPTSsMNXdvjlt@dumbo.db.elephantsql.com:5432/zyfyaacx', echo=False)
session_for_sec = sessionmaker(bind=engine, autoflush=False, autocommit=False)
db_session = scoped_session(session_for_sec)


Base = declarative_base(bind=engine)
Base.query = db_session.query_property()



from app.database import models
def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(models.UserAccount).all()
    print(res[0].email)
    print(res[0].get_security_payload())
