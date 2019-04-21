from flask import render_template,redirect,url_for
from app import app
from ..import db
from flask_login import login_required
from .. models import User
from . forms import RegistrationForm


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

#views
@app.route('/'')
def index(id):
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch panel'

@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id)
    return render_template('pitch.html', title = title)
