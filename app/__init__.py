import logging

from flask import Flask, render_template
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()



def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.run(debug=True)
    # Load the config file specified by the APP environment variable
    
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Registro de los filtros
    # register_filters(app)

    # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    # from .admin import admin_bp
    # app.register_blueprint(admin_bp)

    # from .public import public_bp
    # app.register_blueprint(public_bp)

    # Custom error handlers
    # register_error_handlers(app)

    return app