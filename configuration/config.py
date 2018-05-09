import os
import sys


SECRET_KEY = "some_strong_bullshit"

APP_NAME = "EduCerts"
CSRF_ENABLED = True
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_SALT = 'some_very_strong_and_stupid_text'
SECURITY_DEFAULT_REMEMBER_ME = True
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True

MAIL_SERVER = 'smtp.mail.ru'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'notifications_test@bk.ru'
MAIL_PASSWORD = 'Qwerty!@'