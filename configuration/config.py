import os
import sys
from logger import c_logger as log
from sqlalchemy.engine.url import make_url



#initialization
IS_HEROKU = False
try:
    if os.environ.get('HEROKU'):
        IS_HEROKU = True
        log.info('APPLICATION IS IN HEROKU ENVIRONMENT')
except Exception as e:
    log.error('configuration module initializaiton error' + str(e))





SECRET_KEY = "some_strong_bullshit"

APP_NAME = "EduCerts"

#FLASK SECURITY
CSRF_ENABLED = True
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_SALT = 'some_very_strong_and_stupid_text'
SECURITY_DEFAULT_REMEMBER_ME = True
SECURITY_TRACKABLE = True
SECURITY_CONFIRMABLE= False
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
SECURITY_SEND_REGISTER_EMAIL=False #testing


#Ethereum account
ACCOUNT_ADDRESS='0x11eaDA0f2416d3C79faEB2cD70D26556F0b3EDeB'
ETHERSCAN_API_KEY='IMHHCJ323XDZ3AJIPFEMYCEMP5TBC7RHPY'

#MAIL
MAIL_SERVER = 'smtp.mail.ru'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'notifications_test@bk.ru'
MAIL_PASSWORD = 'Qwerty!@'


#SQL ALCHEMY
SQLALCHEMY_DATABASE_URI = None

try:
    if (IS_HEROKU) and (os.environ["DATABASE_URL"]):
            SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
            db_params = make_url(SQLALCHEMY_DATABASE_URI)
            DB_NAME = db_params.database
            DB_HOST = db_params.host
            DB_USER = db_params.username
            DB_PORT = 5432

    if SQLALCHEMY_DATABASE_URI is None:
        log.info("Environment variable for DATABASE_URL is not defined use default ones")
        DB_HOST = 'ec2-54-204-46-236.compute-1.amazonaws.com'
        DB_NAME = 'd7j9lbgpo9jroc'
        DB_USER = 'yyozrwidyoeony'
        DB_PASSWORD = '1fc3fd0ed210a47d3d5cba1e2c715d7bbef27ba7784e04c1a31fe00fb5bf6ff3'
        DB_SSL_MODE = 'require'
        DB_PORT = 5432
        SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    # place to store generated migration scripts
    basedir = os.path.abspath(os.path.dirname(__file__))
    log.info('DB connection is ' + SQLALCHEMY_DATABASE_URI)
except KeyError as e:
    log.info("DATABASE_URL setup error:" + str(e))