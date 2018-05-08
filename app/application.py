
from flask import Flask, render_template
# from flask.ext.sqlalchemy import SQLAlchemy
from configuration import config as cf
from app.views import frontend
from app.views import api

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    frontend,
    api,
)


def create_app(config=None, app_name=None, blueprints=None):
    if app_name is None:
        app_name = cf.APP_NAME
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    app = Flask(app_name, template_folder='app/templates', static_folder='app/static')
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)
    return app

def configure_hook(app):
    @app.before_request
    def before_request():
        pass

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
