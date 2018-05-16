
from app import log
from flask_security import Security, SQLAlchemySessionUserDatastore
from database import loadSession
from database import models


# it is needed to init security in application. fuck flask



def init_security(app):
    global user_datastore
    user_datastore = SQLAlchemySessionUserDatastore(loadSession(), models.UserAccount, models.UserRole)
    global security
    security = Security(app, user_datastore)
    user_datastore.remove_role_from_user(user='5@example.com', role='user')
    user_datastore.commit()

    log.info('Init security')