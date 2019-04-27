<<<<<<< HEAD
from .. import db
from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User  
from flask_login import login_user, logout_user,  login_required
from .forms import RegistrationForm, LoginForm
from ..email import mail_message
=======
from . import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required,current_user
from .. models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from .. email import mail_message
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

<<<<<<< HEAD
    form = LoginForm()
    title = "personal-blog login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods = ["GET","POST"])
=======
    title = "Make or Break!!Welcome to Pitch Panel."
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods = ['GET','POST'])
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

<<<<<<< HEAD
        mail_message("Welcome to my blog","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

=======
        mail_message("Welcome to Pitch Panel","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',registration_form = form)


>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
@auth.route('/auth/logout')
@login_required
def logout():
    logout_user()
<<<<<<< HEAD
    
    return redirect(url_for("main.index"))    
=======

    return redirect(url_for("auth.login"))
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
