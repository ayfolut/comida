from flask import Blueprint, Flask

bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')



from comida.auth import routes


