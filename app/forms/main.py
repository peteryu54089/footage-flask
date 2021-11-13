from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class FormLogin(FlaskForm):
    username = StringField('Username', validators = [
        validators.DataRequired(),
        validators.Length(1, 30)
    ])
    password = PasswordField('Password', validators = [
        validators.DataRequired(),
        validators.Length(1, 50)
    ])
    submit = SubmitField('Log in')
