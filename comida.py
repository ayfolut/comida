import os
from comida import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'production')

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)
