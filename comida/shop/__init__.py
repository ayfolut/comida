from flask import Blueprint, Flask

bp = Blueprint('shop', __name__, template_folder='templates', static_folder='static')



from comida.shop import routes