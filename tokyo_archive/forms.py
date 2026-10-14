from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class CheckoutForm(FlaskForm):
    address = StringField('Адрес доставки', validators=[DataRequired(), Length(min=5, max=250)])
    phone = StringField('Номер телефона', validators=[DataRequired(), Length(min=6, max=50)])
    submit = SubmitField('Подтвердить заказ')