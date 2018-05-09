
from app import log
from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore
from app.database import models, loadSession

# it is needed to init security in application. fuck flask
security = None


def init_security(app):
    user_datastore = SQLAlchemySessionUserDatastore(loadSession(), models.UserAccount, models.UserRole)
    global security
    security = Security(app, user_datastore)

log.info('Init security')