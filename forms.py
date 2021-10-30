"""
This file is used to create forms  for users to register, login, etc.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, data_required, Length, Email, EqualTo

"""
Created a class to register as a user. Note the validators, and 
their requirements. Data Required means there must be something in the
input box. Length is self explanatory.
"""
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                             validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                         validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')