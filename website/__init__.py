from flask import Flask
from .db import db
from .config import config as app_config
from .loginManager import login_manager
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config['dev'])
    db.init_app(app)  # type: ignore
    login_manager.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth')
    return app
