import os
from comida import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'production')

