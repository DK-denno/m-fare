
from flask_wtf import FlaskForm, Form
from wtforms.validators import Required,Email,EqualTo
from..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,\
    RadioField, SelectMultipleField, widgets

class SaccoLoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SaccoRegistrationForm(FlaskForm):
    email = StringField('Business Email Address',validators=[Required(),Email()])
    sacconame = StringField('Sacco Name',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    phone_number = StringField('Sacco Phone Number',validators = [Required()])
    route_choices = [('Nairobi - Mombasa','Nairobi - Mombasa'), ('Mombasa - Kisumu', 'Mombasa - Kisumu'), ('Kisumu - Nairobi', 'Kisumu - Nairobi'),\
              ('Nairobi - Muranga','Nairobi - Muranga'), ('Nairobi - Narok','Nairobi - Narok'), ('Nairobi - Garissa','Nairobi - Garissa'),\
              ('Nairobi - Kajiado','Nairobi - Kajiado'), ('Nairobi - Nakuru','Nairobi - Nakuru'), ('Nairobi - Naivasha','Nairobi - Naivasha'),\
                                        ('Nairobi - Kisumu','Nairobi - Kisumu'), ('Nairobi - Kampala','Nairobi - Kampala'), ('Nairobi - Samburu','Nairobi - Samburu'),\
                                        ('Nairobi - Garissa','Nairobi - Garissa'), ('Nairobi - Mandera','Nairobi - Mandera'), ('Nairobi - Arusha','Nairobi - Arusha'),\
                                        ('Nairobi - Jinja','Nairobi - Jinja'), ('Nairobi - Machakos','Nairobi - Machakos'), ('Nairobi - Marsabit','Nairobi - Marsabit'),\
                                        ('Nairobi - Isiolo','Nairobi - Isiolo'), ('Mombasa - Kampala','Mombasa - Kampala')]
    route = MultiCheckboxField('Routes',choices= route_choices, validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')


    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from flask_wtf import FlaskForm


# class RegistrationForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     username = StringField('Enter your username',validators = [Required()])
#     password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
#     password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
#     submit = SubmitField('Sign Up')

#     def validate_email(self,data_field):
#         if User.query.filter_by(email =data_field.data).first():
#             raise ValidationError('There is an account with that email')

#     def validate_username(self,data_field):
#         if User.query.filter_by(username = data_field.data).first():
#             raise ValidationError('That username is taken')

# class LoginForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     password = PasswordField('Password',validators =[Required()])
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Sign In')    






# class RouteSelectionForm(FlaskForm):
#     route = MultiCheckboxField('Routes', [Required(message= "Please select the Routes you offer")],  choices=[('Nairobi - Mombasa'), ('Mombasa - Kisumu'),('Kisumu - Nairobi'),
#                                               ('Nairobi - Muranga'),('Nairobi - Narok'),('Nairobi - Garissa'),
#                                               ('Nairobi - Kajiado'),('Nairobi - Nakuru'),('Nairobi - Naivasha'),
#                                               ('Nairobi - Kisumu'),('Nairobi - Kampala'),('Nairobi - Samburu'),
#                                               ('Nairobi - Garissa'),('Nairobi - Mandera'), ('Nairobi - Arusha'),
#                                               ('Nairobi - Jinja'), ('Nairobi - Machakos'),('Nairobi - Marsabit'),
#                                               ('Nairobi - Isiolo'),('Mombasa - Kampala')])
