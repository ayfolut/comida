from . import bp
from flask import redirect, url_for, render_template
from . import root
from .. import login
from flask_login import login_required



@root.route('/')
@root.route('/home')

def index():
    return render_template ('index.html')

@root.route('/profile')
def profile():
    return render_template('profile.html')

@root.route('/pay')
def pay():
    return render_template('pay.html')