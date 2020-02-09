from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()], render_kw={'placeholder': 'email'})
    password = PasswordField(validators=[DataRequired()], render_kw={'placeholder': 'password'})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ChatForm(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Send')