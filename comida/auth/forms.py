from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, DateField,SubmitField, BooleanField
from wtforms.validators import DataRequired, URL, Email, EqualTo, ValidationError
from ..models import User

class LoginForm(FlaskForm):
    login_email = StringField('Email', validators=[DataRequired()])
    login_password_b = PasswordField('Password', validators=[DataRequired()])
    login_submit_b = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_b = PasswordField('Password', validators=[DataRequired()])
    password_b2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password_b')])
    submit_b = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')