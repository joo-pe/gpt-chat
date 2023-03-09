from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    sendMsg =  TextAreaField("전송할 메세지", 
                            validators=[DataRequired(), Length(min=4, max=200)])
    reqMsg =  StringField("받은 메세지", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("가입")