from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from flask_wtf import FlaskForm

class Saccotext(FlaskForm):
     text = StringField('Enter message to be sent',validators=[Required()])    
     submit = SubmitField('SEND')