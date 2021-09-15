from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User_account

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1,64),
        Regexp('^[A-Za-z][A-Za-z0-9_]*$',0, 'Username must contain only letters, numbers, and underscores')])
    password = PasswordField('Password', validators=[
                DataRequired(), EqualTo('password_confirm', message='Password must match')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User_account.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered')
