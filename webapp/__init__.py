from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from os import path
from .config import DB_name

db = SQLAlchemy()
migrate = Migrate(db)
login_mgr = None
mail_mgr = Mail()


def create_app():
    from .config import DevelopmentConfig
    from .views.home import main_print
    from .views.scrape import scrape_print
    from .views.search import search_print
    from .auth.auth import auth_blueprint
    from .views.personal import personal_print

    app = Flask(__name__)

    db.init_app(app)

    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(main_print, url_prefix="/")
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(scrape_print, url_prefix="/scrape")
    app.register_blueprint(search_print, url_prefix="/")
    app.register_blueprint(personal_print, url_prefix="/personal")

    create_database(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.auth.login'

    # login_manager.init_app(app)
    migrate.init_app(app, db)

    from webapp.models import User

    # mail_mgr.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('webapp/' + DB_name):
        db.create_all(app=app)
        print('Created Database!')
