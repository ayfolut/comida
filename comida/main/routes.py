from . import bp
from flask import redirect, url_for, render_template
from . import root
from .. import login
from flask_login import login_required



@root.route('/')
@root.route('/home')
@login_required

def index():
    return render_template ('index.html')