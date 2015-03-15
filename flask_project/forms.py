__author__ = 'masawant'
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import Form, TextField, PasswordField, validators, BooleanField


class LoginForm(Form):
    username = StringField('Username', [validators.required(),validators.email()])
    password = PasswordField('Password', [validators.required()])
    remember_me = BooleanField('Remember me', default = False)

class SignupForm(Form):
    username = StringField('Username(email)', [validators.email()])
    password = PasswordField('New Password',
                             [validators.required(),
                              validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    agree = BooleanField('I accept the TOS', [validators.required()])

class RegistrationForm(Form):
    name = StringField('name', validators=[DataRequired()])