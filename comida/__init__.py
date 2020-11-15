from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
 

def create_app(config_class='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_class])

    db.init_app(app)
    migrate.init_app(app)


    """ blueprint registrations"""
    from comida.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from comida.shop import bp as shop_bp
    app.register_blueprint(shop_bp, url_prefix='/shop')

    from comida.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')



    return app

    