from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker


class Bookmarks(object):
    pass


# ----------------------------------------------------------------------
def loadSession():
    """"""

    engine = create_engine('postgres://zyfyaacx:Sots53T4Hheq7h2pygbKPTSsMNXdvjlt@dumbo.db.elephantsql.com:5432/zyfyaacx', echo=True)

    metadata = MetaData(engine)
    moz_bookmarks = Table('user_role', metadata, autoload=True)
    mapper(Bookmarks, moz_bookmarks)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(Bookmarks).all()
    print(res[0].user_role_note)