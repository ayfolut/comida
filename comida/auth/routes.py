from . import bp
from flask import redirect, render_template, url_for,request,  flash, current_app,  session, request
from .forms import LoginForm , RegistrationForm
from ..models import User, db
from flask_login import login_user, logout_user, current_user



@bp.route('/')
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('root.index'))
    login_form = LoginForm()
    registration_form = RegistrationForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.login_email.data).first()
        if user is None or not user.check_password(login_form.login_password_b.data):
            flash("Invalid username or password")
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('root.index'))
    else:
        print('no')

    
    return render_template('login.html', login_form=login_form, registration_form=registration_form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    registration_form = RegistrationForm()
    login_form =LoginForm()
    if registration_form.validate_on_submit():
        user = User(username=registration_form.username.data, email=registration_form.email.data)
        user.set_password(registration_form.password2.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, You have been registered')
        return redirect(url_for('auth.login'))

    else:
        print('nojjjt')


    return render_template('login.html', login_form=login_form, registration_form=registration_form)
    

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

