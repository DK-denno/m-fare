from flask import render_template,redirect,url_for,flash,request
from .. import db
from flask_login import login_user
from ..models import Sacco
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required
from . import sacco_auth


@sacco_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@sacco_auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        sacco = Sacco(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(sacco)
        db.session.commit()
        return redirect(url_for('sacco_auth.login'))
        title = "New Account"
    return render_template('sacco_auth/registration.html',registration_form = form)
    
@sacco_auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        sacco = Sacco.query.filter_by(email = login_form.email.data).first()
        if sacco is not None and sacco.verify_password(login_form.password.data):
            login_sacco(sacco,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "sacco login"
    return render_template('sacco_auth/login.html',login_form = login_form,title=title)    