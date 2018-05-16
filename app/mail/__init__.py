from flask_mail import Mail





def init_mail(app):
    global mail
    mail = Mail(app)
