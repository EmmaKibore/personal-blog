from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,PasswordField,BooleanField,SubmitField
=======
from wtforms import StringField,PasswordField,SubmitField,BooleanField
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
<<<<<<< HEAD
    
    email = StringField('Your Email Address',validators=[Required(),Email()])

    username = StringField('Enter your username',validators = [Required()])

    password = PasswordField('Password',validators = [Required(), EqualTo('confirm_password',message = 'Passwords must match')])

    confirm_password = PasswordField('Confirm Passwords',validators = [Required()])

    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('That account is taken')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Ooopsy!!That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Email()])

    password = PasswordField('Password', validators = [Required()]) 
    
    remember = BooleanField('Remember Me ')

    submit = SubmitField('Log in ')
=======
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email = data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already in use')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
