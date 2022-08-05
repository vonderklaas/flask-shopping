from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already exists! Try a different email address')

    username = StringField(label='Enter your username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Enter an email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter your password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm your password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create')

class LoginForm(FlaskForm):
    username = StringField(label='Enter your username:', validators=[DataRequired()])
    password = PasswordField(label='Enter your password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell')