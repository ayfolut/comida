from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
login.session_protection = 'strong'
login.login_view = 'auth.login'



def create_app(config_class='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_class])

    db.init_app(app)
    from . import models
    migrate.init_app(app, db)
    login.init_app(app)

    """ blueprint registrations"""
    from comida.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from comida.shop import bp as shop_bp
    app.register_blueprint(shop_bp, url_prefix='/shop')

    from comida.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/home')

    from comida.main import root as root_bp
    app.register_blueprint(root_bp)




    return app


#app = create_app('production')

    