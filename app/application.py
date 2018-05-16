
from flask import Flask, render_template, session
# from flask.ext.sqlalchemy import SQLAlchemy
from configuration import config as cf
from flask_login import current_user
# At top of file
from werkzeug.contrib.fixers import ProxyFix



from app.mail import init_mail
from app.security import init_security




__all__ = ['create_app']




def create_app(config=None, app_name=None, blueprints=None):
    if app_name is None:
        app_name = cf.APP_NAME

    app = Flask(app_name, template_folder='app/templates', static_folder='app/static')
    configure_app(app, config)

    init_security(app)
    init_mail(app)

    from app.views import frontend
    from app.views import api
    DEFAULT_BLUEPRINTS = (
        frontend,
        api
    )
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)

    app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
    return app

def configure_hook(app):
    @app.before_request
    def before_request():
        pass
    from app.security import user_datastore
    @app.after_request
    def after_request(req):
        user_datastore.commit()
        return req

    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)


def configure_app(app, config):
    """Configure app from object, parameter and env."""
    app.config.from_object(cf)
    if config is not None:
        app.config.from_object(config)

def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extensions(app):
    # sqlalchemy config here
    # db.init_app(app)
    pass

def configure_logging(app):
    if app.debug or app.testing:
        # skip debug and test mode.
        return
    from logger import log_handler
    app.logger.addHandler(log_handler)
    app.logger.info('web app startup')

def configure_template_filters(app):
    # Jinja filters
    pass
    # Example
    # @app.template_filter()
    # def filter(value):
    #     return somefunc(value)

def configure_error_handlers(app):
    pass
    # Example
    # @app.errorhandler(403)
    # def forbidden_page(error):
#     return render_template("errors/forbidden_page.html"), 403



