from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    # Check if username already exists
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists, please try a different username')

    # Check if email already exists
    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError('Email already exists, please try a different email')


    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6, max=255), DataRequired()])
    password2 = PasswordField(label='Password Confirm', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register now')
