from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пороль', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    lastname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пороль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтвердить пороль', validators=[DataRequired(), EqualTo('password')])


