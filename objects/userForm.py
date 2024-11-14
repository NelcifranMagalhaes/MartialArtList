
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField

class UserForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1 , max=8 )])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=1 , max=100 )])
    login = SubmitField('login')

class UserFormCreate(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1 , max=100 )])
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1 , max=8 )])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=1 , max=100 )])
    save = SubmitField('Save')