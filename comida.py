import os
from comida import db, create_app
from flask_sqlalchemy import SQLAlchemy


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)
