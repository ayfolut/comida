from flask import Blueprint, Flask

bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')


root = Blueprint('root', __name__, template_folder='templates', static_folder='static')

from comida.main import routes

