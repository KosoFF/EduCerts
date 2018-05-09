from flask_mail import Mail


mail = None


def init_mail(app):
    global mail
    mail = Mail(app)
