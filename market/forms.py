from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6, max=255), DataRequired()])
    password2 = PasswordField(label='Password Confirm', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register now')
