from . import bp
from flask import redirect, render_template, url_for, current_app, session, request



@bp.route('/')
@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')